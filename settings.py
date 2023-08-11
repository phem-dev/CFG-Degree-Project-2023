import pygame


# Fonts
pygame.font.init()
# FONT = pygame.font.Font(pygame.font.get_default_font(), 32)
FONT = pygame.font.SysFont("Courier New", 40, bold=True, italic=False)

# Colour (constants are written in all-caps)
WHITE = (255, 255, 255, 1)
BLACK = (0, 0, 0, 1)
RED = (255, 0, 0, 1)
BLUE = (0, 0, 255, 1)
GREY = (128, 128, 128, 1)

# Screen dimensions (this can be changed but all positioning of buttons etc. may nned to be scaled releatice to this)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
