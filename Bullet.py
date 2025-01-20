import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, size, pos):
        super().__init__()
        self.size = size
        self.screen = screen
        self.speed = 7

        self.BULLET_IMGS = [
            pygame.transform.rotate(pygame.transform.scale(pygame.image.load('images/bullet_1.png'), (80, 20)), 90),
            pygame.transform.rotate(pygame.transform.scale(pygame.image.load('images/bullet_2.png'), (80, 20)), 90),
            pygame.transform.rotate(pygame.transform.scale(pygame.image.load('images/bullet_3.png'), (80, 20)), 90),
            pygame.transform.rotate(
                pygame.transform.flip(pygame.transform.scale(pygame.image.load('images/bullet_2.png'), (80, 20), ),
                                      False, True), 90)]
        self.bullet_index = 0
        self.image = self.BULLET_IMGS[self.bullet_index]
        self.rect = pygame.Rect(0, 0, 40, 10)
        self.rect = self.rect.move(*pos)
        self.spawn_delay = 10
        self.spawn_timer = 0

    def update(self):
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_delay:
            self.spawn_timer = 0

            self.bullet_index = (self.bullet_index + 1) % len(self.BULLET_IMGS)
            self.image = self.BULLET_IMGS[self.bullet_index]

        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
