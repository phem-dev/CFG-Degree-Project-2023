import pygame


class TypewriterText:
    def __init__(self, x, y, text, font_name="Courier New", font_size=40, color=(0, 0, 0), bg_color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.SysFont(font_name, font_size)
        self.color = color
        self.bg_color = bg_color

        self.text_cursor = 0
        self.text_image = self.font.render('', True, self.color, self.bg_color)
        self.next_update = 0
        self.typing_speed = 10  # milliseconds
        self.completed = False

    def update(self, clock):
        current_time = pygame.time.get_ticks()

        if current_time > self.next_update and not self.completed:
            self.next_update = current_time + self.typing_speed
            if self.text_cursor < len(self.text):
                self.text_cursor += 1
                self.text_image = self.font.render(self.text[:self.text_cursor], True, self.color, self.bg_color)
            else:
                self.text_image = self.font.render(self.text, True, self.color, self.bg_color)
                self.completed = True

    def draw(self, surface):
        surface.blit(self.text_image, (self.x, self.y))