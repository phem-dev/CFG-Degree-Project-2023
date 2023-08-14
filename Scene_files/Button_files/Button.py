import pygame
from Scene_files.Button_files.draw_rounded_rect import draw_rounded_rect # instead of the pygame.draw.rect, use this custom function for a rounded rectangle in the Button class
from settings import FONT
from settings import SCREEN_HEIGHT, SCREEN_WIDTH



# If we want to standardise the button sizes
# BUTTON_WIDTH = SCREEN_WIDTH / 5       #  been updated to be width of text
# BUTTON_HEIGHT = SCREEN_HEIGHT / 12    #  been updated to be height of text


class Button:
    """
    Represents a rectangular button.

    Attributes:
        x (int, or string): The x coordinate of the button (with origin in the top left) in pixels, Or "center for center justification or "left" or "right"
        y (int): The y coordinate of the button (with origin in the top left) in pixels.
        colour  (tuple[int, int, int, int]) : The background colour of the button in r,g,b,a format (red, green, blue, alpha (or opacity)).
        hover_colour  (tuple[int, int, int, int]) : The background colour of the button when mouse hovered in r,g,b,a format (red, green, blue, alpha (or opacity)).
        text (str): The text to display on teh button.
        text_colour  (tuple[int, int, int, int]) : The text colour of the button in r,g,b,a format (red, green, blue, alpha (or opacity)).
        hover_text_colour  (tuple[int, int, int, int]) : The text colour of the button when mouse hovered in r,g,b,a format (red, green, blue, alpha (or opacity)).
        action (function): A function to be called when the button is clicked.
    """

    def __init__(self, x, y, colour, hover_colour, text, text_colour, hover_text_colour, action):
        self.width = FONT.size(text)[0] * 1.1
        self.height = FONT.size(text)[1] * 1.1

        if x == "center":
            x = (SCREEN_WIDTH // 2) - (self.width // 2)
        elif x == "left":
            x = SCREEN_WIDTH * 0.1
        elif x == "right":
            x = (SCREEN_WIDTH * 0.9) - self.width

        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.colour = colour
        self.hover_colour = hover_colour
        self.text = text
        self.text_colour = text_colour
        self.hover_text_colour = hover_text_colour
        self.action = action

    def draw(self, surface):
        """
            Draws the button on the provided surface, listens for collision/hover and updates colours.
        """
        current_colour = self.colour
        current_text_colour = self.text_colour

        # the bit means: if the rectangle representing the button area (self.rect) collides wth where the mouse is update the button colour
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            current_colour = self.hover_colour
            current_text_colour = self.hover_text_colour

        draw_rounded_rect(surface, current_colour, self.rect, (self.height * 0.1))  # draw the button rectangle
        text_surface = FONT.render(self.text, True, current_text_colour)  # render the button ready for adding (blit) to the screen surface, True here has enabled anti-aliasing on the text to make it render nice and smooth on the edges (not as pixely)
        text_rect = text_surface.get_rect(center=self.rect.center)  # make a rectangle bounding box for the text and match the center to the button rect center
        surface.blit(text_surface, text_rect)  # blit is used to actually add the rendered button surface to the the screen surface at the position defined by text_rect

    def handle_event(self, event):
        """
            Event handling for the button click, it calls the action.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()
