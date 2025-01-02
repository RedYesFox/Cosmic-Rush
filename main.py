import pygame
from Hero import Hero
from Enemies import Enemy
from Settings import MAIN_BG_IMAGE, cursor1, cursor2
from pause import PauseMenu
from start_menu import StartMenu


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
            if event.type == pygame.MOUSEMOTION:
                if paused == False and start_menu_opened == False:
                    player.move(event.pos[0])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_menu.start_game_button().collidepoint(pygame.mouse.get_pos()):
                    start_menu_opened = False
                    paused = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_g]:
            all_sprites.add(Enemy(size))

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

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    main()
