import matplotlib.pyplot as plt
import pygame
import numpy as np
import random
from video import make_video
pygame.init()
width = 1000
height = 1000
no = 100
resolution = int(width/no)
#box = 
main_surface = pygame.display.set_mode((width,height))
save_screen = make_video(main_surface, "anti")

arr = np.zeros((no,no), dtype="uint8")
nex = np.zeros((no,no), dtype="uint8")
lifedeath = np.zeros((no,no), dtype="uint8")

single = np.zeros((no,no), dtype="uint8")
for x in range(no):
    for y in range(no):
        arr[x][y] = random.randint(0,1)
print(arr)

def countNeighbours(ar, x, y):
    summ = 0
    for i in range(3):
        for j in range(3):
            q = (x-1+i+no) % no
            #print(x)
            w = (y-1+j+no) % no
            #if x < no and y < no:
            summ += ar[q][w]
            #if not lifedeath[q][w] == 255 and not lifedeath[q][w] == 125 and  not lifedeath[q][w] == 0:
                #summ +=1
                
    summ -= ar[x][y]
    return summ
    
def draw():
    main_surface.fill((0,0,0))
    for i in range(no):
        for j in range(no):
            x = int(i * resolution)
            y = int(j * resolution)
            if arr[i][j] == 1 and lifedeath[i][j] == 255:
                pass#pygame.draw.rect(main_surface, (125,255,125), (x,y,resolution,resolution))
            elif arr[i][j] == 0 and lifedeath[i][j] == 125:
                pass#pygame.draw.rect(main_surface, (125,255,125), (x,y,resolution,resolution))
            elif arr[i][j] == 1 and lifedeath[i][j] == 0:
                pass#pygame.draw.rect(main_surface, (125,255,125), (x,y,resolution,resolution))
            else:#single[i][j] == 1:
                pygame.draw.rect(main_surface, (125,255,255), (x,y,resolution,resolution))
    """      
    ra1 = random.randint(0,no-2)
    ra2 = random.randint(0,no-2)
    arr[ra1][ra2] = random.randint(0,1)
    arr[ra1+1][ra2+1] = random.randint(0,1)
    arr[ra1-1][ra2-1] = random.randint(0,1)
    arr[ra1-1][ra2] = random.randint(0,1)
    arr[ra1][ra2-1] = random.randint(0,1)
    arr[ra1+1][ra2] = random.randint(0,1)
    arr[ra1][ra2+1] = random.randint(0,1)
    arr[ra1+1][ra2-1] = random.randint(0,1)
    """
    for i in range(no):
        for j in range(no):
            state = arr[i][j]
            prev = lifedeath[i][j]
        #Count neighbours that live
            summ = 0
            neighbours = countNeighbours(arr, i, j)
            
            if lifedeath[i][j] == 255:
                neighmin = 1
                neighmax = 3#random.randint(2,3)
            elif lifedeath[i][j] == 125:
                neighmin = 10
                neighmax = 0
            else:
                neighmin = 2
                neighmax = 3
                
            if state == 0 and neighbours == 3:
                nex[i][j] = 1
                lifedeath[i][j] = 255
            #elif state == 1 and neighbours < 2 or neighbours > 3:
            elif state == 1 and neighbours < neighmin or neighbours > neighmax:
                nex[i][j] = 0
                lifedeath[i][j] = 125
            else:
                nex[i][j] = state
                lifedeath[i][j] = 0
            #print(neighbours)
        
    for i in range(no):
        for j in range(no):
            arr[i][j] = nex[i][j]
    for i in range(no):
        for j in range(no):
            neighbours = countNeighbours(nex, i, j)
            if neighbours > 0:
                single[i][j] = 0
            else:
                single[i][j] = 1
                
            
def loop():
    while True:
        ev = pygame.event.poll()
        #pygame.display.flip()
        next(save_screen)
        draw()
loop() 
#pygame.draw.line(main_surface, (255,255,255), (x, y), (x, y), 1)
