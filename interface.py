import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280,720))

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('lightblue')
    
    pygame.display.update()
