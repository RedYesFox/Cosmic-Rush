import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Castle Defense")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Шрифт для отображения счета и здоровья
font = pygame.font.Font(None, 36)

# Герой
class Hero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (100, HEIGHT // 2)
        self.health = 100

# Катапульта
class Catapult(pygame.sprite.Sprite):
    def __init__(self, hero):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.hero = hero
        self.update_position()

    def update_position(self):
        self.rect.center = (self.hero.rect.right + 20, self.hero.rect.centery)

# Зомби
class Zombie(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed

# Снаряд
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5

    def update(self):
        self.rect.x += self.speed

# Группы спрайтов
all_sprites = pygame.sprite.Group()
zombies = pygame.sprite.Group()
projectiles = pygame.sprite.Group()

hero = Hero()
catapult = Catapult(hero)
all_sprites.add(hero, catapult)

# Игровые переменные
score = 0
level = 1
zombie_speed = 1
zombie_spawn_rate = 120  # Каждые 2 секунды (120 кадров)

# Игровой цикл
running = True
clock = pygame.time.Clock()
zombie_spawn_timer = 0

def draw_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (x, y))

while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                projectile = Projectile(catapult.rect.centerx, catapult.rect.centery)
                all_sprites.add(projectile)
                projectiles.add(projectile)

    # Обновление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        hero.rect.y -= 5
    if keys[pygame.K_DOWN]:
        hero.rect.y += 5
    
    hero.rect.clamp_ip(screen.get_rect())
    catapult.update_position()

    # Создание зомби
    zombie_spawn_timer += 1
    if zombie_spawn_timer >= zombie_spawn_rate:
        zombie = Zombie(zombie_speed)
        all_sprites.add(zombie)
        zombies.add(zombie)
        zombie_spawn_timer = 0

    # Обновление спрайтов
    all_sprites.update()

    # Проверка столкновений
    for projectile in projectiles:
        zombie_hits = pygame.sprite.spritecollide(projectile, zombies, True)
        if zombie_hits:
            projectile.kill()
            score += 10

    # Проверка столкновений героя с зомби
    zombie_hits = pygame.sprite.spritecollide(hero, zombies, True)
    if zombie_hits:
        hero.health -= 10
        if hero.health <= 0:
            running = False

    # Увеличение сложности
    if score >= level * 100:
        level += 1
        zombie_speed += 0.5
        zombie_spawn_rate = max(30, zombie_spawn_rate - 10)

    # Отрисовка
    screen.fill(WHITE)
    all_sprites.draw(screen)
    
    # Отображение счета, уровня и здоровья
    draw_text(f"Score: {score}", 10, 10)
    draw_text(f"Level: {level}", 10, 50)
    draw_text(f"Health: {hero.health}", WIDTH - 150, 10)

    pygame.display.flip()

    # Ограничение FPS
    clock.tick(60)

# Отображение экрана Game Over
screen.fill(WHITE)
draw_text("GAME OVER", WIDTH // 2 - 100, HEIGHT // 2 - 50)
draw_text(f"Final Score: {score}", WIDTH // 2 - 100, HEIGHT // 2 + 50)
pygame.display.flip()

# Ожидание перед закрытием игры
pygame.time.wait(3000)

pygame.quit()