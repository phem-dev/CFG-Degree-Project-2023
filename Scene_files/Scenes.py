import sys
import pygame
import Missions.Mission1_Asteroids

# Superclass and constants
from Scene_files.SceneManager import Scene
from settings import WHITE, BLACK, RED, GREEN, ORANGE, YELLOW, BLUE, PURPLE, L_PURPLE, TURQ, GREY, SCREEN_HEIGHT, SCREEN_WIDTH, FONT_TITLE, FONT_SMALL, FONT, FONT_VSMALL
# Mission classes
from Missions.Mission1_Asteroids import Challenge, Asteroids
# functional classes
from Scene_files.Typewriter import TypewriterText
from Scene_files.Button_files.Button import Button
from Scene_files.TextInput import TextInput
from Scene_files.background import *


########################################################################################################################
# START AND CONTROLS ###################################################################################################
########################################################################################################################

class SceneStart(Scene):
    # here we will pass the SceneManager class as an attribute to allow to change scene... eg. scene_manager.switch_scene(SceneStart(SceneManager()))  # start scene 1
    def __init__(self, manager, game_clock):
        # we call the superclass (Scene) init as this has the template for the mute/umute
        super().__init__()
        self.manager = manager
        self.game_clock = game_clock
        self.title = "Stratobus Missions"
        self.typewriter = TypewriterText(150, 120, 500, 500, self.title, FONT_TITLE, justify="center")
        self.draw_intro = False

        # here we define the things to be drawn by the draw method further down
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.72), GREEN, BLUE, "PLAY", BLACK, WHITE, self.to_mission_menu
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.84), ORANGE, BLUE, "EXIT", BLACK, WHITE, sys.exit
        )

        pygame.time.set_timer(pygame.USEREVENT + 1, 1000)  # This will trigger a USER EVENT after a set time. (the + 1 is used as ID for that USER EVENT in case there are more)

    # here we define some actions as functions to be called on button clicks
    def to_mission_menu(self):
        self.manager.switch_scene(SceneStartMenu(self.manager, self.game_clock))

    def to_controls(self):
        self.manager.switch_scene(SceneControls(self.manager, self.game_clock))

    # here we have an event handler, events are fed in using a while loop with "for event in pygame.event.get():" in the main game.py
    def handle_event(self, event):
        super().handle_event(event)
        # waiting for the timer USER EVENT to happen
        if event.type == pygame.USEREVENT + 1:
            self.draw_intro = True
        self.button1.handle_event(event)
        self.button2.handle_event(event)

    def update(self):
        #  if timer has finished
        if self.draw_intro:
            self.typewriter.update()

    def draw(self, screen):
        screen.fill([255, 255, 255])
        screen.blit(BackGround_home.image, BackGround_home.rect)
        #  if timer has finished
        if self.draw_intro:
            self.button1.draw(screen)
            self.button2.draw(screen)
            self.typewriter.draw(screen)

        # Call the base class's draw method to draw the mute/unmute buttons
        super().draw(screen)


########################################################################################################################


class SceneControls(Scene):
    def __init__(self, manager, game_clock):
        super().__init__()
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
        super().handle_event(event)
        self.button1.handle_event(event)
        self.button2.handle_event(event)

    def draw(self, screen):
        screen.fill(TURQ)
        self.button1.draw(screen)
        self.button2.draw(screen)
        super().draw(screen)


#######################################################################################################################

