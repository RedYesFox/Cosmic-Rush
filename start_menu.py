import pygame


class StartMenu:
    def __init__(self, screen, size):
        self.screen = screen
        self.size = size

    def draw_start_menu(self):
        width, height = self.size
        menu_font = pygame.font.Font("fonts/Sixtyfour-Regular-VariableFont_BLED,SCAN.ttf", 45)
        menu_text = menu_font.render("Cosmic Rush", True, (255, 255, 255))
        bg_color = (0, 0, 0, 255)
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        surface.fill(bg_color)
        bg_img = pygame.image.load('images/StartBg.png')
        self.screen.blit(bg_img, (0, 0))
        self.screen.blit(menu_text, (width // 2 - menu_text.get_width() // 2, 100))
