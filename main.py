import pygame
from plyer import notification

from Enemies import Enemy
from Hero import Hero
from Bullet import Bullet
from Explosion import Explosion

import Settings
from Settings import MAIN_BG_IMAGE, cursor1, cursor2, WINDOW_SIZE, WINDOW_HEIGHT, WINDOW_WIDTH, click_effect, \
    shot_effect, button_focused, music_channel2, music_channel1, game_music, wait_music, start_btn_effect, VOLUME, \
    read_results, lose_effect

from SettingsMenu import SettingsMenu
from PauseMenu import PauseMenu
from StartMenu import StartMenu
from GameOverWindow import GameOverWindow
from UpWindow import UpWindow
from EscapeMenu import EscapeMenu
from GameHud import Heart, Shield, Text, ArmorShield

focus = False
last_focused_button = None


def spawn_enemies(num_enemies):  # Появление врагов группами
    new_enemies = pygame.sprite.Group()
    for _ in range(num_enemies):
        new_enemies.add(Enemy(WINDOW_SIZE, screen))
    return new_enemies


def handle_button_focus(button, pos):  # Звук при фокусе кнопки
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


def push_notice(LVL):  # Уведомлении о ЛВЛе
    notification.notify(
        title=" 🔔Cosmic Rush",
        message=f"Новый Уровень❗\n        LVL: {LVL}",
        timeout=5
    )


