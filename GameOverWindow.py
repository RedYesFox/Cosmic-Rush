import pygame
import math

from Settings import PAUSE_FONT2, PAUSE_FONT1


class GameOverWindow:
    def __init__(self, screen, window_size):
        self.screen = screen
        self.window_size = self.width, self.height = window_size
        self.font = pygame.font.Font(None, 74)
        self.text = self.font.render("GAME OVER", True, (255, 0, 0))
        self.text_rect = self.text.get_rect(center=(window_size[0] // 2, window_size[1] // 2))
        self.alpha = 0
        self.fade_speed = 5

        bg_color = (0, 0, 0, 190)
        self.surface = pygame.Surface(self.window_size, pygame.SRCALPHA)
        self.surface.fill(bg_color)
        self.resume_text = PAUSE_FONT2.render("Нажмите R чтобы начать сначала", True, (200, 200, 200))
        self.return_text = PAUSE_FONT2.render("Нажмите ESC для возврата на стартовое окно", True, (200, 200, 200))
        self.quit_text = PAUSE_FONT1.render("Нажмите E для выхода", True, (200, 200, 200))

    def draw(self):
        self.screen.blit(self.surface, (0, 0))

        self.alpha = 128 + 127 * math.sin(pygame.time.get_ticks() * 0.005)
        text_surface = pygame.Surface(self.text.get_size(), pygame.SRCALPHA)
        text_surface.fill((255, 0, 0, self.alpha))
        text_surface.blit(self.text, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        self.screen.blit(text_surface, self.text_rect)

        self.screen.blit(self.resume_text, (self.width // 2 - self.resume_text.get_width() // 2,
                                            self.text_rect.midbottom[1] + self.resume_text.get_height()))
        self.screen.blit(self.return_text, (self.width // 2 - self.return_text.get_width() // 2,
                                            self.text_rect.midbottom[1] + self.resume_text.get_height() * 3))
        self.screen.blit(self.quit_text, (self.width // 2 - self.quit_text.get_width() // 2,
                                            self.height - self.quit_text.get_height() * 2))
