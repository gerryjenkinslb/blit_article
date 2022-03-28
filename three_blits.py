import pygame
import os
import sys

# demo of three ways to use blit method for a surface
# blit surface to another surface
# blit part of surface to another surface
# blit part of a surface to itself


def wait_key():  # await any key or quit event
    pygame.display.flip()  # write to screen then wait
    while True:  # keep looping till key
        for event in pygame.event.get():  # loop to get all events
            if event.type == pygame.KEYDOWN:  # if key, then return
                return
            elif event.type == pygame.QUIT:
                sys.exit()

# setup
os.environ['SDL_VIDEO_WINDOW_POS'] = "1100,100"   # where window is located
bgcolor = 100, 100, 100
pygame.init()
screen = pygame.display.set_mode((800, 800)) # create surface 'screen;' associated with display
image = pygame.image.load("letterbox.png").convert()  # create picture surface, convert makes it faster for blit
screen.fill(bgcolor)

# -------- 1. Basic blit: whole surface (image) to screen or other surface
screen.blit(image, (50, 50))  # copy block picture to screen at (x,y) or dest
wait_key()

# -------- 2. blit area of surface (image) to screen (letter F)
from_area = pygame.Rect(264, 133, 135, 135)
screen.blit(image, (75, 470), from_area)  # area of image to screen or other surface
wait_key()

# -------- 3. blit from area of screen to another place on screen, letter E
from_area = pygame.Rect(50+133, 50+133, 134, 134)
pygame.draw.rect(screen, (255, 255, 0), from_area, 9)  # modify the screen to verify, we are not coping the image
screen.blit(screen, (230, 550), from_area)  # screen to screen
wait_key()

