import pygame
from Settings import START_FONT, START_BG_IMAGE, settings_icon


class StartMenu:
    def __init__(self, screen, size):
        self.screen = screen
        self.width, self.height = self.size = size
        self.start_game_text = START_FONT.render("Начать игру", True, (255, 255, 255))
        self.game_title_text = START_FONT.render("Cosmic Rush", True, (255, 255, 255))
        bg_color = (0, 0, 0, 160)
        surface = pygame.Surface((self.width * 3, self.height), pygame.SRCALPHA)
        surface.fill(bg_color)
        self.surface = pygame.transform.rotate(surface, -25)
        self.button_start_x = self.width // 12
        self.button_start_y = self.height - 300
        self.button_settings_x = self.width - 70
        self.button_settings_y = 20

    def draw_start_menu(self):
        self.screen.blit(START_BG_IMAGE, (0, 0))
        self.screen.blit(self.game_title_text, (self.width // 2 - self.game_title_text.get_width() // 2, 100))
        self.screen.blit(self.surface, (-350, 200))
        self.screen.blit(self.start_game_text, (self.button_start_x, self.button_start_y))
        self.screen.blit(settings_icon, (self.button_settings_x, self.button_settings_y))

    def start_game_button(self):
        return self.start_game_text.get_rect(topleft=(self.button_start_x, self.button_start_y))

    def settings_button(self):
        return settings_icon.get_rect(topleft=(self.button_settings_x, self.button_settings_y))
