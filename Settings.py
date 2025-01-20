import pygame

pygame.init()

FPS = 60
LVL = 0
HEALTH = 100
SHIELD = 100
SCORE = 0
blaster_sound = True
VOLUME = 0.2
# ENEMIES = round(LVL * 2.5)

device_size = device_width, device_height = pygame.display.get_desktop_sizes()[0]
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 1500, 800
if WINDOW_SIZE >= device_size:
    WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = device_size[0] - 100, device_size[1] - 100

music_channel1 = pygame.mixer.Channel(0)
music_channel2 = pygame.mixer.Channel(1)
wait_music = pygame.mixer.Sound('sounds/wait_music.mp3')
game_music = pygame.mixer.Sound('sounds/cyborg-ninja-kevin-macleod-main-version-7993-03-00.mp3')
music_channel1.play(wait_music, loops=-1)
music_channel1.set_volume(VOLUME)

click_effect = pygame.mixer.Sound('sounds/click_mouse.mp3')

shot_effect = pygame.mixer.Sound('sounds/laser_shot.mp3')
button_focused = pygame.mixer.Sound('sounds/focus_mouse.mp3')
start_btn_effect = pygame.mixer.Sound('sounds/start_button.mp3')

START_BG_IMAGE = pygame.transform.scale(pygame.image.load('images/StartBG.png'), WINDOW_SIZE)
MAIN_BG_IMAGE = pygame.transform.scale(pygame.image.load('images/background.png'), WINDOW_SIZE)

PAUSE_FONT1 = pygame.font.Font(None, 60)
PAUSE_FONT2 = pygame.font.Font(None, 28)
START_FONT1 = pygame.font.Font("fonts/RubikGlitch-Regular.ttf", 50)
START_FONT2 = pygame.font.Font("fonts/RubikGlitch-Regular.ttf", 30)
FONT1 = pygame.font.Font("fonts/Sixtyfour-Regular-VariableFont_BLED,SCAN.ttf", 45)
FONT2 = pygame.font.Font("fonts/RubikGlitch-Regular.ttf", 30)

HERO_IMG = pygame.transform.scale(pygame.image.load('images/plane.png'), (100, 50))
ENEMY_IMG = pygame.transform.scale(pygame.image.load('images/red_plane.png'), (60, 60))
ENEMY_IMG = pygame.transform.rotate(ENEMY_IMG, -90)

point = pygame.transform.scale(pygame.image.load('icons/point_scan.png'), (30, 30))

cursor1_img = pygame.transform.rotate(pygame.image.load('icons/rocket_white.png'), 90)
cursor1_img = pygame.transform.scale(cursor1_img, (40, 40))
cursor1 = pygame.cursors.Cursor((0, 0), cursor1_img)

cursor2_img = pygame.transform.rotate(pygame.image.load('icons/highlight_mouse_cursor.png'), 45)
cursor2_img = pygame.transform.scale(cursor2_img, (60, 60))
cursor2 = pygame.cursors.Cursor((0, 0), cursor2_img)

resume_img = pygame.transform.scale(pygame.image.load('icons/resume.png'), (30, 30))
logout_img = pygame.transform.scale(pygame.image.load('icons/logout.png'), (30, 30))
settings_icon = pygame.transform.scale(pygame.image.load('icons/settings.png'), (50, 50))
cancel_button_img = pygame.transform.scale(pygame.image.load('icons/cancel.png'), (40, 40))
toggle_on_img = pygame.transform.scale(pygame.image.load('icons/toggle_on.png'), (60, 60))
toggle_off_img = pygame.transform.scale(pygame.image.load('icons/toggle_off.png'), (60, 60))

file_name = 'scores.txt'


# Сохранение наилучшего результата в txt файле
# Для каждого устройства будет создаваться новый файл
def save_result():
    try:
        with open(file_name, 'r') as file:
            text = file.readlines()
            total_score, total_lvl = int(text[0]), int(text[1])
    except:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write("0\n0")
        total_score = 0
        total_lvl = 0
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(f'{max(total_score, SCORE)}\n{max(total_lvl, LVL)}')


def read_results():
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.readlines()
            total_score, total_lvl = int(text[0]), int(text[1])
    except:
        return 0, 0
    return total_score, total_lvl
