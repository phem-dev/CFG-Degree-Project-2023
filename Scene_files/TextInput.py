import pygame
from settings import FONT_SMALL


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

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    # def update(self):
    #     pass

    def draw(self, screen):
        txt_surface = self.font.render(self.text, True, self.color)
        pygame.draw.rect(screen, self.bg_color, (self.x, self.y, self.width, self.height))
        screen.blit(txt_surface, (self.x, self.y))

    def user_answer(self):
        return self.text



