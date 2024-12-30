import pygame


class Hero(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        self.size = size
        self.x = size[0] // 2
        self.y = size[1] - 60
        self.image = pygame.image.load('images/plane.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 50))
        # self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = 5

    def move(self, pos):
        if 10 < pos < self.size[0] - 80:
            self.rect.x = pos
