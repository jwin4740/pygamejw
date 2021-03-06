import pygame


# initialize pygame
x = pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


# surface for game to be seen by user

gameDisplay = pygame.display.set_mode((1000,800))  # parameter is a tuple to set view size gameSurface object
pygame.display.set_caption('Snake')
# pygame.display.flip()  # like a flipped book comic



gameExit = False

lead_x = 300
lead_y = 300
lead_x_change = 0

clock = pygame.time.Clock()

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change -= 10
            if event.key == pygame.K_RIGHT:
                lead_x_change += 10

    lead_x += lead_x_change

    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay, white, [lead_x, lead_y, 10, 10])
    pygame.display.update()

    clock.tick(15)  # frames/second

#     fill method get accelerated processing compared to draw
#     gameDisplay.fill(red, rect=[200, 200, 50, 50])


# quits and uninitializes pygame
pygame.quit()

quit()  # quits python
