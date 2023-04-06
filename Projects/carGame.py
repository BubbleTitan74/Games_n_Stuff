import pygame, random
from leCar import Car
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
screen = pygame.display.set_mode(size)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Need_4_$peed")

all_sprites_list = pygame.sprite.Group()
all_comming_cars = pygame.sprite.Group()

SCREENHIGHT =size[1]

BLACK = ( 0, 0, 0)
BLUE = ( 0, 0, 255)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
CYAN = (11, 255, 254)
YELLOW = (255, 248, 57)
PURPLE = (107, 0, 147)
ORANGE = (254, 99, 0)
Road_grey = (106, 106, 106)
Grass_green = (53, 118, 44)
speed = 1
colorList = (CYAN, YELLOW, BLUE, PURPLE)

playerCar = Car(RED, 20, 60, 70)
playerCar.rect.x = 420
playerCar.rect.y = 350

vognTog = Car(BLUE, 65, 200, random.randint(50,100))
vognTog.rect.x = 380
vognTog.rect.y = -1000

car1 = Car(PURPLE, 60, 80, random.randint(50,100))
car1.rect.x = 480
car1.rect.y = -1000
 
car2 = Car(YELLOW, 60, 80, random.randint(50,100))
car2.rect.x = 280
car2.rect.y = -1000
 
car3 = Car(CYAN, 60, 80, random.randint(50,100))
car3.rect.x = 180
car3.rect.y = -1000

all_sprites_list.add(playerCar, vognTog, car1, car2, car3)
all_comming_cars.add(vognTog, car1, car2, car3)


carryOn = True

clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              carryOn = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                carryOn = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight(5) 
    if keys[pygame.K_UP]:
        speed += 0.05
    if keys[pygame.K_DOWN]:
        speed -= 0.05

    if speed >=3:
        speed = 1
    elif speed <= 1:
        speed = 1




    for car in all_comming_cars:
        car.moveForward(speed)
        if car.rect.y > SCREENHIGHT:
            car.changeSpeed(random.randint(50,100))
            car.repaint(random.choice(colorList))
            car.rect.y = -200                   

     # --- Game logic should go here
    all_sprites_list.update()

    car_collision_list = pygame.sprite.spritecollide(playerCar,all_comming_cars,False)
    for car in car_collision_list:
        #End Of Game
        carryOn=False


    
     # --- Drawing code should go here
    screen.fill(Grass_green)
    
    pygame.draw.rect(screen, Road_grey, [150, 0, 400, 500],0)
    pygame.draw.line(screen, WHITE, (150, 0), (150, 500), 2)
    pygame.draw.line(screen, WHITE, (250, 0), (250, 500), 2)
    pygame.draw.line(screen, WHITE, (350, 0), (350, 500), 2)
    pygame.draw.line(screen, WHITE, (450, 0), (450, 500), 2)
    pygame.draw.line(screen, WHITE, (550, 0), (550, 500), 2)
    all_sprites_list.draw(screen)

	



     # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
     # --- Limit to 60 frames per second
    clock.tick(60)


"""
explosion_colour = (255, random.randint(40, 220), 0)
explosion_size = random.randint(50, 100)
explosion_pos = (random.randint(100, 400), random.randint(100, 600))
if carryOn == False:
    screen.fill(ORANGE)
    for _ in range(10):
        pygame.draw.circle(screen, explosion_colour, explosion_pos, explosion_size)
"""
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()