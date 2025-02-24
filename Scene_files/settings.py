import pygame
import os

# Fonts
pygame.font.init()

# Get the directory where the current settings.py script resides
current_dir = os.path.dirname(os.path.abspath(__file__))
# now anything pointing to a directory is redefined by applying the hosts absolute path

font_path = os.path.join(current_dir, "kenvector_future.ttf")

FONT = pygame.font.Font(font_path, 35)
FONT_TITLE = pygame.font.Font(font_path, 80)
FONT_MEDIUM = pygame.font.Font(font_path, 25)
FONT_MEDSMALL = pygame.font.Font(font_path, 18)
FONT_SMALL = pygame.font.Font(font_path, 20)
FONT_VSMALL = pygame.font.Font(font_path, 15)
FONT_TINY = pygame.font.Font(font_path, 13)
FONT_TEENYTINY = pygame.font.Font(font_path, 7)


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
MUSIC_PATH = os.path.join(current_dir, "Audio\CFG Track 2.wav")
BUTTON_VOLUME = 0.4
BUTTON_HOVER_PATH = os.path.join(current_dir, "Audio\Button hover 1.wav")
BUTTON_CLICK_PATH = os.path.join(current_dir, "Audio\Button click 1.wav")
MUTED_VOLUME = 0
IS_MUTED = False



