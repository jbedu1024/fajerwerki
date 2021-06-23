import pygame

from firework import Firework

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

firework = Firework()

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    firework.update()

    screen.fill( (0,0,0) )

    firework.draw(screen)

    pygame.display.update()