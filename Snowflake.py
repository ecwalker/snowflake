# -*- coding: utf-8 -*-
"""
Snowflake 

Created on Sun Jun 14 20:58:32 2020

@author: ecwal
"""

import pygame
from sys import exit
import random


#initialise pygame
pygame.init()

#Create screen
screen = pygame.display.set_mode((800, 600)) #width, height

#Snowflake
snowImg = []
snowX = []
snowY = []
snowX_change = []
snowY_change = []
snow_direction = []
num_snowflakes = 100

for i in range(num_snowflakes) :
    snowImg.append(pygame.image.load('snow.png'))
    snowX.append(random.randint(1, 800))
    snowY.append(random.randint(1, 600))
    snowX_change.append(0)
    snowY_change.append(0)
    snow_direction.append(random.randint(1, 3))

def snowflake(snowX, snowY, i) :
    screen.blit(snowImg[i], (snowX, snowY))

while True :
    
    screen.fill((211, 226, 245)) #RGB
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
                     
    #Snowflake movement
    for i in range(num_snowflakes) :
        move = 0.1
        if snow_direction[i] == 1 :
            snowX_change[i] = move
            snowY_change[i] = move
        elif snow_direction[i] == 2 :
            snowX_change[i] = 0
            snowY_change[i] = move
        elif snow_direction[i] == 3 :
            snowX_change[i] = -move
            snowY_change[i] = move
        snowX[i] += snowX_change[i]
        snowY[i] += snowY_change[i]
    
    #Snowflake stay in bounds
    for i in range(num_snowflakes) :
        if snowX[i] <= -5 :
            snowX[i] = random.randint(1, 800)
            snowY[i] = 0
            snow_direction[i] = random.randint(1, 3)
        elif snowX[i] >= 805 : #(width - image pixels)
            snowX[i] = random.randint(1, 800)
            snowY[i] = 0
            snow_direction[i] = random.randint(1, 3)
        if snowY[i] <= -5 :
            snowY[i] = 0
            snowX[i] = random.randint(1, 800)
            snow_direction[i] = random.randint(1, 3)
        elif snowY[i] >= 605 : #(height - image pixels)
            snowY[i] = 0
            snowX[i] = random.randint(1, 800)
            snow_direction[i] = random.randint(1, 3)
         #Form snowflake
        snowflake(snowX[i], snowY[i], i)  
        
        

    pygame.display.update()