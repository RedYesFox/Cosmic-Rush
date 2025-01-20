import pygame
from Settings import PAUSE_FONT1, PAUSE_FONT2, toggle_on_img, toggle_off_img, music_channel1, music_channel2
import Settings


class SettingsMenu:
    def __init__(self, screen, size):
        self.screen = screen
        self.width, self.height = self.size = size
        self.slider_rect = pygame.Rect(self.width // 2 - 200, self.height // 2, 200, 20)  # Положение и размер ползунка
        self.handle_rect = pygame.Rect(0, 0, 20, 20)
        self.handle_rect.center = self.slider_rect.centerx - 80, self.slider_rect.centery
        self.toggle_btn_x = self.width // 2 - toggle_on_img.get_width() * 2
        self.toggle_btn_y = self.height // 2 + 50
        self.menu_text = PAUSE_FONT1.render("Настройки", True, (200, 200, 200))
        self.volume_text = PAUSE_FONT2.render("Громкость музыки", True, (200, 200, 200))
        self.blast_text = PAUSE_FONT2.render("Вкл/вкл звук нажатия", True, (200, 200, 200))
        self.fullscreen_text = PAUSE_FONT2.render("В разработке **** Оконный/полноэкранный режим", True,
                                                  (200, 200, 200))

        bg_color = (0, 0, 0, 230)
        self.surface = pygame.Surface((self.width // 1.5, self.height // 1.5), pygame.SRCALPHA)
        self.surface.fill(bg_color)

    def update_volume(self, x):
        volume = x / self.slider_rect.width  # Нормализуем значение от 0 до 1
        music_channel1.set_volume(volume)
        music_channel2.set_volume(volume)

    def draw_settings_menu(self):
        self.screen.blit(self.surface,
                         ((self.width - self.surface.get_width()) // 2, (self.height - self.surface.get_height()) // 2))
        self.screen.blit(self.menu_text, (self.width // 2 - self.menu_text.get_width() // 2, self.height // 2 - 70))
        self.screen.blit(self.volume_text, (self.width // 2 + self.volume_text.get_width() // 4, self.height // 2))
        self.screen.blit(self.blast_text, (self.width // 2 + self.blast_text.get_width() // 5, self.height // 2 + 70))
        self.screen.blit(self.fullscreen_text,
                         (self.width // 2 - self.fullscreen_text.get_width() // 3, self.height // 2 + 140))

        if Settings.blaster_sound:
            self.screen.blit(toggle_on_img, (self.toggle_btn_x, self.toggle_btn_y))
        else:
            self.screen.blit(toggle_off_img, (self.toggle_btn_x, self.toggle_btn_y))

    def toggle_button(self):
        return toggle_on_img.get_rect(topleft=(self.toggle_btn_x, self.toggle_btn_y))
