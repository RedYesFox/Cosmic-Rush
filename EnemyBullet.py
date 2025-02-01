import pygame
from Settings import enemy_bullet

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, screen, window_size, pos):
        super().__init__()
        self.screen = screen
        self.window_size = window_size
        self.image = enemy_bullet
        self.rect = self.image.get_rect(center=pos)
        self.speed = 7

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > self.window_size[1]:
            self.kill()