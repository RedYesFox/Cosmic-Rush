import pygame
from Settings import START_FONT1, START_BG_IMAGE, settings_icon, START_FONT2


class StartMenu:
    def __init__(self, screen, size):
        self.screen = screen
        self.width, self.height = self.size = size
        self.start_game_text = START_FONT1.render("Начать игру", True, (255, 255, 255))
        self.game_title_text = START_FONT1.render("Cosmic Rush", True, (255, 255, 255))
        self.info_text = START_FONT2.render("Лучший результат:", True, (48, 7, 74))
        bg_color = (0, 0, 0, 160)
        surface = pygame.Surface((self.width * 3, self.height), pygame.SRCALPHA)
        surface.fill(bg_color)
        self.surface = pygame.transform.rotate(surface, -25)
        self.button_start_x = self.width // 12
        self.button_start_y = self.height - 300
        self.button_settings_x = self.width - 70
        self.button_settings_y = 20
        self.rect = self.info_text.get_rect()
        self.rect = self.rect.move(self.width - self.info_text.get_width() - 20, self.height // 2)

    def draw_start_menu(self, BEST_SCORE, BEST_LVL):
        self.screen.blit(START_BG_IMAGE, (0, 0))
        self.screen.blit(self.game_title_text, (self.width // 2 - self.game_title_text.get_width() // 2, 100))
        self.screen.blit(self.surface, (-350, 200))
        self.screen.blit(self.start_game_text, (self.button_start_x, self.button_start_y))
        self.screen.blit(settings_icon, (self.button_settings_x, self.button_settings_y))
        self.screen.blit(self.info_text, self.rect.topleft)
        best_score_text = START_FONT2.render(f"Очки - {BEST_SCORE}", True, (48, 7, 74))
        best_lvl_text = START_FONT2.render(f"Лвл - {BEST_LVL}", True, (48, 7, 74))
        self.screen.blit(best_score_text, (self.rect.centerx - best_score_text.get_width() // 2, self.height // 2 + 50))
        self.screen.blit(best_lvl_text, (self.rect.centerx - best_lvl_text.get_width() // 2, self.height // 2 + 100))

    def start_game_button(self):
        return self.start_game_text.get_rect(topleft=(self.button_start_x, self.button_start_y))

    def settings_button(self):
        return settings_icon.get_rect(topleft=(self.button_settings_x, self.button_settings_y))
