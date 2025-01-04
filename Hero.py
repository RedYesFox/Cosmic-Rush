import pygame

from Settings import HERO_IMG


class Hero(pygame.sprite.Sprite):
    def __init__(self, screen, size):
        super().__init__()
        self.size = size
        self.screen = screen
        self.x = size[0] // 2
        self.y = size[1] - 60
        self.image = HERO_IMG
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = 5

    def move(self, pos):
        if 10 < pos < self.size[0] - 80:
            self.rect.x = pos

    def shot(self):
        return self.rect.center
