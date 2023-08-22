import pygame


# Fonts
pygame.font.init()

# Font settings

# NEW FONT PATH????**************************************************
# font path = 'Scene_files/spaceranger.ttf'

# Delete below font path ******************************************
font_path = 'Scene_files/kenvector_future.ttf'

FONT = pygame.font.Font(font_path, 40)
FONT_TITLE = pygame.font.Font(font_path, 80)
FONT_MEDIUM = pygame.font.Font(font_path, 25)
FONT_SMALL = pygame.font.Font(font_path, 20)
FONT_VSMALL = pygame.font.Font(font_path, 15)

# Colour (constants are written in all-caps)
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)
RED = (255, 0, 0, 255)
GREEN = (104, 187, 66)
ORANGE = (232, 106, 23)
YELLOW = (255, 204, 0)
BLUE = (30, 167, 225)
PURPLE = (54, 34, 71)
L_PURPLE = (157, 75, 199)
TURQ = (21, 193, 231)
GREY = (128, 128, 128, 255)


# Screen dimensions (this can be changed but all positioning of buttons etc. may need to be scaled relative to this)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Audio
MUSIC_VOLUME = 0.3
MUSIC_PATH = "Scene_files/Audio/CFG Track 2.wav"
BUTTON_VOLUME = 0.4
BUTTON_HOVER_PATH = "Scene_files/Audio/Button hover 1.wav"
BUTTON_CLICK_PATH = "Scene_files/Audio/Button click 1.wav"
MUTED_VOLUME = 0
IS_MUTED = False