class SceneStartMenu(Scene):
    # here we will pass the SceneManager class as an attribute to allow to change scene... eg. scene_manager.switch_scene(SceneStart(SceneManager()))  # start scene 1
    def __init__(self, manager, game_clock):
        super().__init__()
        self.manager = manager
        self.game_clock = game_clock
        self.title = "Select a mission:"
        self.typewriter = TypewriterText(130, 20, 550, 500, self.title, justify="center")
        # self.typewriter = TypewriterText(50, 50, 500, 500, Challenge.greet(Challenge(self.title)), 100) #  to use in missions

        # here we define the things to be drawn byt the draw method further down
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.12), GREEN, BLUE, "1: Asteroid Challenge", BLACK, WHITE, self.to_scene_mission_asteroids
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.22), YELLOW, BLUE, "2: Satellite Images", BLACK, WHITE, self.to_scene_mission_sentinel
        )
        self.button3 = Button(
            "center", (SCREEN_HEIGHT * 0.32), GREEN, BLUE, "3: Capture Mars", BLACK, WHITE, self.to_scene_mission_mars
        )
        self.button4 = Button(
            "center", (SCREEN_HEIGHT * 0.42), YELLOW, BLUE, "4: Payload Mission", BLACK, WHITE, self.to_scene_payload
        )
        self.button5 = Button(
            "center", (SCREEN_HEIGHT * 0.52), GREEN, BLUE, "5: Locate ISS", BLACK, WHITE, self.to_scene_dodge
        )
        self.button6 = Button(
            "center", (SCREEN_HEIGHT * 0.62), YELLOW, BLUE, "6: Asteroid Dodge", BLACK, WHITE, self.to_scene_dodge
        )
        self.button7 = Button(
            "center", (SCREEN_HEIGHT * 0.72), GREEN, BLUE, "7: Quiz", BLACK, WHITE, self.to_scene_dodge
        )
        self.button8 = Button(
            "center", (SCREEN_HEIGHT * 0.84), ORANGE, BLUE, "EXIT", BLACK, WHITE, sys.exit
        )

    # here we define some actions as functions to be called on button clicks
    def to_scene_mission_asteroids(self):
        self.manager.switch_scene(SceneMissionAsteroids(self.manager, self.game_clock))

    def to_scene_mission_sentinel(self):
        self.manager.switch_scene(SceneMissionSentinel(self.manager, self.game_clock))

    def to_scene_mission_mars(self):
        self.manager.switch_scene(SceneMissionMars(self.manager, self.game_clock))

    def to_scene_payload(self):
        self.manager.switch_scene(SceneMissionPayload(self.manager, self.game_clock))

    def to_scene_dodge(self):
        self.manager.switch_scene(SceneMissionDodge(self.manager, self.game_clock))

    # here we have an event handler, events are fed in using a while loop with "for event in pygame.event.get():" in the main game.py

    def handle_event(self, event):
        super().handle_event(event)
        self.button1.handle_event(event)
        self.button2.handle_event(event)
        self.button3.handle_event(event)
        self.button4.handle_event(event)
        self.button5.handle_event(event)
        self.button6.handle_event(event)
        self.button7.handle_event(event)
        self.button8.handle_event(event)

    def update(self):
        self.typewriter.update()

    def draw(self, screen):
        screen.fill([255, 255, 255])
        screen.blit(BackGround_home.image, BackGround_home.rect)
        self.typewriter.draw(screen)
        self.button1.draw(screen)
        self.button2.draw(screen)
        self.button3.draw(screen)
        self.button4.draw(screen)
        self.button5.draw(screen)
        self.button6.draw(screen)
        self.button7.draw(screen)
        self.button8.draw(screen)
        super().draw(screen)


########################################################################################################################
# MISSIONS #############################################################################################################
########################################################################################################################
# ASTEROIDS

