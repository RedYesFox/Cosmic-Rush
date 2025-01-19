import pygame
from pygame import FULLSCREEN

from Enemies import Enemy
from EscapeMenu import EscapeMenu
from Hero import Hero
from Bullet import Bullet
import Settings
from Settings import MAIN_BG_IMAGE, cursor1, cursor2, FPS, WINDOW_SIZE, WINDOW_HEIGHT, WINDOW_WIDTH, click_effect, \
    shot_effect, button_focused, music_channel2, music_channel1, game_music, wait_music, start_btn_effect, VOLUME
from SettingsMenu import SettingsMenu
from PauseMenu import PauseMenu
from StartMenu import StartMenu

focus = False
last_focused_button = None


def handle_button_focus(button, pos):
    global focus, last_focused_button

    if button.collidepoint(pos):
        if not focus and button != last_focused_button:
            button_focused.play()
            focus = True
            last_focused_button = button
    else:
        if button == last_focused_button:
            focus = False
            last_focused_button = None


def main():
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Cosmic Rush")
    pygame.mouse.set_pos(WINDOW_WIDTH // 2 - 90, WINDOW_HEIGHT // 2)
    pygame.mouse.set_cursor(cursor1)

    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = Hero(screen, WINDOW_SIZE)
    enemy = Enemy(WINDOW_SIZE)

    pause_menu = PauseMenu(screen, WINDOW_SIZE)
    start_menu = StartMenu(screen, WINDOW_SIZE)
    escape_menu = EscapeMenu(screen, WINDOW_SIZE)
    settings_menu = SettingsMenu(screen, WINDOW_SIZE)

    all_sprites.add(player)
    enemies.add(enemy)

    clock = pygame.time.Clock()
    running = True
    paused = False
    start_menu_opened = True
    settings_menu_opened = False
    spawn_delay = 30
    spawn_timer = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if settings_menu_opened:
                    settings_menu_opened = False
                paused = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused

                if event.key == pygame.K_e:
                    if paused:
                        Settings.save_result(Settings.score)
                        running = False
            if event.type == pygame.MOUSEMOTION:
                if settings_menu_opened:
                    if event.buttons[0]:
                        if settings_menu.slider_rect.collidepoint(event.pos):
                            settings_menu.handle_rect.centerx = event.pos[0]
                            settings_menu.update_volume(
                                settings_menu.handle_rect.centerx - settings_menu.slider_rect.left)

                if paused == False and start_menu_opened == False:
                    player.move(event.pos[0])

                if not paused and not start_menu_opened:
                    player.move(event.pos[0])

                if settings_menu_opened:
                    handle_button_focus(settings_menu.toggle_button(), event.pos)

                if paused:
                    handle_button_focus(pause_menu.settings_button(), event.pos)
                    handle_button_focus(escape_menu.cancel_button(), event.pos)

                if start_menu_opened:
                    handle_button_focus(start_menu.start_game_button(), event.pos)
                    handle_button_focus(start_menu.settings_button(), event.pos)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Settings.blaster_sound and (start_menu_opened or settings_menu_opened or paused):
                    click_effect.play()

                if settings_menu_opened:
                    if settings_menu.toggle_button().collidepoint(pygame.mouse.get_pos()):
                        Settings.blaster_sound = not Settings.blaster_sound

                if paused:
                    if pause_menu.settings_button().collidepoint(pygame.mouse.get_pos()):
                        settings_menu_opened = not settings_menu_opened
                    if escape_menu.cancel_button().collidepoint(pygame.mouse.get_pos()):
                        paused = not paused

                if start_menu_opened:
                    if start_menu.start_game_button().collidepoint(pygame.mouse.get_pos()):
                        start_btn_effect.play()
                        start_menu_opened = False
                        paused = False
                    if start_menu.settings_button().collidepoint(pygame.mouse.get_pos()):
                        settings_menu_opened = not settings_menu_opened

        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            if not any([start_menu_opened, settings_menu_opened, paused]):
                if spawn_timer >= spawn_delay:
                    shot_effect.play()
                    bullet = Bullet(screen, WINDOW_SIZE, player.shot())
                    all_sprites.add(bullet)
                    bullets.add(bullet)
                    spawn_timer = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_g]:
            enemies.add(Enemy(WINDOW_SIZE))

        if settings_menu.handle_rect.centerx < settings_menu.slider_rect.left:
            settings_menu.handle_rect.centerx = settings_menu.slider_rect.left
        elif settings_menu.handle_rect.centerx > settings_menu.slider_rect.right:
            settings_menu.handle_rect.centerx = settings_menu.slider_rect.right

        if not paused and not start_menu_opened:
            if music_channel1.get_busy():
                music_channel1.pause()
                if not music_channel2.get_busy():
                    music_channel2.play(game_music, loops=-1)
                    music_channel2.set_volume(VOLUME)
                else:
                    music_channel2.unpause()


            settings_menu_opened = False
            pygame.mouse.set_visible(False)
            for bullet in bullets:
                enemy_hit = pygame.sprite.spritecollide(bullet, enemies, True)
                if enemy_hit:
                    bullet.kill()
                    Settings.score += 10
                    print(Settings.score)
            all_sprites.update()
            enemies.update()
        screen.blit(MAIN_BG_IMAGE, (0, 0))
        all_sprites.draw(screen)
        enemies.draw(screen)

        if paused and not start_menu_opened:
            if music_channel2.get_busy():
                music_channel2.pause()
                if not music_channel1.get_busy():
                    music_channel1.play(wait_music, loops=-1)
                else:
                    music_channel1.unpause()


            pygame.mouse.set_cursor(cursor1)
            pygame.mouse.set_visible(True)
            pause_menu.draw_pause_menu()

        if start_menu_opened:
            start_menu.draw_start_menu()
            rect1 = pygame.rect.Rect(*pygame.mouse.get_pos(), 40, 40)
            if start_menu.start_game_button().colliderect(rect1):
                handle_button_focus(start_menu.start_game_button(), pygame.mouse.get_pos())
                handle_button_focus(start_menu.settings_button(), pygame.mouse.get_pos())
                pygame.mouse.set_cursor(cursor2)
            else:
                pygame.mouse.set_cursor(cursor1)

        if paused and start_menu_opened and not settings_menu_opened:
            escape_menu.draw_escape_menu()
        if paused and start_menu_opened and settings_menu_opened:
            settings_menu_opened = False
            paused = False

        if settings_menu_opened:
            settings_menu.draw_settings_menu()
            pygame.draw.rect(screen, (50, 50, 50), settings_menu.slider_rect)
            pygame.draw.rect(screen, (255, 255, 255), settings_menu.handle_rect)

        spawn_timer += 1
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    main()
