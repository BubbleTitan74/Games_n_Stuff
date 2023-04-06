import pygame
from coat import Hero

pygame.init()


xPos = 50
yPos = 300
width = 30
height = 70
speed = 12
door_bool = True
cave_bool = False
jump = False
jumpCount = 10
hand_lengt_l = 0
hand_lengt_r = 0
direction = 'right'
door_width = 50

carryOn = True
clock = pygame.time.Clock()
size = (750, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Caves_n_stuff")
all_sprites_list = pygame.sprite.Group()

#______________________________Colours_________________________________
Cave_blue = (45, 58, 70)
Coat_red = (131, 7, 31)
Troll_grey = (56, 59, 56)
Moss_green = (7, 131, 107)
Grass_green = (53, 118, 44)
Cloud_white = (217, 224, 224) 
Door_brown = (180, 190, 50)
Door_colour = Door_brown
Ground = Grass_green
BLUE = (0,0,225)
BLACK = (0, 0, 0)
loading_x = 0
loading_y = 0

CoatHero = Hero(Coat_red, 25, 75, 50)
CoatHero.rect.x = 20
CoatHero.rect.y = 500

all_sprites_list.add(CoatHero)

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

#________________________Funksjoner____________________-

def on_ground(heigth):
    bakketest = True
    bakkenivå = 500-150-heigth
    if ground := bakkenivå and ground != bakkenivå:
        bakketest = False

def troll_enemy(scr, grey, arm,):
    move = 1
    height = 175
    TxPos = 500 + move
    TyPos = 200
    if TxPos == arm:
        height = height - 50
    pygame.draw.rect(scr, grey, [TxPos, TyPos, 75, height])


#______________________________Canvas_______________________________
while carryOn:
    pygame.time.delay(50)

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and xPos > speed:
        xPos -= speed
        direction = 'right'
        #CoatHero.moveLeft(5)
    if keys[pygame.K_d] and xPos < 750 - width- speed:
        xPos += speed
        direction = 'left'
#   if keys[pygame.K_DOWN]:
#   elif not keys[pygame.K_DOWN]:

    if cave_bool == False:
        screen.fill(BLUE)
        pygame.draw.rect(screen, Ground, [0, 350, 750, 150])
        pygame.draw.rect(screen, Cave_blue, [450, 100, 300, 250])
        pygame.draw.rect(screen, BLACK, [650, 260, 50, 90])
        pygame.draw.rect(screen, Door_brown, [650, 260, door_width, 90])

    if cave_bool == True:
        screen.fill(Cave_blue)
        pygame.draw.rect(screen, Ground, [0, 350, 750, 150])
        pygame.draw.rect(screen, BLACK, [50, 260, 50, 90])
        troll_enemy(screen, Troll_grey, xPos)


    if keys[pygame.K_f] and xPos >= 650 and xPos <= 700:
        if door_bool:
            for i in range(10):
                door_width -= 5
            door_bool = False
    if door_bool == False and keys[pygame.K_e]:
        screen.fill(Cave_blue)
        xPos = 30
        Ground = Moss_green
        cave_bool = True

  #  if event.type == pygame.KEYDOWN:
   #     pygame.draw.rect(screen, Coat_red, [xPos, yPos, width, height])
    
    if  jump == False:
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if jumpCount >= -10:
            neg = 1            
            if jumpCount <= 0:
                neg = -1
            yPos -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
            pygame.draw.ellipse(screen, BLACK, [xPos, 350, width, 20])  
        else:
            jump = False
            jumpCount = 10
            mink = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_v and direction == 'left':
                for i in range(20):
                    hand_lengt_l = 20
            if event.key==pygame.K_v and direction == 'right':
                    hand_lengt_r = 20

        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_v and direction == 'left':
                    hand_lengt_l = 0
            if event.key==pygame.K_v and direction == 'right':
                    hand_lengt_r = 0

    pygame.draw.rect(screen, Coat_red, [xPos + width, yPos+30, hand_lengt_l, 7])
    pygame.draw.rect(screen, Coat_red, [xPos - 20, yPos+30, hand_lengt_r, 7])
    pygame.draw.rect(screen, Coat_red, [xPos, yPos, width, height])
    
    pygame.display.flip()  
    clock.tick(FPS)


pygame.quit()



#______________________________Drawing_______________________________

