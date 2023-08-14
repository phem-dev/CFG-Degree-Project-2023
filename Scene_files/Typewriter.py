import pygame
from settings import FONT

class TypewriterText:
    """
    A class representing text that appears character-by-character then line-by-line in a typewriter fashion constricted to a bounding box and left-justified.

    Attributes:
    x (int): The x-coordinate for the upper-left corner of the text box.
    y (int): The y-coordinate for the upper-left corner of the text box.
    width (int): The width of the bounding box.
    height (int): The height of the bounding box.
    text (str): The complete text to be displayed.
    font (pygame.font.Font): The font used for rendering the text.
    colour (tuple): The RGBA colour of the text.
    justify (str): The alignment of the lines when wrapped, either "left", "center" or "right" ("left" by default).
    """

    def __init__(self, x, y, width, height, text, font=FONT, colour=(255, 255, 255, 255), justify="left"):
        # Initialize bounding box properties
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Initialize text properties
        self.text = text
        self.font = font  # default is FONT imported from the settings.py
        self.colour = colour  # Text colour, is default white (not imported from settings.py but could be?)
        self.justify = justify

        # Text typing related variables
        self.text_cursor = 0  # Index of the character currently being typed
        self.current_line = ""  # The current line of text being constructed
        self.next_line = ""  # Predicted next line of text
        self.lines = []  # All the lines of text that have been completely typed out
        self.next_update = 0  # Time when the next character will be added (to be an accumulator)
        self.typing_speed = 10  # Time (in milliseconds) to wait before rendering next character (though speed is limited by main game clock?)
        self.completed = False  # Whether all the text has been typed out or not
        self.typed_text = ""  # Accumulated text that has been typed so far

    def update(self):
        """
        Updates the text's state, adding characters and new lines (with line breaks at whole words) as time passes.

        Raises:
        ValueError: If the accumulated lines exceed the height of the bounding box.
        """

        # Get the current time
        current_time = pygame.time.get_ticks()

        # Check if it's time to add a new character and typing is not finished
        if current_time > self.next_update and not self.completed:
            # Set the next update time based on typing speed
            self.next_update = current_time + self.typing_speed

            # Check if there's still text left to type out
            if self.text_cursor < len(self.text):
                char = self.text[self.text_cursor]

                # If it's not a space, add the character to the current line
                if char != ' ':
                    self.current_line += char
                else:
                    # Check if adding the character would exceed the bounding box width
                    potential_line = self.current_line + char
                    if self.font.size(potential_line)[0] <= self.width:
                        self.current_line = potential_line
                    else:
                        # Start a new line and store the completed line
                        self.lines.append(self.current_line)
                        self.current_line = ""

                # Move to the next character in the text
                self.text_cursor += 1
                self.typed_text += char
            else:
                # If all text has been typed, mark typing as completed
                if self.current_line:
                    self.lines.append(self.current_line)
                self.completed = True

            # Check if the text exceeds the height of the bounding box, will raise an error in case a tester doesn't notice it being cut-off
            total_lines_height = (len(self.lines) + 1) * self.font.get_height()
            if total_lines_height > self.height:
                raise ValueError(f"The text starting with: '{self.typed_text}' exceeds the bounding box height.")

    def draw(self, surface):
        """
        Draws the typed text made in the update function on the given surface.

        Args:
        surface (pygame.Surface): The surface on which the text should be rendered and drawn.
        """

        y_offset = 0
        for line_text in self.lines:
            line_surface = self.font.render(line_text, True, self.colour)
            x_offset = self.get_x_offset(line_surface)
            surface.blit(line_surface, (self.x + x_offset, self.y + y_offset))
            y_offset += self.font.get_height()

        if not self.completed:
            current_line_surface = self.font.render(self.current_line, True, self.colour)
            x_offset = self.get_x_offset(current_line_surface)
            surface.blit(current_line_surface, (self.x + x_offset, self.y + y_offset))

    def get_x_offset(self, surface):
        """Calculate the x offset based on justification."""
        if self.justify == "center":
            return (self.width - surface.get_width()) // 2
        elif self.justify == "right":
            return self.width - surface.get_width()
        else:  # Default to left justification
            return 0
