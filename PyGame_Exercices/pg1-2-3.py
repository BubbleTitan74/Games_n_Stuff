#______________________________This_Game________________________
#The purpose of this exercice is to get better with pygame to make games that
#comes to mind.
#______________________________Libraries________________________
import pygame, sys
from pygame.locals import *

#______________________________Func_________________________-

def change_pos():
    pos = input("New pos")
    pos_x, pos_y = pos.split(",")
    pos_x, pos_y = int(pos_x), int(pos_y)
    if pos_x >= 500 and pos_x <= 0 and pos_y >= 500 and pos_y <= 0:
        print("invalid")
        pygame.quit()
        sys.exit()
    return pos_x, pos_y
#______________________________Identifiers______________________
pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 500))
pygame.display.set_caption('PyGame Rocks!')
screen = (500, 500)
pos_x, pos_y = change_pos()
myRect = pygame.Rect(pos_x, pos_y, 100, 200)
RED = (255, 0, 0)
DISPLAYSURF.fill(RED, myRect)

print(f"This is the pos 4 the right side of myRect {myRect.right}")
print(f"This is the pos 4 the bottom right side of myRect {myRect.bottomright}")


#______________________________Logic____________________________
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    change_pos()

#______________________________Drawing__________________________

#______________________________Ending___________________________
    pygame.display.update()