import pygame
from Settings import HERO_IMG
import Settings


class Hero(pygame.sprite.Sprite):
    def __init__(self, screen, size):
        super().__init__()
        self.size = self.screen_width, self.screen_height = size
        self.screen = screen
        self.x = size[0] // 2
        self.y = size[1] - 60
        self.image = HERO_IMG
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = 5

    def move(self, pos):
        if 10 < pos < self.size[0] - 100:
            self.rect.centerx = pos

    def shot(self):
        return self.rect.center

    def reset(self):
        self.rect.centerx = self.screen_width // 2
        self.rect.bottom = self.screen_height - 10
        Settings.HEALTH = 100
        Settings.SHIELD = 100
