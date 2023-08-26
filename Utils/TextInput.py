import pygame
from Scene_files.settings import FONT_SMALL


class TextInput:
    """
    A simple text input class for pygame.

    Attributes:
        x, y (int): Position of the top-left corner of the input box.
        width, height (int): Dimensions of the input box.
        font (pygame.font.Font): Font used for rendering the text.
        color (tuple): RGB color of the text.
        bg_color (tuple): RGB background color of the input box.
        text (str): The current text inside the input box.
        margins (int): Margins inside the input box.

        # For flashing caret
        caret_visible (bool): Whether the caret is currently visible.
        frame_count (int): Frame counter for caret flashing.
        frames_for_toggle (int): Number of frames to toggle the caret visibility.
    """

    def __init__(self, x, y, width, height, font=FONT_SMALL, color=(0, 0, 0), bg_color=(255, 255, 255)):
        """Initialize the text input box with given position, dimensions, font, and colors."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font
        self.color = color
        self.bg_color = bg_color
        self.text = ""
        self.margins = 5

        # Initialize attributes for flashing caret
        self.caret_visible = False
        self.frame_count = 0
        self.frames_for_toggle = 30  # Number of frames to toggle caret visibility.

    def handle_event(self, event):
        """Handle keyboard events related to text input."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                pass  # Do nothing for Enter key.
            else:
                # Render the new text with the appended character to check its width.
                new_text = self.text + event.unicode
                txt_surface = self.font.render(new_text, True, self.color)

                # Append the new character only if the text fits within the input box.
                if txt_surface.get_width() <= self.width - self.margins:
                    self.text = new_text

    def draw(self, screen):
        """Draw the text input box and the text on the given screen."""
        txt_surface = self.font.render(self.text, True, self.color)
        pygame.draw.rect(screen, self.bg_color, (self.x, self.y, self.width, self.height))
        screen.blit(txt_surface, (self.x + self.margins, self.y))

        # Manage the flashing caret logic and drawing.
        self.frame_count += 1
        if self.frame_count % self.frames_for_toggle == 0:
            self.caret_visible = not self.caret_visible
        if self.caret_visible:
            caret_x = self.x + self.margins + txt_surface.get_width()
            caret_y = self.y + self.margins
            caret_height = txt_surface.get_height() - 2 * self.margins
            pygame.draw.line(screen, self.color, (caret_x, caret_y), (caret_x, caret_y + caret_height))

    def user_answer(self):
        """Return the current text inside the input box."""
        return self.text
