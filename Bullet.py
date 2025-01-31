import pygame
from Settings import BULLET_IMGS


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, size, pos):
        super().__init__()
        self.size = size
        self.screen = screen
        self.speed = 7

        self.bullet_index = 0
        self.image = BULLET_IMGS[self.bullet_index]
        self.rect = self.image.get_rect(center=pos)
        self.spawn_delay = 10
        self.spawn_timer = 0

    def update(self):
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_delay:
            self.spawn_timer = 0

            self.bullet_index = (self.bullet_index + 1) % len(BULLET_IMGS)
            self.image = BULLET_IMGS[self.bullet_index]

        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
