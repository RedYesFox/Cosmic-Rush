import pygame
from Settings import PAUSE_FONT1, PAUSE_FONT2


class EscapeMenu:
    def __init__(self, screen, size):
        self.screen = screen
        self.width, self.height = self.size = size

    def draw_escape_menu(self):
        menu_text = PAUSE_FONT1.render("Выйти из игры?", True, (180, 180, 180))
        quit_text = PAUSE_FONT2.render("Нажмите E для выхода", True, (180, 180, 180))
        resume_text = PAUSE_FONT2.render("Нажмите ESC для продолжения", True, (180, 180, 180))
        img_1 = pygame.image.load('icons/resume.png').convert_alpha()
        img_1 = pygame.transform.scale(img_1, (resume_text.get_height(), resume_text.get_height()))
        img_2 = pygame.image.load('icons/logout.png')
        img_2 = pygame.transform.scale(img_2, (quit_text.get_height(), quit_text.get_height()))

        bg_color = (0, 0, 0, 230)
        surface = pygame.Surface((self.width // 1.5, self.height // 1.5), pygame.SRCALPHA)
        surface.fill(bg_color)
        self.screen.blit(surface, ((self.width - surface.get_width()) // 2, (self.height - surface.get_height()) // 2))

        self.screen.blit(menu_text, (self.width // 2 - menu_text.get_width() // 2, self.height // 2 - 70))
        self.screen.blit(resume_text, (self.width // 2 - resume_text.get_width() // 2, self.height // 2))
        self.screen.blit(quit_text, (self.width // 2 - quit_text.get_width() // 2, self.height // 2 + 70))
        self.screen.blit(img_1, (
            self.width // 2 - resume_text.get_width() // 2 - (img_1.get_width() + 10), self.height // 2 - 2))
        self.screen.blit(img_2, (
            self.width // 2 - quit_text.get_width() // 2 - (img_2.get_width() + 10), self.height // 2 + 70))