class SceneMissionAsteroids(Scene):
    def __init__(self, manager, game_clock):
        super().__init__()
        self.manager = manager
        self.game_clock = game_clock
        self.title = "Asteroid"
        self.block = "In this challenge you will track 3 asteroids and see how close they passed by Earth. |Report the data back to base to complete the mission!"
        self.typewriter_title = TypewriterText(130, 20, 550, 500, Challenge.greet(Challenge(self.title)), justify="center")
        self.typewriter_block = TypewriterText(150, 200, 430, 200, self.block, font=FONT_SMALL)
        self.mission_box_image = pygame.image.load('./Scene_files/Images/mission_box.png')

        # Adjust these buttons to your needs for the second scene
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.75), GREEN, BLUE, "ACCEPT", BLACK, WHITE, self.to_scene_mission_asteroids_input
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "EXIT", BLACK, WHITE, self.to_menu
        )

    def to_scene_mission_asteroids_input(self):
        self.manager.switch_scene(SceneMissionAsteroidsInput(self.manager, self.game_clock))

    def to_menu(self):
        self.manager.switch_scene(SceneStartMenu(self.manager, self.game_clock))

    def handle_event(self, event):
        super().handle_event(event)
        self.button1.handle_event(event)
        self.button2.handle_event(event)

    def update(self):
        # Always update the typewriter_title
        self.typewriter_title.update()

        # Only update typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.update()

    def draw(self, screen):
        screen.fill([255, 255, 255])
        screen.blit(BackGround_asteroid.image, BackGround_asteroid.rect)
        screen.blit(self.mission_box_image, (75, 120))
        self.typewriter_title.draw(screen)

        # Only draw typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.draw(screen)

        self.button1.draw(screen)
        self.button2.draw(screen)
        super().draw(screen)


########################################################################################################################

class SceneMissionAsteroidsInput(Scene):
    def __init__(self, manager, game_clock):
        super().__init__()
        self.manager = manager
        self.game_clock = game_clock

        # title
        self.title = "Asteroid Mission"
        self.typewriter_title = TypewriterText(130, 20, 550, 500, self.title, justify="center")

        # display text box
        self.display_bl_image = pygame.image.load('./Scene_files/Images/display_bl.png')
        self.typewriter_display_head = TypewriterText(55, 105, 200, 100, "Data Received", font=FONT_SMALL, colour=(0, 0, 0, 0))
        self.display_text1 = f"{Asteroids.asteroid_distance_prompt(Asteroids(self.title))}"
        self.display_text2 = f"{Asteroids.get_3_asteroid_data(Asteroids(self.title), Asteroids.get_all_asteroid_data(Asteroids(self.title)), Missions.Mission1_Asteroids.today_date_string)}"
        self.typewriter_display1 = TypewriterText(55, 170, 150, 300, self.display_text1, font=FONT_VSMALL, colour=(0, 0, 0, 0))
        self.typewriter_display2 = TypewriterText(55, 320, 150, 300, self.display_text2, font=FONT_SMALL, colour=(0, 0, 0, 0))

        # input box
        self.trivia_box1_image = pygame.image.load('./Scene_files/Images/trivia_box1.png')
        self.typewriter_input_head = TypewriterText(420, 210, 200, 100, "User Input", font=FONT_SMALL, colour=(0, 0, 0, 0))
        self.user_input = TextInput(420, 255, 300, 25)
        self.result_message = None
        self.attempts = 3
        self.click_sound = Button.click_sound

        # Adjust these buttons to your needs for the second scene
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.75), GREEN, BLUE, "SUBMIT", BLACK, WHITE, self.user_submit
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "EXIT", BLACK, WHITE, self.to_menu
        )
