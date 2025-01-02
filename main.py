import pygame
from Hero import Hero
from Enemies import Enemy
from Settings import MAIN_BG_IMAGE, cursor1, cursor2, point, settings_icon
from pause import PauseMenu
from start_menu import StartMenu
from EscapeMenu import EscapeMenu
from SettingsMenu import SettingsMenu


def main():

    device_width, device_height = pygame.display.get_desktop_sizes()[0]
    size = width, height = device_width - 400, device_height - 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Cosmic Rush")
    pygame.mouse.set_pos(width // 2 - 90, height // 2)
    pygame.mouse.set_cursor(cursor1)

    all_sprites = pygame.sprite.Group()
    player = Hero(size)
    enemy = Enemy(size)

    pause_menu = PauseMenu(screen, size)
    start_menu = StartMenu(screen, size)
    escape_menu = EscapeMenu(screen, size)
    settings_menu = SettingsMenu(screen, size)

    all_sprites.add(player)
    all_sprites.add(enemy)

    clock = pygame.time.Clock()
    running = True
    paused = False
    start_menu_opened = True
    settings_menu_opened = False

    pygame.mixer.music.load('sounds/wait_music.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(50)
    sound_effect = pygame.mixer.Sound('sounds/laser-gun-beam-blaster-shot_fjfjpfvu.mp3')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused
                if event.key == pygame.K_e:
                    running = False
            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0]:  # Если левая кнопка мыши нажата
                    if settings_menu.slider_rect.collidepoint(event.pos):
                        settings_menu.handle_rect.centerx = event.pos[0]
                        settings_menu.update_volume(settings_menu.handle_rect.centerx - settings_menu.slider_rect.left)
                if paused == False and start_menu_opened == False:
                    player.move(event.pos[0])
            if event.type == pygame.MOUSEBUTTONDOWN:
                sound_effect.play()
                # if settings_menu.handle_rect.collidepoint(event.pos):
                #     settings_menu.handle_rect.centerx = event.pos[0]
                #     settings_menu.update_volume(settings_menu.handle_rect.centerx - settings_menu.slider_rect.left)

                if start_menu.start_game_button().collidepoint(pygame.mouse.get_pos()):
                    start_menu_opened = False
                    paused = False
                if start_menu.settings_button().collidepoint(pygame.mouse.get_pos()):
                    settings_menu_opened = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_g]:
            all_sprites.add(Enemy(size))

        if settings_menu.handle_rect.centerx < settings_menu.slider_rect.left:
            settings_menu.handle_rect.centerx = settings_menu.slider_rect.left
        elif settings_menu.handle_rect.centerx > settings_menu.slider_rect.right:
            settings_menu.handle_rect.centerx = settings_menu.slider_rect.right

        if not paused and not start_menu_opened:
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

        if paused and start_menu_opened:
            pygame.mouse.set_cursor(cursor1)
            pygame.mouse.set_visible(True)
            escape_menu.draw_escape_menu()

        if settings_menu_opened:
            settings_menu.draw_settings_menu()
            pygame.draw.rect(screen, (50, 50, 50), settings_menu.slider_rect)
            pygame.draw.rect(screen, (255, 255, 255), settings_menu.handle_rect)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    main()
