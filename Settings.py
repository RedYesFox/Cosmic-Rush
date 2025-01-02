import os, sys
import pygame

pygame.init()

# def load_image(name, colorkey=None, folder='images'):
#     fullname = os.path.join(folder, name)
#     if not os.path.isfile(fullname):
#         print(f"Файл с изображением '{fullname}' не найден")
#         sys.exit()
#     image = pygame.image.load(fullname)
#     if colorkey is not None:
#         image = image.convert()
#         if colorkey == -1:
#             colorkey = image.get_at((0, 0))
#         image.set_colorkey(colorkey)
#     else:
#         image = image.convert_alpha()
#     return image

FPS = 60
LVL = 0
HEALTH = 100
score = 0

device_size = device_width, device_height = pygame.display.get_desktop_sizes()[0]
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 1520, 780
if WINDOW_SIZE >= device_size:
    WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = device_size[0] - 100, device_size[1] - 100

START_BG_IMAGE = pygame.image.load('images/StartBG.png')
MAIN_BG_IMAGE = pygame.image.load('images/background.png')

PAUSE_FONT = pygame.font.Font(None, 45)
START_FONT = pygame.font.Font("fonts/RubikGlitch-Regular.ttf", 50)
FONT = pygame.font.Font("fonts/Sixtyfour-Regular-VariableFont_BLED,SCAN.ttf", 45)

cursor1_img = pygame.image.load('icons/rocket_white.png')
cursor1_img = pygame.transform.rotate(cursor1_img, 90)
cursor1_img = pygame.transform.scale(cursor1_img, (40, 40))
cursor1 = pygame.cursors.Cursor((0, 0), cursor1_img)

cursor2_img = pygame.image.load('icons/highlight_mouse_cursor.png')
cursor2_img = pygame.transform.rotate(cursor2_img, 45)
cursor2_img = pygame.transform.scale(cursor2_img, (60, 60))
cursor2 = pygame.cursors.Cursor((0, 0), cursor2_img)

# Сохранение только последнего результата в txt файле
def save_result(score):
    with open('scores.txt', 'a') as file:
        file.write(f'{score}\n')
