import pygame
from Settings import explosion_imgs


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center_pos):
        super().__init__()

        self.explosion_index = 0
        self.image = explosion_imgs[self.explosion_index]
        self.rect = self.image.get_rect(center=center_pos)
        self.change_delay = 2
        self.change_timer = 0

    def update(self):
        self.change_timer += 1
        if self.change_timer >= self.change_delay:
            self.change_timer = 0

            self.explosion_index = (self.explosion_index + 1) % len(explosion_imgs)
            self.image = explosion_imgs[self.explosion_index]

        if self.explosion_index == len(explosion_imgs) - 1:
            self.kill()
