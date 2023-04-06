#______________________________This_Game________________________
#The purpose of this exercice is to get better with pygame to make games that
#comes to mind.
#______________________________Libraries________________________
import pygame, sys, random
from pygame.locals import *
#______________________________Functions________________________

#______________________________Identifiers______________________
pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Geometry_Wars')
screen = (200, 100)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
BRIGHTBLUE = (0, 150, 255)
YELLOW = (255, 225, 0)
FUCHSIA = (255, 0, 255)
RED = (255, 0, 0)
colour_list_int = [BLACK, WHITE, YELLOW, FUCHSIA]
colour_list_str = ["BLACK", "WHITE", "YELLOW", "FUCHSIA"]
screen = pygame.display.set_mode((800,600))
pointlist1 = [(46, 217), (82, 204), (93, 169), (104, 204), (139, 217), (104, 227), (93, 263), (81, 228)]
posx = random.sample(range(0, 800), 10)
posy = random.sample(range(0, 600), 10)
pos_x_b = random.sample(range(0, 800), 5)
pos_y_b = random.sample(range(0, 600), 5)
pos_x_r = random.sample(range(0, 800), 10)
pos_y_r = random.sample(range(0, 600), 10)

#______________________________Logic____________________________
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
#______________________________Drawing__________________________

    screen.fill(BLACK)

    x_var = 0
    y_var = 0
    for i in range(16):
        if y_var != 650:
            pygame.draw.line(screen, YELLOW, (0, y_var), (800, y_var), 1)
        pygame.draw.line(screen, YELLOW, (x_var, 0), (x_var, 600), 1)
        x_var += 50
        y_var += 50
        
    pygame.draw.polygon(screen, WHITE, pointlist1, 5)
    
    for i in range(0, 10):
        pygame.draw.circle(screen, WHITE, (posx[i],posy[i]), 20, 0)

    for i in range(5):
        pygame.draw.ellipse(screen, BRIGHTBLUE, (pos_x_b[i], pos_y_b[i], 40, 80), 2)

    for i in range(10):
        pygame.draw.rect(screen, RED, (pos_x_r[i], pos_y_r[i], 40, 80), 3)    

            
#______________________________Ending___________________________
    pygame.display.update()
