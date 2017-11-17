''' This script loads an image and then moves it from left to right alternatively across the primary display surface

It's important to note that x, y represents the top left most position in your image. see diagram below

		   y
		   |
		x -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		   @@@@@@@@@ @@@@@@@@@@@@ @@@@@@@@@
		   @@@@@@@@   @@@@@@@@@@   @@@@@@@@
		   @@@@@@@@  @@@@@@@@@@@@  @@@@@@@@
		   @@@@@@@@  @@@@@@@@@@@@  @@@@@@@@
		   @@@@@@@@  @@@@@@@@@@@@  @@@@@@@@
		   @@@@@@@@   @@@@@@@@@@   @@@@@@@@
		   @@@@@@@@@ @@@@@@@@@@@@ @@@@@@@@@
		   @@@  @@@@@@@@@@@@@@@@@@@@@@  @@@
		   @@@@                        @@@@
		   @@@@@@@@@@            @@@@@@@@@@
		   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@- width
										  |
										height

This means that if you'd like to centralise your image on x, y
you need to subtract half the width and half the height of your image for x, and yield

for example:
	displaysurface.blit(image, (x - image_width / 2, y - image_height / 2)

'''
import sys
import random
import math
import time

import pygame
import pygame.gfxdraw
from pygame.locals import *

pygame.init()

''' DISPLAY SETUP -------------------------------------------------------------------------------- DISPLAY SETUP '''
DISPLAY_WIDTH = 1240
DISPLAY_HEIGHT = 720
DW_HALF = DISPLAY_WIDTH / 2
DH_HALF = DISPLAY_HEIGHT / 2
DISPLAY_AREA = DISPLAY_WIDTH * DISPLAY_HEIGHT
DS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
ground = 147
''' LOAD IMAGES ---------------------------------------------------------------------------------- LOAD IMAGES '''
# Load the image from a file
# Supported formats are JPEG, PNG, GIF
MY_IMAGE = pygame.image.load('mario_still.png')
MY_IMAGE = pygame.transform.scale(MY_IMAGE, (30, 55))
# Get the dimensions of the image by calling the Surface get_rect() function
R = MY_IMAGE.get_rect()

''' SETUP VARIABLES ------------------------------------------------------------------------------ SETUP VARIABLES '''
# determine which why the image is travelling, 1 = right, -1 = left
direction = 1

# starting position is the centre of the display surface
y = 573
x = 10  # .center[0] = half image width, .center[1] = half image height
lead_y_change = 0
lead_x_change = 0
''' FUNCTIONS AND CLASSES ------------------------------------------------------------------------ FUNCTIONS AND CLASSES '''

clock = pygame.time.Clock()
mar = pygame.image.load('marback.jpg').convert()

def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


''' MAIN LOOP ------------------------------------------------------------------------------------ MAIN LOOP '''
while True:
    # event_handler()

    # draw the image in the center of the primary display surface (DS)s

    clock.tick(15)
    # increment or decrement the x position using the direction vector
    # direction vector could be 1 or -1
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_RIGHT:
            lead_x_change += 8
        if event.type == KEYDOWN and event.key == K_LEFT:
            lead_x_change -= 8
        if event.type == KEYUP:
            lead_x_change = 0
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            lead_y_change -= 18


    x += lead_x_change
    # y = DISPLAY_HEIGHT - lead_y_change
    y += lead_y_change
    if y < 550:
        lead_y_change += 6
    if y == 573:
        lead_y_change = 0
    # check if the image has reached either side of the display surface
    if x >= DISPLAY_WIDTH - R.width or x <= 0:
        direction *= -1  # swap the direction vector. -1 becomes 1, 1 becomes -1

    DS.blit(MY_IMAGE, (x, y))
    pygame.display.update()

    # it's important in the this script to clear the display surface after updating
    # overwise you'll see a trail of images as it moves from one side of the display
    # surface to the other. Try deleting the line below and running the script again!

    DS.fill([255, 0, 0])

    mar = pygame.transform.scale(mar, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
    DS.blit(mar, (0, 0))


