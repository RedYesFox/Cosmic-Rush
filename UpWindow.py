import pygame
from Settings import PAUSE_FONT2, START_FONT1


class UpWindow:
    def __init__(self, screen, size):
        self.screen = screen
        self.width, self.height = self.size = size
        bg_color = (0, 0, 0, 230)
        self.surface = pygame.Surface((self.width // 1.5, self.height // 1.5), pygame.SRCALPHA)
        self.surface.fill(bg_color)
        self.main_text = START_FONT1.render("Вперёд!", True, (200, 180, 150))
        self.tip1_text = PAUSE_FONT2.render("ЛКМ - Огонь", True, (200, 200, 200))
        self.tip2_text = PAUSE_FONT2.render("Пробел - Энергетическая броня", True, (180, 180, 180))
        self.tip3_text = PAUSE_FONT2.render("ESC - Пауза", True, (180, 180, 180))

        self.y = self.height
        self.up = 6
        self.opened = False
        self.surface_w, self.surface_h = self.surface.get_width() // 2, self.surface.get_height() // 2

    def draw_up_window(self):
        self.screen.blit(self.surface,
                         ((self.width - self.surface.get_width()) // 2, self.y))

        self.surface.blit(self.main_text, (self.surface_w - self.main_text.get_width() // 2, self.surface_h - 80))
        self.surface.blit(self.tip1_text, (self.surface_w - self.tip1_text.get_width() // 2, self.surface_h))
        self.surface.blit(self.tip2_text, (self.surface_w - self.tip2_text.get_width() // 2, self.surface_h + 70))
        self.surface.blit(self.tip3_text, (self.surface_w - self.tip3_text.get_width() // 2, self.surface_h + 140))

    def update(self):
        if self.y < (self.height - self.surface.get_height()) // 2:
            self.opened = True

        if not self.opened:
            self.y -= self.up
