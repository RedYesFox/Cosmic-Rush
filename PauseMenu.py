import pygame
from Settings import PAUSE_FONT1, PAUSE_FONT2, settings_icon, resume_img, logout_img


class PauseMenu:
    def __init__(self, screen, size):
        self.screen = screen
        self.width, self.height = self.size = size
        self.button_settings_x, self.button_settings_y  = self.width - 70, 20
        self.menu_text = PAUSE_FONT1.render("ПАУЗА", True, (180, 180, 180))
        self.resume_text = PAUSE_FONT2.render("Нажмите ESC для продолжения", True, (180, 180, 180))
        self.quit_text = PAUSE_FONT2.render("Нажмите E для выхода", True, (180, 180, 180))
        bg_color = (0, 0, 0, 190)
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.surface.fill(bg_color)

    def draw_pause_menu(self):
        self.screen.blit(self.surface, (0, 0))
        self.screen.blit(self.menu_text, (self.width // 2 - self.menu_text.get_width() // 2, self.height // 2 - 70))
        self.screen.blit(self.resume_text, (self.width // 2 - self.resume_text.get_width() // 2, self.height // 2))
        self.screen.blit(self.quit_text, (self.width // 2 - self.quit_text.get_width() // 2, self.height // 2 + 70))
        self.screen.blit(resume_img,
                         (self.width // 2 - self.resume_text.get_width() // 2 - (resume_img.get_width() + 10), self.height // 2 - 2))
        self.screen.blit(logout_img,
                         (self.width // 2 - self.quit_text.get_width() // 2 - (logout_img.get_width() + 10), self.height // 2 + 68))


        self.screen.blit(settings_icon, (self.button_settings_x, self.button_settings_y))

    def settings_button(self):
        return settings_icon.get_rect(topleft=(self.button_settings_x, self.button_settings_y))
