import pygame

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, screen, window_size, pos):
        super().__init__()
        self.screen = screen
        self.window_size = window_size
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 0, 0))  # Красный цвет для пули врага
        self.rect = self.image.get_rect(center=pos)
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > self.window_size[1]:
            self.kill()