import pygame

from Settings import FONT2

pygame.init()
size_s = (60, 60)


class Heart(pygame.sprite.Sprite):
    def __init__(self, screen, size):
        super().__init__()
        self.screen = screen
        self.size = size
        self.HEART_IMGS = [
            pygame.transform.scale(pygame.image.load('images/0h.png'), size_s),
            pygame.transform.scale(pygame.image.load('images/30h.png'), size_s),
            pygame.transform.scale(pygame.image.load('images/65h.png'), size_s),
            pygame.transform.scale(pygame.image.load('images/100h.png'), size_s)]
        self.heart_index = 3
        self.image = self.HEART_IMGS[self.heart_index]
        self.rect = pygame.Rect(0, 0, 60, 60)
        self.rect = self.rect.move(20, 20)


class Shield(pygame.sprite.Sprite):
    def __init__(self, screen, size):
        super().__init__()
        self.screen = screen
        self.size = size
        self.image = pygame.transform.scale(pygame.image.load('images/shield.png'), size_s)
        self.rect = pygame.Rect(0, 0, 60, 60)
        self.rect = self.rect.move(270, 20)

    def update(self):
        pass


class Text:
    def __init__(self, screen, size):
        super().__init__()
        self.screen = screen
        self.width, self.height = self.size = size

    def draw(self, HP, SHIELD, LVL, SCORE):
        text_h = FONT2.render(f'HP {HP}%', True, (255, 255, 255))
        text_s = FONT2.render(f'Shield {SHIELD}%', True, (255, 255, 255))
        text_lvl = FONT2.render(f'LVL: {LVL}', True, (255, 255, 255))
        text_score = FONT2.render(f'SCORE: {SCORE}', True, (255, 255, 255))
        self.screen.blit(text_h, (90, 30))
        self.screen.blit(text_s, (330, 30))
        self.screen.blit(text_lvl, (self.width // 2 - text_lvl.get_width() // 2, 60))
        self.screen.blit(text_score, (self.width - text_score.get_width() - 20, 30))
