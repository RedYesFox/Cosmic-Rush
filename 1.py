import pygame
from Hero import Hero

if __name__ == '__main__':
    pygame.init()

    BACKGROUND_IMG = pygame.image.load('images/background.png')
    device_width, device_height = pygame.display.get_desktop_sizes()[0]
    size = width, height = device_width - 400, device_height - 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Cosmic Rush")
    pygame.mouse.set_visible(False)

    all_sprites = pygame.sprite.Group()
    player = Hero(size)
    all_sprites.add(player)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                player.move(event.pos[0])

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT]:
        #     player.update()

        all_sprites.update()
        screen.blit(BACKGROUND_IMG, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
