import pygame
from settings import FONT_SMALL, BUTTON_CLICK_PATH


class TextInput:
    def __init__(self, x, y, width, height, font=FONT_SMALL, color=(0, 0, 0), bg_color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font
        self.color = color
        self.bg_color = bg_color
        self.text = ""
        self.margins = 5

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                pass
            else:
                # Render the new text with the appended character to check its width
                new_text = self.text + event.unicode
                txt_surface = self.font.render(new_text, True, self.color)

                # Check if the width of the rendered text is within the boundary of the rectangle
                if txt_surface.get_width() <= self.width - self.margins:
                    self.text = new_text

    def draw(self, screen):
        txt_surface = self.font.render(self.text, True, self.color)
        pygame.draw.rect(screen, self.bg_color, (self.x, self.y, self.width, self.height))
        screen.blit(txt_surface, (self.x + self.margins, self.y))

    def user_answer(self):
        return self.text



