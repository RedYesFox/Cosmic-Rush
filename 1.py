import pygame
from Hero import Hero
from Enemies import Enemy

if __name__ == '__main__':
    pygame.init()

    BACKGROUND_IMG = pygame.image.load('images/background.png')
    device_width, device_height = pygame.display.get_desktop_sizes()[0]
    size = width, height = device_width - 400, device_height - 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Cosmic Rush")
    pygame.mouse.set_visible(False)
    pygame.mouse.set_pos(width // 2 - 90, height // 2)

    all_sprites = pygame.sprite.Group()
    player = Hero(size)
    enemy = Enemy(size)

    all_sprites.add(player)
    all_sprites.add(enemy)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                player.move(event.pos[0])

        # if enemy.can:
        #     enemy.move()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.display.toggle_fullscreen()
        if keys[pygame.K_g]:
            all_sprites.add(Enemy(size))

        all_sprites.update()
        screen.blit(BACKGROUND_IMG, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
