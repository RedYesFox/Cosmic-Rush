import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        self.size = size
        self.x = random.choice([random.randint(-100, 0), random.randint(self.size[0], self.size[0] + 100)])
        self.y = random.randint(60, 180)
        print(self.x, self.y)
        self.image = pygame.image.load('images/red_plane.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = random.randint(4, 8)
    #     self.can = True
    #
    # def can_move(self):
    #     self.can = not self.can
    #
    # def move(self):
    #     if self.rect.center[0] < self.size[0] // 2:
    #         self.rect.x += self.speed
    #     if self.rect.center[1] < 180:
    #         self.rect.y += self.speed

        self.target_x = self.x
        self.target_y = self.y
        self.move_delay = 10  # Задержка перед новым движением (в кадрах)
        self.move_timer = 0

    def update(self):
        self.move_timer += 1
        if self.move_timer >= self.move_delay:
            self.set_new_target()
            self.move_timer = 0

        self.move_towards_target()

    def set_new_target(self):
        self.target_x = random.randint(10, self.size[0] - 10)
        self.target_y = random.randint(20, 300)

    def move_towards_target(self):
        dx = self.target_x - self.rect.centerx
        dy = self.target_y - self.rect.centery
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance > self.speed:
            move_ratio = self.speed / distance
            self.rect.x += dx * move_ratio
            self.rect.y += dy * move_ratio
        else:
            self.rect.center = (self.target_x, self.target_y)