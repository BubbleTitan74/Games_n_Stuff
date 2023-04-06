x_var = 0
y_var = 0
while True:

    #pygame.draw.line(screen, YELLOW, (x_var, 0), (x_var, 600))
    #pygame.draw.line(screen, YELLOW, (0, y_var), (800, y_var))
    x_var += 50
    if 800/x_var == 1:
        print("Yippi")
        break