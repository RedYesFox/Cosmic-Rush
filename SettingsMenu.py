import pygame
from Settings import PAUSE_FONT1, PAUSE_FONT2


class SettingsMenu:
    def __init__(self, screen, size):
        self.screen = screen
        self.width, self.height = self.size = size
        self.slider_rect = pygame.Rect(self.width // 2 - 200, self.height // 2, 200, 20)  # Положение и размер ползунка
        self.handle_rect = pygame.Rect(0, 0, 20, 20)
        self.handle_rect.center = self.slider_rect.center

    def update_volume(self, x):
        volume = x // 2  # Нормализуем значение от 0 до 1
        pygame.mixer.music.set_volume(volume)

    def draw_settings_menu(self):
        menu_text = PAUSE_FONT1.render("Настройки", True, (200, 200, 200))
        volume_text = PAUSE_FONT2.render("Громкость музыки", True, (200, 200, 200))

        bg_color = (0, 0, 0, 230)
        surface = pygame.Surface((self.width // 1.5, self.height // 1.5), pygame.SRCALPHA)
        surface.fill(bg_color)

        self.screen.blit(surface, ((self.width - surface.get_width()) // 2, (self.height - surface.get_height()) // 2))
        self.screen.blit(menu_text, (self.width // 2 - menu_text.get_width() // 2, self.height // 2 - 70))
        self.screen.blit(volume_text, (self.width // 2 + volume_text.get_width() // 4, self.height // 2))