#

    def user_submit(self):
        # Get the current text input from the user using the user_answer method from TextInput
        player_input = self.user_input.user_answer()

        asteroid_challenge_instance = Asteroids(self.title)
        asteroid_data = asteroid_challenge_instance.get_all_asteroid_data()
        asteroid_distances = asteroid_challenge_instance.get_3_asteroid_data(asteroid_data, Missions.Mission1_Asteroids.today_date_string)

        # Call the player_enter_asteroid_distance function
        result_message, remaining_attempts = asteroid_challenge_instance.player_enter_asteroid_distance(asteroid_distances, player_input, self.attempts)
        self.attempts = remaining_attempts
        # Create a TypewriterText instance with the result and assign it to result_message
        self.result_message = TypewriterText(420, 285, 300, 300, result_message, font=FONT_VSMALL, colour=(0, 0, 0, 0))
        if result_message == asteroid_challenge_instance.success():
            self.button1 = Button(
                "center", (SCREEN_HEIGHT * 0.75), GREEN, BLUE, "PROCEED", BLACK, WHITE, self.to_scene_mission_sentinel
            )
        elif result_message == asteroid_challenge_instance.fail_message:
            self.button1 = Button(
                           "center", (SCREEN_HEIGHT * 1.1), GREEN, BLUE, "", BLACK, WHITE, None
            )



    def back_to_scene_start(self):
        self.manager.switch_scene(SceneStart(self.manager, self.game_clock))

    def to_menu(self):
        self.manager.switch_scene(SceneStartMenu(self.manager, self.game_clock))

    def to_scene_mission_sentinel(self):
        self.manager.switch_scene(SceneMissionSentinel(self.manager, self.game_clock))

    def handle_event(self, event):
        super().handle_event(event)
        # for buttons
        self.button1.handle_event(event)
        self.button2.handle_event(event)
        # for keyboard entry to user input
        self.user_input.handle_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                self.click_sound.play()
                self.user_submit()


    def update(self):
        # Always update the typewriter_title
        self.typewriter_title.update()

        # stagger the typewriting
        if self.typewriter_title.completed:
            self.typewriter_display_head.update()
            self.typewriter_input_head.update()
        if self.typewriter_display_head.completed:
            self.typewriter_display1.update()
        if self.typewriter_display1.completed:
            self.typewriter_display2.update()

        #  if the result message has been made by the user pressing the submit button
        if self.result_message:
            self.result_message.update()

    def draw(self, screen):
        screen.fill([255, 255, 255])
        screen.blit(BackGround_asteroid.image, BackGround_asteroid.rect)
        screen.blit(self.display_bl_image, (30, 70))
        screen.blit(self.trivia_box1_image, (390, 190))
        self.typewriter_title.draw(screen)

        # Only draw stagger the typewriting
        if self.typewriter_title.completed:
            self.typewriter_display_head.draw(screen)
            self.typewriter_input_head.draw(screen)
        if self.typewriter_display_head.completed and self.typewriter_input_head.completed:
            self.typewriter_display1.draw(screen)
        if self.typewriter_display1.completed:
            self.typewriter_display2.draw(screen)

        self.user_input.draw(screen)
        self.button1.draw(screen)
        self.button2.draw(screen)

        # Draw the result_message if it's not None
        if self.result_message:
            self.result_message.draw(screen)
        super().draw(screen)


########################################################################################################################
########################################################################################################################
# Mission 2: Sentinel

class SceneMissionSentinel(Scene):
    def __init__(self, manager, game_clock):
        super().__init__()
        self.manager = manager
        self.game_clock = game_clock
        self.title = "Earth Satellite Imaging"
        self.block = "In this challenge you will take aerial photographs of Earth.  What does your house look like from above? "
        self.typewriter_title = TypewriterText(130, 20, 550, 500, Challenge.greet(Challenge(self.title)), justify="center")
        self.typewriter_block = TypewriterText(150, 200, 430, 200, self.block, font=FONT_SMALL)
        self.mission_box_image = pygame.image.load('./Scene_files/Images/mission_box.png')

        # Adjust these buttons to your needs for the second scene
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.75), GREEN, BLUE, "ACCEPT", BLACK, WHITE, self.to_scene_mission_asteroids_input
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "EXIT", BLACK, WHITE, self.to_menu
        )

    def to_scene_mission_asteroids_input(self):
        self.manager.switch_scene(SceneMissionAsteroidsInput(self.manager, self.game_clock))

    def to_menu(self):
        self.manager.switch_scene(SceneStartMenu(self.manager, self.game_clock))

    def handle_event(self, event):
        super().handle_event(event)
        self.button1.handle_event(event)
        self.button2.handle_event(event)

    def update(self):
        # Always update the typewriter_title
        self.typewriter_title.update()

        # Only update typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.update()

    def draw(self, screen):
        screen.fill([255, 255, 255])
        screen.blit(BackGround_sentinel.image, BackGround_sentinel.rect)
        screen.blit(self.mission_box_image, (75, 120))
        self.typewriter_title.draw(screen)

        # Only draw typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.draw(screen)

        self.button1.draw(screen)
        self.button2.draw(screen)
        super().draw(screen)


