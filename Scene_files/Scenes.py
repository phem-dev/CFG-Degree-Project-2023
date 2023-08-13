import sys
from Scene_files.SceneManager import Scene
from Scene_files.Button_files.Button import Button, BUTTON_HEIGHT, BUTTON_WIDTH
from settings import WHITE, BLACK, RED, BLUE, GREY, PURPLE, SCREEN_HEIGHT, SCREEN_WIDTH
from Scene_files.Typewriter import TypewriterText
from Missions.stratobus_challenges_DRAFT import Challenge


########################################################################################################################

class SceneStart(Scene):
    # here we will pass the SceneManager class as an attribute to allow to change scene... eg. scene_manager.switch_scene(SceneStart(SceneManager()))  # start scene 1
    def __init__(self, manager, game_clock):
        self.manager = manager
        self.game_clock = game_clock
        self.title = "Asteroid"
        self.typewriter = TypewriterText(50, 50, 500, 500, Challenge.greet(Challenge(self.title)))

        # here we define the things to be drawn byt the draw method  further down
        self.button1 = Button(
            SCREEN_WIDTH // 2 - (BUTTON_WIDTH + (SCREEN_WIDTH * 0.1)), (SCREEN_HEIGHT * 0.8), BUTTON_WIDTH, BUTTON_HEIGHT,
            RED, BLUE, "Black", BLACK, WHITE, self.to_scene_black
        )
        self.button2 = Button(
            SCREEN_WIDTH // 2 + (SCREEN_WIDTH * 0.1), (SCREEN_HEIGHT * 0.8), BUTTON_WIDTH, BUTTON_HEIGHT,
            RED, BLUE, "Grey", BLACK, WHITE, self.to_scene3
        )

    # here we define some actions as functions to be called on button clicks
    def to_scene_black(self):
        self.manager.switch_scene(SceneBlack(self.manager, self.game_clock))

    def to_scene3(self):
        self.manager.switch_scene(SceneGrey(self.manager, self.game_clock))

    # here we have an event handler, events are fed in using a while loop with "for event in pygame.event.get():"
    def handle_event(self, event):
        self.button1.handle_event(event)
        self.button2.handle_event(event)

    def update(self):
        self.typewriter.update()

    def draw(self, screen):
        screen.fill(PURPLE)
        self.typewriter.draw(screen)
        self.button1.draw(screen)
        self.button2.draw(screen)


########################################################################################################################


class SceneBlack(Scene):
    def __init__(self, manager, game_clock):
        self.manager = manager
        self.game_clock = game_clock

        # Adjust these buttons to your needs for the second scene
        self.button1 = Button(
            SCREEN_WIDTH // 2 - (BUTTON_WIDTH + (SCREEN_WIDTH * 0.1)), (SCREEN_HEIGHT * 0.8), BUTTON_WIDTH, BUTTON_HEIGHT,
            GREY, BLUE, "Back", BLACK, WHITE, self.back_to_scene_start
        )
        self.button2 = Button(
            SCREEN_WIDTH // 2 + (SCREEN_WIDTH * 0.1), (SCREEN_HEIGHT * 0.8), BUTTON_WIDTH, BUTTON_HEIGHT,
            GREY, BLUE, "Quit", BLACK, WHITE, sys.exit
        )

    def back_to_scene_start(self):
        self.manager.switch_scene(SceneStart(self.manager, self.game_clock))

    def handle_event(self, event):
        self.button1.handle_event(event)
        self.button2.handle_event(event)

    def draw(self, screen):
        screen.fill(BLACK)
        self.button1.draw(screen)
        self.button2.draw(screen)


########################################################################################################################


class SceneGrey(Scene):
    def __init__(self, manager, game_clock):
        self.manager = manager
        self.game_clock = game_clock

        # Adjust these buttons to your needs for the second scene
        self.button1 = Button(
            SCREEN_WIDTH // 2 - (BUTTON_WIDTH + (SCREEN_WIDTH * 0.1)), (SCREEN_HEIGHT * 0.8), BUTTON_WIDTH, BUTTON_HEIGHT,
            GREY, BLUE, "Back", BLACK, WHITE, self.back_to_scene_start
        )
        self.button2 = Button(
            SCREEN_WIDTH // 2 + (SCREEN_WIDTH * 0.1), (SCREEN_HEIGHT * 0.8), BUTTON_WIDTH, BUTTON_HEIGHT,
            GREY, BLUE, "Quit", BLACK, WHITE, sys.exit
        )

    def back_to_scene_start(self):
        self.manager.switch_scene(SceneStart(self.manager, self.game_clock))

    def handle_event(self, event):
        self.button1.handle_event(event)
        self.button2.handle_event(event)

    def draw(self, screen):
        screen.fill(GREY)
        self.button1.draw(screen)
        self.button2.draw(screen)
