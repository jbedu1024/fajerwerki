import pygame

import random

class Flame:
    def __init__(self):
        self.rect = pygame.Rect(640, 200, 10, 10)
        self.image = pygame.Surface( (10,10) )
        self.image.fill( (random.randint(100,255), random.randint(100,255), random.randint(100, 255) ) )
        self.Vy = -12 * random.random() - 1
        self.Vx = random.random() * 20 - 10
        self.px = 640
        self.py = 200

    def update(self):
        self.Vy += 0.2
        self.px += self.Vx
        self.py += self.Vy
        self.rect.x = self.px
        self.rect.y = self.py
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)