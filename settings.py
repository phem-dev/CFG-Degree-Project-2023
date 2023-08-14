import pygame


# Fonts
pygame.font.init()
# FONT = pygame.font.Font(pygame.font.get_default_font(), 32)
FONT = pygame.font.SysFont("Courier New", 40, bold=True, italic=False)
TITLE_FONT = pygame.font.SysFont("Courier New", 60, bold=True, italic=False)

# Colour (constants are written in all-caps)
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)
RED = (255, 0, 0, 255)
BLUE = (0, 0, 255, 255)
GREY = (128, 128, 128, 255)
PURPLE = (128, 0, 255, 255)

# Screen dimensions (this can be changed but all positioning of buttons etc. may need to be scaled relative to this)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
