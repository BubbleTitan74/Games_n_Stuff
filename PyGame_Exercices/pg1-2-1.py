#______________________________This_Game________________________
#The purpose of this exercice is to get better with pygame to make games that
#comes to mind.
#______________________________Libraries________________________
import pygame, sys
from pygame.locals import *

pygame.init()
#_______________________________Functions________________________

def colour_time(colour_list_str):
    while True:
        colour_input = input("What colour?")
        if colour_input.upper() not in colour_list_str:
            print("Colour not in list.")
        else:
            break
        return colour_input

def choose_colour(colour, colour_list_str, colour_list_int):
    chk = 0
    for colour in colour_list_str:
        if colour in colour_list_str:
            choosen_colour = colour_list_int[chk]
    return choosen_colour

def size_time():
    while True:
        size_input = input("How big do you want the screen in x and y?")
        size_input_x, size_input_y = size_input.split(",")
        if size_input_x.isnumeric() and size_input_y.isnumeric == False:
            print("You input is not noumeric")
        elif int(size_input_x) and int(size_input_y) >= 1000:
            print("Your input exceeds 1000")
        else:    
            break
    return int(size_input_x), int(size_input_y)

def name_time():
    while True:
        name_input = input("Name of the Game?")
        if len(name_input) <= 2 or name_input[0].isalpha == False:
            print("Invalid name")
        else:
            break
    return name_input

#______________________________Identifiers______________________
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption(f'{name_time()}')
size_x, size_y = size_time()
print(size_x, size_y)
screen = pygame.display.set_mode((size_x, size_y))

BLACK = (255, 255, 255)
WHITE = (0,0,0)
YELLOW = (255, 225, 0)
FUCHSIA = (255, 0, 255)
colour_list_int = [BLACK, WHITE, YELLOW, FUCHSIA]
colour_list_str = ["BLACK", "WHITE", "YELLOW", "FUCHSIA"]

screen_colour = colour_time(colour_list_str)
print(screen_colour)


#______________________________Logic____________________________

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

#___________________Functions___________________



#______________________________Drawing__________________________

    screen.fill(choose_colour(screen_colour, colour_list_str, colour_list_int))

#______________________________Ending___________________________
    pygame.display.update()

