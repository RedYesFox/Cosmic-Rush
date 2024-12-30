import pygame


class PauseMenu:
    def draw_pause_menu(screen, size):
        width, height = size
        menu_font = pygame.font.Font(None, 36)
        menu_text = menu_font.render("ПАУЗА", True, (255, 255, 255))
        resume_text = menu_font.render("Нажмите ESC для продолжения", True, (255, 255, 255))
        quit_text = menu_font.render("Нажмите E для выхода", True, (255, 255, 255))
        red_color = (36, 27, 74, 160)
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        surface.fill(red_color)
        screen.blit(surface, (0, 0))
        screen.blit(menu_text, (width // 2 - menu_text.get_width() // 2, height // 2 - 50))
        screen.blit(resume_text, (width // 2 - resume_text.get_width() // 2, height // 2))
        screen.blit(quit_text, (width // 2 - quit_text.get_width() // 2, height // 2 + 50))
