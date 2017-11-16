import pygame


# initialize pygame
x = pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


# surface for game to be seen by user

gameDisplay = pygame.display.set_mode((800,600))  # parameter is a tuple to set view size gameSurface object
pygame.display.set_caption('Snake')
# pygame.display.flip()  # like a flipped book comic



gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay, white, [400, 300, 10, 10])

# fill method get accelerated processing compared to draw
    gameDisplay.fill(red, rect=[200, 200, 50, 50])

    pygame.display.update()
# quits and uninitializes pygame
pygame.quit()

quit()  # quits python