########################################################################################################################
########################################################################################################################
# Mission 3: Mars

class SceneMissionMars(Scene):
    def __init__(self, manager, game_clock):
        super().__init__()
        self.manager = manager
        self.game_clock = game_clock
        self.title = "Mars"
        self.block = "In this mission you can take control of the Mars Rover and take photos of Mars!"
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
        super().handle_event(event)
        self.button1.handle_event(event)
        self.button2.handle_event(event)

    def update(self):
        # Always update the typewriter_title
        self.typewriter_title.update()

        # Only update typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.update()

    def draw(self, screen):
        screen.fill([255, 255, 255])
        screen.blit(BackGround_mars.image, BackGround_mars.rect)
        screen.blit(self.mission_box_image, (75, 120))
        self.typewriter_title.draw(screen)

        # Only draw typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.draw(screen)

        self.button1.draw(screen)
        self.button2.draw(screen)
        super().draw(screen)

########################################################################################################################


class SceneMissionMarsInput(Scene):
    def __init__(self, manager, game_clock):
        super().__init__()
        self.manager = manager
        self.game_clock = game_clock

        # title
        self.title = "Capture Mars"
        self.typewriter_title = TypewriterText(130, 20, 550, 500, self.title, justify="center")

        # display text box
        self.display_bl_image = pygame.image.load('./Scene_files/Images/display_bl.png')
        self.typewriter_display_head = TypewriterText(55, 105, 200, 100, "Data Received", font=FONT_SMALL, colour=(0, 0, 0, 0))
        self.display_text1 = f"{Asteroids.asteroid_distance_prompt(Asteroids(self.title))}"
        self.display_text2 = f"{Asteroids.get_3_asteroid_data(Asteroids(self.title), Asteroids.get_all_asteroid_data(Asteroids(self.title)), Missions.Mission1_Asteroids.today_date_string)}"
        self.typewriter_display1 = TypewriterText(55, 170, 150, 300, self.display_text1, font=FONT_VSMALL, colour=(0, 0, 0, 0))
        self.typewriter_display2 = TypewriterText(55, 320, 150, 300, self.display_text2, font=FONT_SMALL, colour=(0, 0, 0, 0))

        # input box
        self.trivia_box1_image = pygame.image.load('./Scene_files/Images/trivia_box1.png')
        self.typewriter_input_head = TypewriterText(420, 210, 200, 100, "User Input", font=FONT_SMALL, colour=(0, 0, 0, 0))
        self.user_input = TextInput(420, 255, 300, 25)
        self.result_message = None
        self.attempts = 3

        # Adjust these buttons to your needs for the second scene
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.75), GREEN, BLUE, "SUBMIT", BLACK, WHITE, self.user_submit
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "EXIT", BLACK, WHITE, self.to_menu
        )
