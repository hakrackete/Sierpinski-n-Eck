from math import *
import pygame
import random
width = 900
height = 900

clock = pygame.time.Clock()

run = True

# method for the Fractal, either only the previous one cannot be used or the two previous ones, both can be disabled
noprevious = False
notwoprevious = False
pygame.init()


window = pygame.display.set_mode((width, height))
window.fill((0,0,0))

# how much corners u want:
corners = 3

#sometimes, u want a rotated Image (pi = 180°)
rotate_image = 0

#its the radius form the Midpoint beginning
length = 400

#empty list for the cornerpoints:
points = []

#Midpoints
place_x = width/2
place_y = height/2

#creating all corners
for i in range(0,corners):
    points.append((int(place_x + length*(sin(i*radians(360/corners) + rotate_image))),(int(place_y + length*(cos(i*radians(360/corners) + rotate_image))))))

# the starting point which is inside the n-gon
randompoint = (width/2,height/2)

# splitting in x and y-coordinates
mid_x = randompoint[0]
mid_y = randompoint[1]

#creating the 2 previous chosen verticies
prevvertex_a = 0
prevvertex_b = 1

#check if a chosen verticies is neighbour with another one
def isneighbour(vertex, prevvertex_a):
    if abs(vertex - prevvertex_a) == 1:
        return True
    elif abs(vertex - prevvertex_a) > corners - 2:
        return True
    else:
        return False

# draws the outside:
for i in range(0, corners):
    #pygame.draw.circle(window, (255, 255, 255), points[i], 2)
    pygame.draw.aaline(window, (255, 255, 255), points[i], points[(i + 1) % corners], 1)
    #pygame.draw.circle(window, (255, 255, 255), randompoint, 2)

while run:
    #clock.tick(120)
    vertex = random.randint(0, corners - 1)     #chooses a random vertex
    if noprevious:
        while vertex == prevvertex_a:           #new vertex, until it is not the previous one
            vertex = random.randint(0,corners - 1)
    elif notwoprevious:
        if prevvertex_a == prevvertex_b:        #new vertex, but only if the previous one were the same, and then no neighbours
            while isneighbour(vertex,prevvertex_a) and isneighbour(vertex,prevvertex_b) :
                vertex = random.randint(0, corners - 1)
    #vericies get older:
    prevvertex_b = prevvertex_a
    prevvertex_a = vertex

    #calculates the newest points from the middle between the chosen vertex and the current point
    mid_x = int((points[vertex][0] + mid_x)/2)
    mid_y = int((points[vertex][1] + mid_y) / 2)

    pygame.draw.line(window, (255, 255, 255),(mid_x,mid_y) , (mid_x,mid_y) , 1)


    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
       run = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()