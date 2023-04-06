# Modified for classroom standards and timing.
# Steve Stoll (3/24/2013)
## This program allows users to move a cat using the keyboard.
## Import the pygame and sys libraries
import pygame
import sys
from pygame.locals import *
## The images are in the same folder as the program
backgroundImg = "background.jpg"
catImg = "cat.png"
## Use the following code if you want to place the images in a 
##    sub-folder named images.
        ##bkg_img = "\images\background.jpg"
        ##mouse_img = "\images\cat.png"
## Set the x, y, directionX, directionY variables
xPos = 0
yPos = 0
# Indicates the x or y direction (+value, -value or zero)
directionX = 0
directionY = 0
# Set screen width and height
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
## Initialize PyGame
pygame.init()

#_____FPS and clock for the program to limit the figures speed______
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

## Set the screen size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
## Load the background and cursor images.
background = pygame.image.load(backgroundImg).convert()
cat = pygame.image.load(catImg).convert_alpha()

## Main loop
while True:
    ## Logic to cleanup after user presses close (red X)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        ## event logic to capture when the user presses arrow keys.
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                directionX = -1

            elif event.key == K_RIGHT:
                directionX = +1

            elif event.key == K_UP:
                directionY = -1
            elif event.key == K_DOWN:
                 directionY = +1

        if event.type == KEYUP:
            if event.key == K_LEFT:
                directionX = 0
            elif event.key == K_RIGHT:
                directionX = 0
            elif event.key == K_UP:
                directionY = 0
            elif event.key == K_DOWN:
                 directionY = 0
    ## This logic identifies where the object should move
    xPos += directionX
    yPos += directionY
    ## Repaint the screen with the objects in the new positions
    screen.blit(background, (0, 0))
    screen.blit(cat, (xPos, yPos))

    pygame.display.flip()
    fpsClock.tick(FPS)