def main():
    pygame.display.set_caption("Cosmic Rush")
    pygame.mouse.set_pos(WINDOW_WIDTH // 2 - 90, WINDOW_HEIGHT // 2)
    pygame.mouse.set_cursor(cursor1)

    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    enemy_bullets = pygame.sprite.Group()

    player = Hero(screen, WINDOW_SIZE)
    pause_menu = PauseMenu(screen, WINDOW_SIZE)
    start_menu = StartMenu(screen, WINDOW_SIZE)
    escape_menu = EscapeMenu(screen, WINDOW_SIZE)
    settings_menu = SettingsMenu(screen, WINDOW_SIZE)
    up_window = UpWindow(screen, WINDOW_SIZE)
    heart = Heart(screen, WINDOW_SIZE)
    shield = Shield(screen, WINDOW_SIZE)
    texts = Text(screen, WINDOW_SIZE)
    armor_shield = None

    all_sprites.add(heart, shield, player)

    clock = pygame.time.Clock()
    running = True
    paused = False
    start_menu_opened = True
    settings_menu_opened = False

    shield_activated = False
    shield_recovery = 35
    shield_delay = 5
    shield_timer = 0

    spawn_delay = 30
    spawn_timer = 0

    wave_delay = 240
    wave_timer = 0
    enemies_per_wave = 3
    total_enemies_to_spawn = 0
    level_started = False

    game_over_window = GameOverWindow(screen, WINDOW_SIZE)
    game_over = False

    up_window_opened = False
    up_window_timer = 0
    up_window_delay = 90

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if settings_menu_opened:
                    settings_menu_opened = False
                paused = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if game_over:
                        start_menu_opened = True
                        settings_menu_opened = False
                        paused = False
                        game_over = False
                        if music_channel2.get_busy():
                            music_channel2.pause()
                            if not music_channel1.get_busy():
                                music_channel1.play(wait_music, loops=-1)
                            else:
                                music_channel1.unpause()

                        pygame.mouse.set_cursor(cursor1)
                        pygame.mouse.set_visible(True)
                    else:
                        paused = not paused

                if event.key == pygame.K_r and game_over:
                    game_over = False
                    paused = False
                    player.reset()
                    enemies.empty()
                    bullets.empty()
                    enemy_bullets.empty()
                    all_sprites.empty()
                    all_sprites.add(heart, shield, player)
                    Settings.SCORE = 0
                    Settings.LVL = 1
                    total_enemies_to_spawn = round(Settings.LVL * 2.5)
                    level_started = False
                    music_channel2.stop()

                if event.key == pygame.K_e:
                    if paused or game_over:
                        Settings.save_result()
                        running = False
                if event.key == pygame.K_SPACE:
                    if not any([start_menu_opened, settings_menu_opened, paused, game_over]):
                        if Settings.SHIELD == 100:
                            shield_activated = True
                            armor_shield = ArmorShield(WINDOW_SIZE, player.rect.center)
                            all_sprites.add(armor_shield)

            if event.type == pygame.MOUSEMOTION:
                if settings_menu_opened:
                    if event.buttons[0]:
                        if settings_menu.slider_rect.collidepoint(event.pos):
                            settings_menu.handle_rect.centerx = event.pos[0]
                            settings_menu.update_volume(
                                settings_menu.handle_rect.centerx - settings_menu.slider_rect.left)

                if not paused and not start_menu_opened and not game_over:
                    player.rect.centerx = event.pos[0]
                    player.move(event.pos[0])
                    if shield_activated:
                        armor_shield.move(event.pos[0])

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
                        up_window_opened = True
                        up_window.draw_up_window()
                    if start_menu.settings_button().collidepoint(pygame.mouse.get_pos()):
                        settings_menu_opened = not settings_menu_opened

        mouse_buttons = pygame.mouse.get_pressed()
        if not any([start_menu_opened, settings_menu_opened, paused, game_over]):
            if mouse_buttons[0]:
                if spawn_timer >= spawn_delay:
                    shot_effect.play()
                    bullet = Bullet(screen, WINDOW_SIZE, player.shot())
                    all_sprites.add(bullet)
                    bullets.add(bullet)
                    spawn_timer = 0

        if settings_menu.handle_rect.centerx < settings_menu.slider_rect.left:
            settings_menu.handle_rect.centerx = settings_menu.slider_rect.left
        elif settings_menu.handle_rect.centerx > settings_menu.slider_rect.right:
            settings_menu.handle_rect.centerx = settings_menu.slider_rect.right

        if not paused and not start_menu_opened and not game_over:

            if music_channel1.get_busy():
                music_channel1.pause()
                if not music_channel2.get_busy():
                    music_channel2.play(game_music, loops=-1)
                    music_channel2.set_volume(VOLUME)
                else:
                    music_channel2.unpause()
            settings_menu_opened = False
            pygame.mouse.set_visible(False)

            if not level_started:
                level_started = True
                total_enemies_to_spawn = round(Settings.LVL * 2.5)

            if len(enemies) == 0 and total_enemies_to_spawn == 0:
                Settings.LVL += 1
                level_started = False
                push_notice(Settings.LVL)

            if total_enemies_to_spawn > 0 and wave_timer >= wave_delay:
                num_to_spawn = min(enemies_per_wave, total_enemies_to_spawn)
                new_enemies = spawn_enemies(num_to_spawn)
                enemies.add(new_enemies)
                total_enemies_to_spawn -= num_to_spawn
                wave_timer = 0

            for bullet in bullets:
                enemy_hit = pygame.sprite.spritecollide(bullet, enemies, False)
                for enemy in enemy_hit:
                    if pygame.sprite.collide_mask(bullet, enemy):
                        all_sprites.add(Explosion(enemy.killed()))
                        bullet.kill()
                        Settings.SCORE += 10

            for enemy in enemies:
                enemy_bullet = enemy.shoot()
                if enemy_bullet:
                    enemy_bullets.add(enemy_bullet)
                    all_sprites.add(enemy_bullet)

            if shield_activated:
                if Settings.SHIELD > 0:
                    shield_timer += 1
                    if shield_timer == shield_delay:
                        Settings.SHIELD -= 1
                        shield_timer = 0

                else:
                    armor_shield.kill()
                    armor_shield = None
                    shield_activated = False
                    shield_timer = 0
            else:
                if Settings.SHIELD < 100:
                    shield_timer += 1
                    if shield_timer == shield_recovery:
                        Settings.SHIELD += 1
                        shield_timer = 0

            if pygame.sprite.spritecollide(player, enemy_bullets, True, pygame.sprite.collide_mask):
                if not shield_activated:
                    Settings.HEALTH -= 10
                if Settings.HEALTH <= 0:
                    game_over = True
                    lose_effect.play()

            all_sprites.update()
            enemies.update()
        screen.blit(MAIN_BG_IMAGE, (0, 0))
        all_sprites.draw(screen)
        enemies.draw(screen)
        enemy_bullets.draw(screen)
        texts.draw(Settings.HEALTH, Settings.SHIELD, Settings.LVL, Settings.SCORE)
        if up_window_opened:
            if up_window_timer < up_window_delay:
                up_window.draw_up_window()
                up_window.update()
            else:
                up_window_opened = False
            if up_window.opened:
                up_window_timer += 1

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
            start_menu.draw_start_menu(*read_results())
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

        if game_over and not paused:
            if music_channel2.get_busy():
                music_channel2.pause()
                if not music_channel1.get_busy():
                    music_channel1.play(wait_music, loops=-1)
                else:
                    music_channel1.unpause()
            game_over_window.draw()

        spawn_timer += 1
        wave_timer += 1
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    main()
