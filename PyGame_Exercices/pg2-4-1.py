import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
BLACK = (0,0,0)
catImg = pygame.image.load('cat.png')
catImg_copy = catImg.copy()
catImg_flip = pygame.transform.flip(catImg_copy, True, False)
catx = 50
caty = 50
cat = catImg
direction = 'down'
MOVE_AMOUNT = 5
soundObj = pygame.mixer.Sound('beeps.wav')

pygame.mixer.music.load('ahhh.mp3')
pygame.mixer.music.play(3, 5.2)

while True: # the main game loop
    DISPLAYSURF.fill(BLACK)

    if direction == 'down':
        caty += MOVE_AMOUNT
        if caty == 220:
            direction = 'right'
            cat = catImg_flip
            soundObj.play()
    elif direction == 'right':
        retning = 0
        catx += MOVE_AMOUNT
        if catx == 250:
            direction = 'up'
            soundObj.play()
    elif direction == 'up':
        caty -= MOVE_AMOUNT
        if caty == 10:
            direction = 'left'
            cat = catImg
            soundObj.play()
    elif direction == 'left':
        retning = 1
        catx -= MOVE_AMOUNT
        if catx == -10:
            direction = 'down'
            soundObj.play()

    DISPLAYSURF.blit(cat, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)