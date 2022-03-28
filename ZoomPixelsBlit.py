import pygame
import os

# Create diagram of how blit is a pixel to pixel transfer of a rectangular area


def grid(surface, color, pixels, loc, size):
    # draw grid of pixels width, at location, with size the number of cells wide and high
    x, y = loc
    w, h = size
    for i in range(w+1):
        pygame.draw.line(surface, color, (x + i * pixels, y), (x + i * pixels, y + w * pixels), 1)
    for i in range(h+1):
        pygame.draw.line(surface, color, (x, y + i * pixels), (x + h * pixels, y + i * pixels), 1)


os.environ['SDL_VIDEO_WINDOW_POS'] = "1060,100"  # where window is located

pygame.init()
screen = pygame.display.set_mode((900, 800))
screen.fill((255, 255, 255))  # white background
image = pygame.image.load("In-yang.png")  # create picture surface

scale = 8
black = 0, 0, 0

img2 = pygame.transform.scale(image, (16*scale, 16*scale))

screen.blit(img2, (60, 60))
screen.blit(img2, (80+(16+10)*scale, 60+10*scale))

grid(screen, black, 8, (60, 60), (16, 16))
grid(screen, black, 8, (80+16*scale, 60), (40, 40))
pygame.display.flip()  # write to screen

while True:  # loop till quit
    for event in pygame.event.get():  # loop to get all events
        if event.type == pygame.QUIT:
            sys.exit()
