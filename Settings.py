import pygame

pygame.init()

FPS = 60
LVL = 0
HEALTH = 100
score = 0
blaster_sound = True

device_size = device_width, device_height = pygame.display.get_desktop_sizes()[0]
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 1500, 800
if WINDOW_SIZE >= device_size:
    WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = device_size[0] - 100, device_size[1] - 100

pygame.mixer.music.load('sounds/wait_music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(50)
click_effect = pygame.mixer.Sound('sounds/laser-gun-beam-blaster-shot_fjfjpfvu.mp3')
shot_effect = pygame.mixer.Sound('sounds/laser_shot.mp3')

START_BG_IMAGE = pygame.image.load('images/StartBG.png')
MAIN_BG_IMAGE = pygame.image.load('images/background.png')

PAUSE_FONT1 = pygame.font.Font(None, 45)
PAUSE_FONT2 = pygame.font.Font(None, 30)
START_FONT = pygame.font.Font("fonts/RubikGlitch-Regular.ttf", 50)
FONT = pygame.font.Font("fonts/Sixtyfour-Regular-VariableFont_BLED,SCAN.ttf", 45)

HERO_IMG = pygame.image.load('images/plane.png')
HERO_IMG = pygame.transform.scale(HERO_IMG, (100, 50))
ENEMY_IMG = pygame.image.load('images/red_plane.png')
ENEMY_IMG = pygame.transform.scale(ENEMY_IMG, (60, 60))
ENEMY_IMG = pygame.transform.rotate(ENEMY_IMG, -90)

cursor1_img = pygame.image.load('icons/rocket_white.png')
cursor1_img = pygame.transform.rotate(cursor1_img, 90)
cursor1_img = pygame.transform.scale(cursor1_img, (40, 40))
cursor1 = pygame.cursors.Cursor((0, 0), cursor1_img)

cursor2_img = pygame.image.load('icons/highlight_mouse_cursor.png')
cursor2_img = pygame.transform.rotate(cursor2_img, 45)
cursor2_img = pygame.transform.scale(cursor2_img, (60, 60))
cursor2 = pygame.cursors.Cursor((0, 0), cursor2_img)

point = pygame.image.load('icons/point_scan.png')
point = pygame.transform.scale(point, (30, 30))

settings_icon = pygame.image.load('icons/settings.png')
settings_icon = pygame.transform.scale(settings_icon, (50, 50))

toggle_on_img = pygame.image.load('icons/toggle_on.png')
toggle_on_img = pygame.transform.scale(toggle_on_img, (60, 60))
toggle_off_img = pygame.image.load('icons/toggle_off.png')
toggle_off_img = pygame.transform.scale(toggle_off_img, (60, 60))


# Сохранение только последнего результата в txt файле
def save_result(score):
    with open('scores.txt', 'a') as file:
        file.write(f'{score}\n')
