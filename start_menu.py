import pygame


class StartMenu:
    def __init__(self, screen, size):
        self.screen = screen
        self.width, self.height = self.size = size

    def draw_start_menu(self):
        menu_font = pygame.font.Font("fonts/Sixtyfour-Regular-VariableFont_BLED,SCAN.ttf", 45)
        menu_text = menu_font.render("Cosmic Rush", True, (255, 255, 255))
        bg_img = pygame.image.load('images/StartBg.png')
        self.screen.blit(bg_img, (0, 0))
        self.screen.blit(menu_text, (self.width // 2 - menu_text.get_width() // 2, 100))

        bg_color = (0, 0, 0, 160)
        surface = pygame.Surface((self.width * 3, self.height), pygame.SRCALPHA)
        surface.fill(bg_color)
        surface = pygame.transform.rotate(surface, -25)
        self.screen.blit(surface, (-350, 200))


        start_game_font = pygame.font.Font("fonts/KellySlab-Regular.ttf", 50)
        self.start_game_text = start_game_font.render("Начать игру", True, (255, 255, 255))
        self.button_x = self.width // 4 - self.start_game_text.get_width()
        self.button_y = self.height - 300
        self.screen.blit(self.start_game_text, (self.button_x, self.button_y))

    def start_game_button(self):
        return self.start_game_text.get_rect(topleft=(self.button_x, self.button_y))