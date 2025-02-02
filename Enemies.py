import pygame
import random
from EnemyBullet import EnemyBullet

from Settings import ENEMY_IMG


class Enemy(pygame.sprite.Sprite):
    def __init__(self, size, screen):
        super().__init__()
        self.size = size
        self.screen = screen
        self.x = random.choice([random.randint(-100, 0), random.randint(self.size[0], self.size[0] + 100)])
        self.y = random.randint(60, 180)
        self.image = ENEMY_IMG
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = random.randint(5, 7)

        self.target_x = self.x
        self.target_y = self.y
        self.move_delay = 30  # Задержка перед новым движением (в кадрах)
        self.move_timer = 0
        self.shoot_delay = random.randint(60, 120)  # Задержка между выстрелами
        self.shoot_timer = 0

    def update(self):
        self.move_timer += 1
        self.shoot_timer += 1

        if self.move_timer >= self.move_delay:
            self.set_new_target()
            self.move_timer = 0
        self.move_towards_target()

    def set_new_target(self):
        self.target_x = random.randint(pygame.mouse.get_pos()[0] - 250, pygame.mouse.get_pos()[0] + 250)
        self.target_y = random.randint(10, self.size[1] - 190)

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

    def killed(self):
        self.kill()
        return self.rect.center

    def shoot(self):
        if self.shoot_timer >= self.shoot_delay:
            self.shoot_timer = 0
            return EnemyBullet(self.screen, self.size, self.rect.midbottom)
        return None
