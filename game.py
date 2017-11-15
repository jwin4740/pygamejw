import pygame


# initialize pygame
x = pygame.init()
print(x)

# surface for game to be seen by user

gameDisplay = pygame.display.set_mode((800,600))  # parameter is a tuple to set view size
pygame.display.set_caption('Snake')
# pygame.display.flip()  # like a flipped book comic

pygame.display.update()  # can update a specific element

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        print(event)





pygame.quit()  # quits and uninitializes

quit()  # quits python
