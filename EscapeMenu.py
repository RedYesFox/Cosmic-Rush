import pygame
from Settings import PAUSE_FONT1, PAUSE_FONT2, cancel_button_img, logout_img, resume_img


class EscapeMenu:
    def __init__(self, screen, size):
        self.screen = screen
        self.width, self.height = self.size = size
        bg_color = (0, 0, 0, 230)
        self.surface = pygame.Surface((self.width // 1.5, self.height // 1.5), pygame.SRCALPHA)
        self.surface.fill(bg_color)
        self.menu_text = PAUSE_FONT1.render("Выйти из игры?", True, (180, 180, 180))
        self.quit_text = PAUSE_FONT2.render("Нажмите E для выхода", True, (180, 180, 180))
        self.resume_text = PAUSE_FONT2.render("Нажмите ESC для продолжения", True, (180, 180, 180))
        self.cancel_btn_x, self.cancel_btn_y = (((self.width * 7 - self.surface.get_width() * 3) // 6) - 80,
                                                (self.height - self.surface.get_height()) // 2 + 40)
        print((self.cancel_btn_x, self.cancel_btn_y))

    def draw_escape_menu(self):
        self.screen.blit(self.surface,
                         ((self.width - self.surface.get_width()) // 2, (self.height - self.surface.get_height()) // 2))

        self.screen.blit(cancel_button_img, (self.cancel_btn_x, self.cancel_btn_y))
        self.screen.blit(self.menu_text, (self.width // 2 - self.menu_text.get_width() // 2, self.height // 2 - 70))
        self.screen.blit(self.resume_text, (self.width // 2 - self.resume_text.get_width() // 2, self.height // 2))
        self.screen.blit(self.quit_text, (self.width // 2 - self.quit_text.get_width() // 2, self.height // 2 + 70))
        self.screen.blit(resume_img, (
            self.width // 2 - self.resume_text.get_width() // 2 - (resume_img.get_width() + 10), self.height // 2 - 2))
        self.screen.blit(logout_img, (
            self.width // 2 - self.quit_text.get_width() // 2 - (logout_img.get_width() + 10), self.height // 2 + 70))

    def cancel_button(self):
        return cancel_button_img.get_rect(topleft=(self.cancel_btn_x, self.cancel_btn_y))
