# Steve Stoll (4/2/2013)
# This program is a simple PyGame template.
# Import the pygame and sys libraries
import pygame
import sys
from pygame.locals import *

def namedisplayText(text, xPos, yPos, fontName, fontSize, f_colour, b_colour):
    fontObj = pygame.font.Font(fontName, fontSize)
    textSurfaceObj = fontObj.render(text, True, f_colour, b_colour)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (xPos, yPos)
    SCREEN.blit(textSurfaceObj, textRectObj)

xPos = 0
yPos = 0
# Set screen width and height
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLACK = (0,0,0)
GREEN = (0, 255, 0)
fontName='freesansbold.ttf'
fontSize=32
fontColor=BLACK
BackgroundColor= GREEN
# Frames per second
FPS = 8
# Initialize PyGame
pygame.init()
fpsClock = pygame.time.Clock()
# Set the screen size
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
# Fill the screen with green.
SCREEN.fill((0, 255, 0))
# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            xPos = pygame.mouse.get_pos()[0]
            yPos = pygame.mouse.get_pos()[1]

        text = f" [{xPos}],[{yPos}] "

    namedisplayText(text, 100, 20, fontName, fontSize, BLACK, GREEN)
# Mouse events or mouse logic may go here...
    pygame.display.flip()
    fpsClock.tick(FPS)

