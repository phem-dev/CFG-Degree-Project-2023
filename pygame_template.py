import pygame
import sys  # needed so the system can exit the window when the 'x' is pressed

pygame.init()

# Fonts
pygame.font.init()
FONT = pygame.font.Font(pygame.font.get_default_font(), 32)

# Colour (constants are written in all-caps)
WHITE = (255, 255, 255, 1)
BLACK = (0, 0, 0, 1)
RED = (255, 0, 0, 1)
BLUE = (0, 0, 255, 1)
GREY = (128, 128, 128, 1)

# Screen dimensions (this can be changed but all positioning of buttons etc. may nned to be scaled releatice to this)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# If we want to standardise the button sizes
BUTTON_WIDTH = 140
BUTTON_HEIGHT = 80

# Create screen and clock, clock will be needed to help make animations and waits https://www.pygame.org/docs/ref/time.html
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # set the screen size
pygame.display.set_caption('Stratobus Mission')  # set the window title
clock = pygame.time.Clock()  # make a clock object, so we can use its method 'clock.tick(30) later, this will slow the frame rate (or refresh rate) to 30 frames per second during while loops instead of doing the while loop nearly instantaneously


########################################################################################################################

class Button:
    """
    Representss a rectangular button.

    Attributes:
        x (int): The x coordinate of the button (with origin in the top left) in pixels.
        y (int): The y coordinate of the button (with origin in the top left) in pixels.
        width (int): The width of the button in pixels.
        length (int): The length of the button in pixels.
        colour  (tuple[int, int, int, int]) : The background colour of the button in r,g,b,a format (red, green, blue, alpha (or opacity)).
        hover_colour  (tuple[int, int, int, int]) : The background colour of the button when mouse hovered in r,g,b,a format (red, green, blue, alpha (or opacity)).
        text (str): The text to display on teh button.
        text_colour  (tuple[int, int, int, int]) : The text colour of the button in r,g,b,a format (red, green, blue, alpha (or opacity)).
        hover_text_colour  (tuple[int, int, int, int]) : The text colour of the button when mouse hovered in r,g,b,a format (red, green, blue, alpha (or opacity)).
        action (function): A function to be called when the button is clicked.
    """

    def __init__(self, x, y, width, height, colour, hover_colour, text, text_colour, hover_text_colour, action):
        self.rect = pygame.Rect(x, y, width, height)
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

        pygame.draw.rect(surface, current_colour, self.rect)  # draw the button rectangle
        text_surface = FONT.render(self.text, True,
                                   current_text_colour)  # render the button ready for adding (blit) to the screen surface, True here has enabled anti-aliasing on the text to make it render nice and smooth on the edges (not as pixely)
        text_rect = text_surface.get_rect(
            center=self.rect.center)  # make a rectangle bounding box for the text and match the center to the button rect center
        surface.blit(text_surface,
                     text_rect)  # blit is used to actually add the rendered button surface to the the screen surface at the position defined by text_rect

    def handle_event(self, event):
        """
            Event handling for the button click, it calls the action.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()


########################################################################################################################

class SceneManager:
    """
        Manages a scene/page displayed, including switching to a new scene

        Attributes:
            current_scene (object): The current active scene. Expected to have `handle_event`, `update`, and `draw` methods.
    """

    def __init__(self):
        """Initialises the SceneManager having no active scene."""
        self.current_scene = None

    def switch_scene(self, scene):
        """Updates the current scene with a new one."""
        self.current_scene = scene

    def handle_event(self, event):
        """If the current screen is active it takes in an event ready to be handled."""
        if self.current_scene:
            self.current_scene.handle_event(event)

    # the update and draw functions will be used in while loops to update/refresh what is ready to show and then show/draw it
    def update(self):
        """If the current screen is active it can be called to be updated before its drawn( below)"""
        if self.current_scene:
            self.current_scene.update()

    def draw(self, screen):
        """Calls the current scene's draw method with the given screen."""
        if self.current_scene:
            self.current_scene.draw(screen)


########################################################################################################################
# Scene superclass, is an abstract class to be used as a template, it includes the essential (but empty so far) methods for a scene
class Scene:
    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass


