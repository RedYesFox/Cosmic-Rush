import pygame

from Enemies import Enemy
from EscapeMenu import EscapeMenu
from Hero import Hero
from Bullet import Bullet
import Settings
from Settings import MAIN_BG_IMAGE, cursor1, cursor2, FPS, WINDOW_SIZE, WINDOW_HEIGHT, WINDOW_WIDTH, click_effect, \
    shot_effect
from SettingsMenu import SettingsMenu
from pause import PauseMenu
from start_menu import StartMenu


def main():

    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Cosmic Rush")
    pygame.mouse.set_pos(WINDOW_WIDTH // 2 - 90, WINDOW_HEIGHT // 2)
    pygame.mouse.set_cursor(cursor1)

    all_sprites = pygame.sprite.Group()
    player = Hero(screen, WINDOW_SIZE)
    enemy = Enemy(WINDOW_SIZE)

    pause_menu = PauseMenu(screen, WINDOW_SIZE)
    start_menu = StartMenu(screen, WINDOW_SIZE)
    escape_menu = EscapeMenu(screen, WINDOW_SIZE)
    settings_menu = SettingsMenu(screen, WINDOW_SIZE)

    all_sprites.add(player)
    all_sprites.add(enemy)

    clock = pygame.time.Clock()
    running = True
    paused = False
    start_menu_opened = True
    settings_menu_opened = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused
                    if settings_menu_opened:
                        settings_menu_opened = False
                if event.key == pygame.K_e:
                    running = False
            if event.type == pygame.MOUSEMOTION:
                if settings_menu_opened:
                    if event.buttons[0]:
                        if settings_menu.slider_rect.collidepoint(event.pos):
                            settings_menu.handle_rect.centerx = event.pos[0]
                            settings_menu.update_volume(settings_menu.handle_rect.centerx - settings_menu.slider_rect.left)
                if paused == False and start_menu_opened == False:
                    player.move(event.pos[0])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Settings.blaster_sound and (start_menu_opened or settings_menu_opened or paused):
                    click_effect.play()
                if not any([start_menu_opened, settings_menu_opened, paused]):
                    shot_effect.play()
                    all_sprites.add(Bullet(screen, WINDOW_SIZE, player.shot()))
                if settings_menu_opened:
                    if settings_menu.handle_rect.collidepoint(event.pos):
                        settings_menu.handle_rect.centerx = event.pos[0]
                        settings_menu.update_volume(settings_menu.handle_rect.centerx - settings_menu.slider_rect.left)
                    if settings_menu.toggle_button().collidepoint(pygame.mouse.get_pos()):
                        Settings.blaster_sound = not Settings.blaster_sound

                if paused:
                    if pause_menu.settings_button().collidepoint(pygame.mouse.get_pos()):
                        settings_menu_opened = not settings_menu_opened

                if start_menu_opened:
                    if start_menu.start_game_button().collidepoint(pygame.mouse.get_pos()):
                        start_menu_opened = False
                        paused = False
                    if start_menu.settings_button().collidepoint(pygame.mouse.get_pos()):
                        settings_menu_opened = not settings_menu_opened

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_g]:
        #     # all_sprites.add(Enemy(WINDOW_SIZE))
        #     print(pygame.sprite.col)

        if settings_menu.handle_rect.centerx < settings_menu.slider_rect.left:
            settings_menu.handle_rect.centerx = settings_menu.slider_rect.left
        elif settings_menu.handle_rect.centerx > settings_menu.slider_rect.right:
            settings_menu.handle_rect.centerx = settings_menu.slider_rect.right

        if not paused and not start_menu_opened:
            settings_menu_opened = False
            pygame.mouse.set_visible(False)
            all_sprites.update()
        screen.blit(MAIN_BG_IMAGE, (0, 0))
        all_sprites.draw(screen)

        if paused and not start_menu_opened:
            pygame.mouse.set_cursor(cursor1)
            pygame.mouse.set_visible(True)
            pause_menu.draw_pause_menu()

        if start_menu_opened:
            start_menu.draw_start_menu()
            rect1 = pygame.rect.Rect(*pygame.mouse.get_pos(), 40, 40)
            if start_menu.start_game_button().colliderect(rect1):
                pygame.mouse.set_cursor(cursor2)
            else:
                pygame.mouse.set_cursor(cursor1)

        if paused and start_menu_opened and not settings_menu_opened:
            pygame.mouse.set_cursor(cursor1)
            pygame.mouse.set_visible(True)
            escape_menu.draw_escape_menu()

        if settings_menu_opened:
            settings_menu.draw_settings_menu()
            pygame.draw.rect(screen, (50, 50, 50), settings_menu.slider_rect)
            pygame.draw.rect(screen, (255, 255, 255), settings_menu.handle_rect)

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    main()