#

    def user_submit(self):
        # Get the current text input from the user using the user_answer method from TextInput
        player_input = self.user_input.user_answer()

        asteroid_challenge_instance = Asteroids(self.title)
        asteroid_data = asteroid_challenge_instance.get_all_asteroid_data()
        asteroid_distances = asteroid_challenge_instance.get_3_asteroid_data(asteroid_data, Missions.Mission1_Asteroids.today_date_string)

        # Call the player_enter_asteroid_distance function
        result_message, remaining_attempts = asteroid_challenge_instance.player_enter_asteroid_distance(asteroid_distances, player_input, self.attempts)
        self.attempts = remaining_attempts
        # Create a TypewriterText instance with the result and assign it to result_message
        self.result_message = TypewriterText(420, 285, 300, 300, result_message, font=FONT_VSMALL, colour=(0, 0, 0, 0))
        if result_message == asteroid_challenge_instance.success():
            self.button1 = Button(
                "center", (SCREEN_HEIGHT * 0.75), GREEN, BLUE, "PROCEED", BLACK, WHITE, self.to_scene_mission_sentinel
            )
        elif result_message == asteroid_challenge_instance.fail_message:
            self.button1 = Button(
                           "center", (SCREEN_HEIGHT * 1.1), GREEN, BLUE, "", BLACK, WHITE, None
            )

    def back_to_scene_start(self):
        self.manager.switch_scene(SceneStart(self.manager, self.game_clock))

    def to_menu(self):
        self.manager.switch_scene(SceneStartMenu(self.manager, self.game_clock))

    def to_scene_mission_sentinel(self):
        self.manager.switch_scene(SceneMissionSentinel(self.manager, self.game_clock))

    def handle_event(self, event):
        super().handle_event(event)
        # for buttons
        self.button1.handle_event(event)
        self.button2.handle_event(event)
        # for keyboard entry to user input
        if event.type == pygame.K_RETURN or event.type == pygame.K_KP_ENTER:
            self.user_submit()
        self.user_input.handle_event(event)


    def update(self):
        # Always update the typewriter_title
        self.typewriter_title.update()

        # stagger the typewriting
        if self.typewriter_title.completed:
            self.typewriter_display_head.update()
            self.typewriter_input_head.update()
        if self.typewriter_display_head.completed:
            self.typewriter_display1.update()
        if self.typewriter_display1.completed:
            self.typewriter_display2.update()

        #  if the result message has been made by the user pressing the submit button
        if self.result_message:
            self.result_message.update()

    def draw(self, screen):
        screen.fill([255, 255, 255])
        screen.blit(BackGround_asteroid.image, BackGround_asteroid.rect)
        screen.blit(self.display_bl_image, (30, 70))
        screen.blit(self.trivia_box1_image, (390, 190))
        self.typewriter_title.draw(screen)

        # Only draw stagger the typewriting
        if self.typewriter_title.completed:
            self.typewriter_display_head.draw(screen)
            self.typewriter_input_head.draw(screen)
        if self.typewriter_display_head.completed and self.typewriter_input_head.completed:
            self.typewriter_display1.draw(screen)
        if self.typewriter_display1.completed:
            self.typewriter_display2.draw(screen)

        self.user_input.draw(screen)
        self.button1.draw(screen)
        self.button2.draw(screen)

        # Draw the result_message if it's not None
        if self.result_message:
            self.result_message.draw(screen)
        super().draw(screen)


########################################################################################################################
#######################################################################################################################
# Mission 4: Payload

class SceneMissionPayload(Scene):
    def __init__(self, manager, game_clock):
        super().__init__()
        self.manager = manager
        self.game_clock = game_clock
        self.title = "Payload"
        self.block = "In this challenge you will track 3 asteroids and see how close they passed by Earth. Report the data back to base to complete the mission!"
        self.typewriter_title = TypewriterText(130, 20, 550, 500, Challenge.greet(Challenge(self.title)), justify="center")
        self.typewriter_block = TypewriterText(150, 200, 430, 200, self.block, font=FONT_SMALL)
        self.mission_box_image = pygame.image.load('./Scene_files/Images/mission_box.png')

        # Adjust these buttons to your needs for the second scene
        self.button1 = Button(
            "left", (SCREEN_HEIGHT * 0.85), GREEN, BLUE, "ACCEPT", BLACK, WHITE, self.to_scene_mission_asteroids_input
        )
        self.button2 = Button(
        "center", (SCREEN_HEIGHT * 0.75), YELLOW, BLUE, "CONTROLS", BLACK, WHITE, self.to_controls
        )
        self.button3 = Button(
            600, (SCREEN_HEIGHT * 0.85), ORANGE, BLUE, "EXIT", BLACK, WHITE, self.to_menu
        )

    def to_scene_mission_asteroids_input(self):
        self.manager.switch_scene(SceneMissionAsteroidsInput(self.manager, self.game_clock))

    def to_controls(self):
        self.manager.switch_scene(SceneControls(self.manager, self.game_clock))

    def to_menu(self):
        self.manager.switch_scene(SceneStartMenu(self.manager, self.game_clock))

    def handle_event(self, event):
        super().handle_event(event)
        self.button1.handle_event(event)
        self.button2.handle_event(event)
        self.button3.handle_event(event)

    def update(self):
        # Always update the typewriter_title
        self.typewriter_title.update()

        # Only update typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.update()

    def draw(self, screen):
        screen.fill([255, 255, 255])
        screen.blit(BackGround_payload.image, BackGround_payload.rect)
        screen.blit(self.mission_box_image, (75, 120))
        self.typewriter_title.draw(screen)

        # Only draw typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.draw(screen)

        self.button1.draw(screen)
        self.button2.draw(screen)
        self.button3.draw(screen)
        super().draw(screen)