# This class inherits from the Scene superclass (which insures every subclass has the event handler, update and draw method to modify (polymorphism))
class SceneStart(Scene):
    # here we will pass the SceneManager class as an attribute to allow to change scene... eg. scene_manager.switch_scene(SceneStart(SceneManager()))  # start scene 1
    def __init__(self, manager):
        self.manager = manager

        # here we define the things to be drawn byt the draw method  further down
        self.button1 = Button(
            SCREEN_WIDTH // 2 - (BUTTON_WIDTH + 10), SCREEN_HEIGHT * 0.8, BUTTON_WIDTH, BUTTON_HEIGHT,
            RED, BLUE, "Black", BLACK, WHITE, self.to_scene_black
        )
        self.button2 = Button(
            SCREEN_WIDTH // 2 + 10, SCREEN_HEIGHT * 0.8, BUTTON_WIDTH, BUTTON_HEIGHT,
            RED, BLUE, "Grey", BLACK, WHITE, self.to_scene3
        )

    # here we define some actions as functions to be called on button clicks
    def to_scene_black(self):
        self.manager.switch_scene(SceneBlack(self.manager))

    def to_scene3(self):
        self.manager.switch_scene(Scene3(self.manager))

    # here we have an event handler, evets are fed in using a while loop with "for event in pygame.event.get():"
    def handle_event(self, event):
        self.button1.handle_event(event)
        self.button2.handle_event(event)

    def draw(self, screen):
        screen.fill(WHITE)
        self.button1.draw(screen)
        self.button2.draw(screen)


class SceneBlack(Scene):
    def __init__(self, manager):
        self.manager = manager

        # Adjust these buttons to your needs for the second scene
        self.button1 = Button(
            SCREEN_WIDTH // 2 - (BUTTON_WIDTH + 10), SCREEN_HEIGHT * 0.8, BUTTON_WIDTH, BUTTON_HEIGHT,
            GREY, BLUE, "Back", BLACK, WHITE, self.back_to_scene_start
        )
        self.button2 = Button(
            SCREEN_WIDTH // 2 + 10, SCREEN_HEIGHT * 0.8, BUTTON_WIDTH, BUTTON_HEIGHT,
            GREY, BLUE, "Quit", BLACK, WHITE, sys.exit
        )

    def back_to_scene_start(self):
        self.manager.switch_scene(SceneStart(self.manager))

    def handle_event(self, event):
        self.button1.handle_event(event)
        self.button2.handle_event(event)

    def draw(self, screen):
        screen.fill(BLACK)
        self.button1.draw(screen)
        self.button2.draw(screen)


class Scene3(Scene):
    def __init__(self, manager):
        self.manager = manager

        # Adjust these buttons to your needs for the second scene
        self.button1 = Button(
            SCREEN_WIDTH // 2 - (BUTTON_WIDTH + 10), SCREEN_HEIGHT * 0.8, BUTTON_WIDTH, BUTTON_HEIGHT,
            GREY, BLUE, "Back", BLACK, WHITE, self.back_to_scene1
        )
        self.button2 = Button(
            SCREEN_WIDTH // 2 + 10, SCREEN_HEIGHT * 0.8, BUTTON_WIDTH, BUTTON_HEIGHT,
            GREY, BLUE, "Quit", BLACK, WHITE, sys.exit
        )

    def back_to_scene1(self):
        self.manager.switch_scene(SceneStart(self.manager))

    def handle_event(self, event):
        self.button1.handle_event(event)
        self.button2.handle_event(event)

    def draw(self, screen):
        screen.fill(GREY)
        self.button1.draw(screen)
        self.button2.draw(screen)


def main():
    scene_manager = SceneManager()  # object instantiation for the SceneManager
    scene_manager.switch_scene(SceneStart(scene_manager))  # start scene 1

    # start running the game but always listen for the event of the user clicking exit or any other events to handle
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # exit event
                pygame.quit()
                sys.exit()
            scene_manager.handle_event(event)  # any other events are passed to whatever scene is active for processing by that specific scene (a button click on a part of a screen could overlap with button clicks on any scene otherwise)

        # continuously (beacasue we are in a while true loop) update the scene, draw the scene, and re-render the display at 30fps
        scene_manager.update()
        scene_manager.draw(screen)
        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
