import sys
import pygame
from Scene_files.SceneManager import Scene
from Scene_files.Button_files.Button import Button
from settings import WHITE, BLACK, RED, GREEN, ORANGE, YELLOW, BLUE, PURPLE, L_PURPLE, TURQ, GREY, SCREEN_HEIGHT, \
    SCREEN_WIDTH, FONT_TITLE, FONT_SMALL, FONT, FONT_VSMALL
from Scene_files.Typewriter import TypewriterText
from Missions.Mission1_Asteroids import Challenge
from Scene_files.TextInput import TextInput


########################################################################################################################
# START AND CONTROLS
########################################################################################################################


class SceneStart(Scene):
    # here we will pass the SceneManager class as an attribute to allow to change scene... eg. scene_manager.switch_scene(SceneStart(SceneManager()))  # start scene 1
    def __init__(self, manager, game_clock):
        self.manager = manager
        self.game_clock = game_clock
        self.title = "Stratobus Missions"
        self.typewriter = TypewriterText(150, 120, 500, 500, self.title, FONT_TITLE, justify="center")
        # self.typewriter = TypewriterText(50, 50, 500, 500, Challenge.greet(Challenge(self.title)), 100) #  to use in missions

        # here we define the things to be drawn byt the draw method further down
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.6), GREEN, BLUE, "PLAY", BLACK, WHITE, self.to_scene_mission_asteroids
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.72), YELLOW, BLUE, "CONTROLS", BLACK, WHITE, self.to_controls
        )
        self.button3 = Button(
            "center", (SCREEN_HEIGHT * 0.84), ORANGE, BLUE, "EXIT", BLACK, WHITE, sys.exit
        )

    # here we define some actions as functions to be called on button clicks
    def to_scene_mission_asteroids(self):
        self.manager.switch_scene(SceneMissionAsteroids(self.manager, self.game_clock))

    def to_controls(self):
        self.manager.switch_scene(SceneControls(self.manager, self.game_clock))

    # here we have an event handler, events are fed in using a while loop with "for event in pygame.event.get():" in the main game.py
    def handle_event(self, event):
        self.button1.handle_event(event)
        self.button2.handle_event(event)
        self.button3.handle_event(event)

    def update(self):
        self.typewriter.update()

    def draw(self, screen):
        screen.fill(PURPLE)
        self.typewriter.draw(screen)
        self.button1.draw(screen)
        self.button2.draw(screen)
        self.button3.draw(screen)


########################################################################################################################


class SceneControls(Scene):
    def __init__(self, manager, game_clock):
        self.manager = manager
        self.game_clock = game_clock

        # Adjust these buttons to your needs for the second scene
        self.button1 = Button(
            "right", (SCREEN_HEIGHT * 0.6), GREY, BLUE, "BACK", BLACK, WHITE, self.back_to_scene_start
        )
        self.button2 = Button(
            "right", (SCREEN_HEIGHT * 0.72), ORANGE, BLUE, "EXIT", BLACK, WHITE, sys.exit
        )

    def back_to_scene_start(self):
        self.manager.switch_scene(SceneStart(self.manager, self.game_clock))

    def handle_event(self, event):
        self.button1.handle_event(event)
        self.button2.handle_event(event)

    def draw(self, screen):
        screen.fill(TURQ)
        self.button1.draw(screen)
        self.button2.draw(screen)


########################################################################################################################
# MISSIONS
########################################################################################################################
# ASTEROIDS
class SceneMissionAsteroids(Scene):
    def __init__(self, manager, game_clock):
        self.manager = manager
        self.game_clock = game_clock
        self.title = "Asteroid"
        self.block = "In this challenge you will track 3 asteroids and see how close they passed by Earth. Report the data back to base to complete the mission!"
        self.typewriter_title = TypewriterText(130, 20, 550, 500, Challenge.greet(Challenge(self.title)), justify="center")
        self.typewriter_block = TypewriterText(150, 200, 430, 200, self.block, font=FONT_SMALL)
        self.mission_box_image = pygame.image.load('./Scene_files/Images/mission_box.png')

        # Adjust these buttons to your needs for the second scene
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.75), GREEN, BLUE, "ACCEPT", BLACK, WHITE, self.to_scene_mission_asteroids_input
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "EXIT", BLACK, WHITE, sys.exit
        )

    def to_scene_mission_asteroids_input(self):
        self.manager.switch_scene(SceneMissionAsteroidsInput(self.manager, self.game_clock))

    def handle_event(self, event):
        self.button1.handle_event(event)
        self.button2.handle_event(event)

    def update(self):
        # Always update the typewriter_title
        self.typewriter_title.update()

        # Only update typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.update()

    def draw(self, screen):
        screen.fill(GREY)
        screen.blit(self.mission_box_image, (75, 120))
        self.typewriter_title.draw(screen)

        # Only draw typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.draw(screen)

        self.button1.draw(screen)
        self.button2.draw(screen)


########################################################################################################################

class SceneMissionAsteroidsInput(Scene):
    def __init__(self, manager, game_clock):
        self.manager = manager
        self.game_clock = game_clock
        # title
        self.title = "Asteroids Mission"
        self.typewriter_title = TypewriterText(130, 20, 550, 500, self.title, justify="center")
        # display text box
        self.display_bl_image = pygame.image.load('./Scene_files/Images/display_bl.png')
        self.typewriter_display_head = TypewriterText(55, 105, 200, 100, "Data Received", font=FONT_SMALL, colour=(0, 0, 0, 0))
        self.display_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam."
        self.typewriter_display = TypewriterText(55, 180, 200, 200, self.display_text, font=FONT_VSMALL, colour=(0, 0, 0, 0))
        # input box
        self.trivia_box1_image = pygame.image.load('./Scene_files/Images/trivia_box1.png')
        self.typewriter_input_head = TypewriterText(420, 210, 200, 100, "User Input", font=FONT_SMALL,colour=(0, 0, 0, 0))
        self.user_input = TextInput(420, 260, 300, 25)

        # Adjust these buttons to your needs for the second scene
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.75), GREEN, BLUE, "SUBMIT", BLACK, WHITE, self.back_to_scene_start
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "EXIT", BLACK, WHITE, sys.exit
        )

    def back_to_scene_start(self):
        self.manager.switch_scene(SceneStart(self.manager, self.game_clock))

    def handle_event(self, event):
        # for buttons
        self.button1.handle_event(event)
        self.button2.handle_event(event)
        # for keyboard entry to user input
        self.user_input.handle_event(event)

    def update(self):
        # Always update the typewriter_title
        self.typewriter_title.update()

        # stagger the typewriting
        if self.typewriter_title.completed:
            self.typewriter_display_head.update()
            self.typewriter_input_head.update()
        if self.typewriter_display_head.completed:
            self.typewriter_display.update()



    def draw(self, screen):
        screen.fill(GREY)
        screen.blit(self.display_bl_image, (30, 70))
        screen.blit(self.trivia_box1_image, (390, 190))
        self.typewriter_title.draw(screen)

        # Only draw stagger the typewriting
        if self.typewriter_title.completed:
            self.typewriter_display_head.draw(screen)
            self.typewriter_input_head.draw(screen)
        if self.typewriter_display_head.completed and self.typewriter_input_head.completed:
            self.typewriter_display.draw(screen)

        self.user_input.draw(screen)
        self.button1.draw(screen)
        self.button2.draw(screen)


########################################################################################################################
