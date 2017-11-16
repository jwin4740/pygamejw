import pygame

# initialize pygame
x = pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
screen_width = 1000
screen_height = 600
# surface for game to be seen by user

gameDisplay = pygame.display.set_mode(
    (screen_width, screen_height))  # parameter is a tuple to set view size gameSurface object
pygame.display.set_caption('PyMario')
mar = pygame.image.load('marback.jpg').convert()
mar = pygame.transform.scale(mar, (screen_width, screen_height))
still_mario = pygame.image.load('mario_still.png').convert()
running_mario = pygame.image.load('mario_running.png').convert()
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
    gameDisplay.blit(mar, (0, 0))
    pygame.draw.rect(gameDisplay, white, [lead_x, lead_y, 10, 10])
    pygame.display.update()

    clock.tick(15)  # frames/second

# fill method get accelerated processing compared to draw
#     gameDisplay.fill(red, rect=[200, 200, 50, 50])


# quits and uninitializes pygame
pygame.quit()

quit()  # quits python
