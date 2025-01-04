import pygame
from Settings import point


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, size, pos):
        super().__init__()
        self.size = size
        self.screen = screen
        self.image = point
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = 7

    def update(self):
        super().update()
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
