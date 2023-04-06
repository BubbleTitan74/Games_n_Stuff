import pygame, random
pygame.init()

carryOn = True

clock = pygame.time.Clock()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("BOOM")

#________________________________Values______________________________
smell = 50
size = random.sample(range(50, 100), smell)
posx = random.sample(range(100, 400), smell)
posy = random.sample(range(200, 500),smell)

#______________________________Colours_________________________________
rand_Ex = random.sample(range(40, 220), smell) 
explosion_colour = (255, rand_Ex, 0)


ORANGE = (254, 99, 0)
sky_blue = (69, 211, 255)


#______________________________Canvas_______________________________
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        
#______________________________Drawing_______________________________
    screen.fill(sky_blue)
    for i in range(0, smell):
        pygame.draw.circle(screen, (255, rand_Ex[i], 0), (posx[i],posy[i]), size[i])

#_________________________________End_____________________________________
    pygame.display.flip()
     
clock.tick(60)
 
pygame.quit()
    



