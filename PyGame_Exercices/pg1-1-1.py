#______________________________This_Game________________________
#The purpose of this exercice is to get better with pygame to make games that
#comes to mind.
#______________________________Libraries________________________
import pygame, sys
from pygame.locals import *
#______________________________Functions________________________

#______________________________Identifiers______________________
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('PyGame Rocks!')
screen = (200, 100)
#______________________________Logic____________________________
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
#______________________________Drawing__________________________

#______________________________Ending___________________________
    pygame.display.update()
