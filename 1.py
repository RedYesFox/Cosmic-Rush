import time

import pygame
from Hero import Hero
from Enemies import Enemy
from pause import PauseMenu
from start_menu import StartMenu

if __name__ == '__main__':
    pygame.init()

    BACKGROUND_IMG = pygame.image.load('images/background.png')
    device_width, device_height = pygame.display.get_desktop_sizes()[0]
    size = width, height = device_width - 400, device_height - 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Cosmic Rush")
    pygame.mouse.set_pos(width // 2 - 90, height // 2)

    all_sprites = pygame.sprite.Group()
    player = Hero(size)
    enemy = Enemy(size)

    pause_menu = PauseMenu(screen, size)
    start_menu = StartMenu(screen, size)

    cursor1_img = pygame.image.load('icons/rocket_white.png').convert_alpha()
    cursor1_img = pygame.transform.rotate(cursor1_img, 90)
    cursor1_img = pygame.transform.scale(cursor1_img, (40, 40))
    cursor1 = pygame.cursors.Cursor((0, 0), cursor1_img)
    pygame.mouse.set_cursor(cursor1)

    cursor2_img = pygame.image.load('icons/rocket_fiolet.png').convert_alpha()
    cursor2_img = pygame.transform.rotate(cursor2_img, 45)
    cursor2_img = pygame.transform.scale(cursor2_img, (50, 50))
    cursor2 = pygame.cursors.Cursor((0, 0), cursor2_img)

    all_sprites.add(player)
    all_sprites.add(enemy)

    clock = pygame.time.Clock()
    running = True
    paused = False
    start_menu_opened = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and start_menu_opened == False:
                    paused = not paused
                if event.key == pygame.K_e:
                    running = False
            if event.type == pygame.MOUSEMOTION and paused == False and start_menu_opened == False:
                player.move(event.pos[0])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_menu.start_game_button().collidepoint(pygame.mouse.get_pos()):
                    start_menu_opened = False
                    paused = False
                    pygame.mouse.set_visible(True)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_g]:
            all_sprites.add(Enemy(size))

        if not paused and not start_menu_opened:
            pygame.mouse.set_visible(False)
            all_sprites.update()
        screen.blit(BACKGROUND_IMG, (0, 0))
        all_sprites.draw(screen)

        if paused and not start_menu_opened:
            pygame.mouse.set_visible(True)
            pause_menu.draw_pause_menu()

        if start_menu_opened:
            start_menu.draw_start_menu()
            if start_menu.start_game_button().collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(cursor2)
            else:
                pygame.mouse.set_cursor(cursor1)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