########################################################################################################################
#######################################################################################################################
# Mission 5: Asteroid dodge

class SceneMissionDodge(Scene):
    def __init__(self, manager, game_clock):
        super().__init__()
        self.manager = manager
        self.game_clock = game_clock
        self.title = "Asteroid"
        self.block = "In this challenge you will track 3 asteroids and see how close they passed by Earth. Report the data back to base to complete the mission!"
        self.typewriter_title = TypewriterText(130, 20, 550, 500, Challenge.greet(Challenge(self.title)), justify="center")
        self.typewriter_block = TypewriterText(150, 200, 430, 200, self.block, font=FONT_SMALL)
        self.mission_box_image = pygame.image.load('./Scene_files/Images/mission_box.png')

        # Adjust these buttons to your needs for the second scene
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.75), GREEN, BLUE, "ACCEPT", BLACK, WHITE, self.to_scene_mission_asteroid_dodge_game
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "EXIT", BLACK, WHITE, self.to_menu
        )

    def to_scene_mission_asteroid_dodge_game(self):
        self.manager.switch_scene(SceneMissionDodgeGame(self.manager, self.game_clock))

    def to_menu(self):
        self.manager.switch_scene(SceneStartMenu(self.manager, self.game_clock))

    def handle_event(self, event):
        super().handle_event(event)
        self.button1.handle_event(event)
        self.button2.handle_event(event)

    def update(self):
        # Always update the typewriter_title
        self.typewriter_title.update()

        # Only update typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.update()

    def draw(self, screen):
        screen.fill([255, 255, 255])
        screen.blit(BackGround_asteroid.image, BackGround_asteroid.rect)
        screen.blit(self.mission_box_image, (75, 120))
        self.typewriter_title.draw(screen)

        # Only draw typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.draw(screen)

        self.button1.draw(screen)
        self.button2.draw(screen)
        super().draw(screen)


########################################################################################################################
# Mission 7: dodge game


class SceneMissionDodgeGame(Scene):
    def __init__(self, manager, game_clock):
        super().__init__()
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
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "EXIT", BLACK, WHITE, self.to_menu
        )

    def to_scene_mission_asteroids_input(self):
        self.manager.switch_scene(SceneMissionAsteroidsInput(self.manager, self.game_clock))

    def to_menu(self):
        self.manager.switch_scene(SceneStartMenu(self.manager, self.game_clock))

    def handle_event(self, event):
        super().handle_event(event)
        self.button1.handle_event(event)
        self.button2.handle_event(event)

    def update(self):
        # Always update the typewriter_title
        self.typewriter_title.update()

        # Only update typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.update()

    def draw(self, screen):
        screen.fill([255, 255, 255])
        screen.blit(BackGround_asteroid.image, BackGround_asteroid.rect)
        screen.blit(self.mission_box_image, (75, 120))
        self.typewriter_title.draw(screen)

        # Only draw typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.draw(screen)

        self.button1.draw(screen)
        self.button2.draw(screen)
        super().draw(screen)

########################################################################################################################
########################################################################################################################