import pygame


class Hero(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        self.size = size
        self.x = size[0] // 2
        self.y = size[1] - 100
        self.image = pygame.image.load('images/plane.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = 5
        self.bullet_speed = 10

    def move(self, pos):
        if 10 < pos < self.size[0] - 80:
            self.rect.x = pos
