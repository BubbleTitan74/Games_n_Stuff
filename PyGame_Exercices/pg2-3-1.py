#______________________________This_Game________________________
#The purpose of this exercice is to get better with pygame to make games that
#comes to mind.
#______________________________Libraries________________________
import pygame, sys
from pygame.locals import *
#______________________________Functions________________________
def namedisplayText(text, xPos, yPos, fontName, fontSize, f_colour, b_colour):
    fontObj = pygame.font.Font(fontName, fontSize)
    textSurfaceObj = fontObj.render(text, True, f_colour, b_colour)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (xPos, yPos)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
#______________________________Identifiers______________________
pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 500))
pygame.display.set_caption('PyGame Rocks!')
screen = (500, 500)
BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
fontName='freesansbold.ttf'
fontSize=32
fontColor=BLACK
BackgroundColor= GREEN
txt_pos = 250
FPS = 40 # frames per second setting
fpsClock = pygame.time.Clock()
#______________________________Logic____________________________
while True: # main game loop
    text = input("What do you want to call you game?")
    namedisplayText(text, txt_pos, txt_pos, fontName, fontSize, GREEN, BLUE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
#______________________________Drawing__________________________

#______________________________Ending___________________________
    pygame.display.update()
    fpsClock.tick(FPS)

