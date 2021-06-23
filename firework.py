import pygame
from flame import Flame

class Firework:
    def __init__(self):
        self.rect = pygame.Rect(640, 720, 25, 50)
        self.image = pygame.Surface( (25, 50) )
        self.image.fill( (255, 255, 255) )
        self.exploded = False
        self.flames = [] 

    def update(self):
        if not self.exploded:
            self.rect.y -= 2
            if self.rect.y <= 200:
                self.explode()
        else:
            for flame in self.flames:
                flame.update()

    def draw(self, screen):
        if not self.exploded:
            screen.blit(self.image, self.rect)
        else:
            for flame in self.flames:
                flame.draw(screen)

    def explode(self):
        self.exploded = True
        for i in range(1000):
            self.flames.append(Flame())