import sys
import Missions.Mission1_Asteroids
import Missions.quiz_SQLite.quiz
import subprocess


# Superclass and constants
from Scene_files.SceneManager import Scene

from settings import *
# Mission classes
from Missions.Mission1_Asteroids import Challenge, Asteroids
from Missions.quiz_SQLite.quiz import QuizGame
# functional classes
from Utils.Typewriter import TypewriterText
from Utils.Button import Button
from Utils.TextInput import TextInput
from Scene_files.background import *


########################################################################################################################
# START AND CONTROLS ###################################################################################################
########################################################################################################################

class SceneStart(Scene):
    # Here we will pass the SceneManager class as an attribute to allow to change scene... e.g. scene_manager.switch_scene(SceneStart(SceneManager()))  # start scene 1
    def __init__(self, manager, game_clock):
        # Call the superclass (Scene) init as this has the template for the mute/unmute
        super().__init__()
        # Store the SceneManager and game clock
        self.manager = manager
        self.game_clock = game_clock
        # Title for the scene
        self.title = "Stratobus Missions"
        # Create a typewriter text for the title
        self.typewriter = TypewriterText(150, 120, 500, 500, self.title, FONT_TITLE, justify="center")
        self.draw_intro = False

        # Create buttons for the scene - here we define the things to be drawn by the draw method further down
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.72), GREEN, BLUE, "PLAY", BLACK, WHITE, self.to_mission_menu
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.84), ORANGE, BLUE, "EXIT", BLACK, WHITE, sys.exit
        )

        pygame.time.set_timer(pygame.USEREVENT + 1,
                              1000)  # This will trigger a USER EVENT after a set time. (the + 1 is used as ID for that USER EVENT in case there are more)

    # Actions as functions to be called on button clicks
    def to_mission_menu(self):
        self.manager.switch_scene(SceneStartMenu(self.manager, self.game_clock))

    def to_controls(self):
        self.manager.switch_scene(SceneControls(self.manager, self.game_clock))

    # Here we have an event handler, events are fed in using a while loop with "for event in pygame.event.get():" in the main game.py
    def handle_event(self, event):
        super().handle_event(event)
        # Waiting for the timer USER EVENT to happen
        if event.type == pygame.USEREVENT + 1:
            self.draw_intro = True
        self.button1.handle_event(event)
        self.button2.handle_event(event)

    def update(self):
        # Update the scene's elements - if timer has finished, update the typewriter effect
        if self.draw_intro:
            self.typewriter.update()

    def draw(self, screen):
        # Draw the scene's elements on the screen

        # Fill the screen with a white background and draw background image
        # If the timer has finished, draw buttons and typewriter text
        # Finally, call the base class's draw method for additional UI elements
        screen.fill([255, 255, 255])
        screen.blit(BackGround_home.image, BackGround_home.rect)
        # If timer has finished, draw buttons and typewriter text
        if self.draw_intro:
            self.button1.draw(screen)
            self.button2.draw(screen)
            self.typewriter.draw(screen)

        # Call the base class's draw method to draw the mute/unmute buttons
        super().draw(screen)


########################################################################################################################


class SceneControls(Scene):
    # Initialise the scene for controls menu
    def __init__(self, manager, game_clock):
        super().__init__()
        self.manager = manager
        self.game_clock = game_clock

        # Create buttons for the controls menu
        # Adjust these buttons to your needs for the second scene
        self.button1 = Button(
            "right", (SCREEN_HEIGHT * 0.6), GREY, BLUE, "BACK", BLACK, WHITE, self.back_to_scene_start
        )
        self.button2 = Button(
            "right", (SCREEN_HEIGHT * 0.72), ORANGE, BLUE, "EXIT", BLACK, WHITE, sys.exit
        )

    def back_to_scene_start(self):
        # Switch to the starting scene
        self.manager.switch_scene(SceneStart(self.manager, self.game_clock))

    def handle_event(self, event):
        # Handle events specific to the controls menu scene
        super().handle_event(event)
        self.button1.handle_event(event)
        self.button2.handle_event(event)

    def draw(self, screen):
        # Draw the controls menu scene
        screen.fill(TURQ)
        self.button1.draw(screen)
        self.button2.draw(screen)
        # Call the base class's draw method to draw additional UI elements
        super().draw(screen)


#######################################################################################################################

class SceneStartMenu(Scene):
    # Here we will pass the SceneManager class as an attribute to allow to change scene... eg. scene_manager.switch_scene(SceneStart(SceneManager()))  #Start scene 1
    def __init__(self, manager, game_clock):
        # Call the superclass (Scene)
        super().__init__()
        # Store the SceneManager and game clock
        self.manager = manager
        self.game_clock = game_clock
        # Title for the scene
        self.title = "Select a mission:"
        # Create a typewriter text for the title
        self.typewriter = TypewriterText(130, 20, 550, 500, self.title, justify="center")
        # self.typewriter = TypewriterText(50, 50, 500, 500, Challenge.greet(Challenge(self.title)), 100) #  to use in missions

        # Define buttons for different missions

        # Button for Asteroid Challenge
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.12), GREEN, BLUE, "1: Asteroid Challenge", BLACK, WHITE,
            self.to_scene_mission_asteroids
        )
        # Button for Satellite Images
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.22), YELLOW, BLUE, "2: Satellite Images", BLACK, WHITE,
            self.to_scene_mission_sentinel
        )
        # Button for Capture Mars
        self.button3 = Button(
            "center", (SCREEN_HEIGHT * 0.32), GREEN, BLUE, "3: Capture Mars", BLACK, WHITE, self.to_scene_mission_mars
        )
        # Button for Payload Mission
        self.button4 = Button(
            "center", (SCREEN_HEIGHT * 0.42), YELLOW, BLUE, "4: Payload Mission", BLACK, WHITE, self.to_scene_payload
        )
        # Button for Locate ISS
        self.button5 = Button(
            "center", (SCREEN_HEIGHT * 0.52), GREEN, BLUE, "5: Locate ISS", BLACK, WHITE, self.to_scene_iss
        )
        # Button for Asteroid Dodge
        self.button6 = Button(
            "center", (SCREEN_HEIGHT * 0.62), YELLOW, BLUE, "6: Asteroid Dodge", BLACK, WHITE, self.to_scene_dodge
        )
        # Button for Quiz
        self.button7 = Button(
            "center", (SCREEN_HEIGHT * 0.72), GREEN, BLUE, "7: Quiz", BLACK, WHITE, self.to_scene_quiz
        )
        # Button for exiting the game
        self.button8 = Button(
            "center", (SCREEN_HEIGHT * 0.84), ORANGE, BLUE, "EXIT", BLACK, WHITE, sys.exit
        )

    # Actions defined as functions to be called on button clicks
    def to_scene_mission_asteroids(self):
        self.manager.switch_scene(SceneMissionAsteroids(self.manager, self.game_clock))

    def to_scene_mission_sentinel(self):
        self.manager.switch_scene(SceneMissionSentinel(self.manager, self.game_clock))

    def to_scene_mission_mars(self):
        self.manager.switch_scene(SceneMissionMars(self.manager, self.game_clock))

    def to_scene_payload(self):
        self.manager.switch_scene(SceneMissionPayload(self.manager, self.game_clock))

    def to_scene_iss(self):
        self.manager.switch_scene(SceneMissionISS(self.manager, self.game_clock))

    def to_scene_dodge(self):
        self.manager.switch_scene(SceneMissionDodge(self.manager, self.game_clock))

    def to_scene_quiz(self):
        self.manager.switch_scene(SceneQuiz(self.manager, self.game_clock))

    # here we have an event handler, events are fed in using a while loop with "for event in pygame.event.get():" in the main game.py

    # Handle events for the scene
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

        # Update the scene's elements

    def update(self):
        # Update the typewriter effect
            self.typewriter.update()

        # Draw the scene's elements on the screen
        # Fill the screen with a white background and draw background image
        # If the timer has finished, draw buttons and typewriter text
        # Finally, call the base class's draw method for additional UI elements

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
# Mission 1 : Asteroids Mission

class SceneMissionAsteroids(Scene):
    # This class represents the mission scene for the Asteroid Challenge
    def __init__(self, manager, game_clock):
        # Initialise the Asteroid Challenge mission scene.
        # Call the superclass (Scene)
        super().__init__()
        # Store the SceneManager and game clock
        self.manager = manager
        self.game_clock = game_clock
        # Title for the scene
        self.title = "Asteroid"
        self.block = "In this challenge you will access the NASA API to track 3 asteroids and see how close they passed by Earth. |Report the data back to base to complete the mission!"
        self.typewriter_title = TypewriterText(130, 20, 550, 500, Challenge.greet(Challenge(self.title)),
                                               justify="center")
        self.typewriter_block = TypewriterText(150, 200, 430, 200, self.block, font=FONT_SMALL)
        # Load and store the mission box image
        self.mission_box_image = pygame.image.load('./Scene_files/Images/mission_box.png')

        # Define buttons for mission operations
        # Adjust these buttons to your needs for the second scene
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.75), GREEN, BLUE, "ACCEPT", BLACK, WHITE, self.to_scene_mission_asteroids_input
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "MENU", BLACK, WHITE, self.to_menu
        )

    def to_scene_mission_asteroids_input(self):
        # Switch to the Asteroid Mission Input scene
        self.manager.switch_scene(SceneMissionAsteroidsInput(self.manager, self.game_clock))

    def to_menu(self):
        # Switch to the Start Menu scene
        self.manager.switch_scene(SceneStartMenu(self.manager, self.game_clock))

    def handle_event(self, event):
        # Handle events for the scene
        super().handle_event(event)
        self.button1.handle_event(event)
        self.button2.handle_event(event)

    # Update the scene's elements
    # Update the typewriter's title
    # Update the typewriter block if typewriter title has completed
    def update(self):
        # Always update the typewriter_title
        self.typewriter_title.update()

        # Only update typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.update()

    # Draw the scene's elements on the screen
    # Fill the screen with a white background and draw background image
    # Draw typewriter title, typewriter block, buttons, and additional UI elements
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

# This class represents the scene where players enter data for the Asteroid Mission
class SceneMissionAsteroidsInput(Scene):
    def __init__(self, manager, game_clock):
        # Initialise the Asteroid Mission Input scene
        # Call the superclass (Scene)
        super().__init__()
        # Store the SceneManager and game clock
        self.manager = manager
        self.game_clock = game_clock

        # Title for the scene
        self.title = "Asteroid Mission"
        # Create typewriter text for the title
        self.typewriter_title = TypewriterText(130, 20, 550, 500, self.title, justify="center")
        self.asteroid_instance = Asteroids(self.title)

        # Display text box elements
        self.display_bl_image = pygame.image.load('./Scene_files/Images/display_bl.png')
        self.typewriter_display_head = TypewriterText(55, 105, 200, 100, "Data Received", font=FONT_SMALL,
                                                      colour=(0, 0, 0, 0))
        self.display_text1 = f"{self.asteroid_instance.asteroid_distance_prompt()}"
        self.display_text2 = f"{Asteroids.get_3_asteroid_data(Asteroids(self.title), self.asteroid_instance.get_all_asteroid_data(), Missions.Mission1_Asteroids.today_date_string)[0]}"
        self.typewriter_display1 = TypewriterText(55, 170, 150, 300, self.display_text1, font=FONT_VSMALL,
                                                  colour=(0, 0, 0, 0))
        self.typewriter_display2 = TypewriterText(55, 320, 150, 300, self.display_text2, font=FONT_SMALL,
                                                  colour=(0, 0, 0, 0))

        # Input box elements
        self.trivia_box1_image = pygame.image.load('./Scene_files/Images/trivia_box1.png')
        self.typewriter_input_head = TypewriterText(420, 210, 200, 100, "User Input", font=FONT_SMALL,
                                                    colour=(0, 0, 0, 0))
        self.user_input = TextInput(420, 255, 300, 25)
        self.result_message = None
        self.attempts = 3
        self.click_sound = Button.click_sound

        # Adjust these buttons to your needs for the second scene
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.75), GREEN, BLUE, "SUBMIT", BLACK, WHITE, self.user_submit
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "MENU", BLACK, WHITE, self.to_menu
        )

    #

    def user_submit(self):
        # Get the current text input from the user using the user_answer method from TextInput
        player_input = self.user_input.user_answer()

        asteroid_data = self.asteroid_instance.get_all_asteroid_data()
        asteroid_distances = \
        self.asteroid_instance.get_3_asteroid_data(asteroid_data, Missions.Mission1_Asteroids.today_date_string)[1]

        # Call the player_enter_asteroid_distance function
        result_message, self.attempts = self.asteroid_instance.player_enter_asteroid_distance(asteroid_distances,
                                                                                              player_input,
                                                                                              self.attempts)
        self.user_input.text = ""
        # Create a TypewriterText instance with the result and assign it to result_message
        self.result_message = TypewriterText(420, 285, 300, 300, result_message, font=FONT_VSMALL, colour=(0, 0, 0, 0))

        if result_message == self.asteroid_instance.success():
            self.button1 = Button(
                "center", (SCREEN_HEIGHT * 0.75), GREEN, BLUE, "PROCEED", BLACK, WHITE, self.to_scene_mission_sentinel
            )
        elif result_message == self.asteroid_instance.fail():
            self.button1 = Button(
                "center", (SCREEN_HEIGHT * 1.1), GREEN, BLUE, "", BLACK, WHITE, None
            )

    # Switch to the Start scene
    def back_to_scene_start(self):
        self.manager.switch_scene(SceneStart(self.manager, self.game_clock))

        # Switch to the Start Menu scene

    def to_menu(self):
        self.manager.switch_scene(SceneStartMenu(self.manager, self.game_clock))

        # Switch to the Sentinel Mission scene

    def to_scene_mission_sentinel(self):
        self.manager.switch_scene(SceneMissionSentinel(self.manager, self.game_clock))

        # Handle events for the scene

    def handle_event(self, event):
        super().handle_event(event)
        # Handle events for buttons
        self.button1.handle_event(event)
        self.button2.handle_event(event)
        # Handle events for keyboard entry to user input
        self.user_input.handle_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                self.click_sound.play()
                self.user_submit()

        # Update the scene's elements
        # Update the typewriter title
        # Stagger the typewriter effect for different text segments
        # Update the result message if it exists

    def update(self):
        # Always update the typewriter_title
        self.typewriter_title.update()

        # Stagger the typewriting
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
        # Draw the scene's elements on the screen
        # Fill the screen with a white background and draw background image
        # Draw typewriter title, staggered typewriter text segments, buttons, user input, and result message
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
    # This class represents the Sentinel Mission scene
    def __init__(self, manager, game_clock):
        # Initialise the Sentinel Mission scene
        # Call the superclass (Scene)
        super().__init__()
        # Store the SceneManager and game clock
        self.manager = manager
        self.game_clock = game_clock
        # Title for the scene
        self.title = "Earth Satellite Imaging"
        self.block = "In this challenge you will take aerial photographs of Earth.  What does your house look like from above? "
        # Create typewriter text for title and mission description
        self.typewriter_title = TypewriterText(130, 20, 550, 500, Challenge.greet(Challenge(self.title)), font = FONT,
                                               justify="center")
        self.typewriter_block = TypewriterText(150, 200, 430, 200, self.block, font=FONT_SMALL)
        # Load and store the mission box image
        self.mission_box_image = pygame.image.load('./Scene_files/Images/mission_box.png')

        # Adjust these buttons to your needs for the second scene
        # Define buttons for mission options
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.75), GREEN, BLUE, "ACCEPT", BLACK, WHITE, self.to_scene_mission_sentinel_play
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "MENU", BLACK, WHITE, self.to_menu
        )

    def to_scene_mission_sentinel_play(self):
        self.manager.switch_scene(SceneMissionSentinelPlay(self.manager, self.game_clock))

    def to_menu(self):
        self.manager.switch_scene(SceneStartMenu(self.manager, self.game_clock))

    def handle_event(self, event):
        super().handle_event(event)
        self.button1.handle_event(event)
        self.button2.handle_event(event)

    def update(self):
        # Always update the typewriter title
        # Only update the typewriter block if typewriter title has completed
        self.typewriter_title.update()

        # Only update typewriter_block if typewriter title has completed
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
class SceneMissionSentinelPlay(Scene):
    # This class represents the Sentinel Mission scene
    def __init__(self, manager, game_clock):
        # Initialise the Sentinel Mission scene
        # Call the superclass (Scene)
        super().__init__()
        # Store the SceneManager and game clock
        self.manager = manager
        self.game_clock = game_clock
        # Title for the scene
        self.title = "Earth Satellite Imaging Mission"
        self.block = ""
        # Create typewriter text for title and mission description
        self.typewriter_title = TypewriterText(130, 20, 550, 500, self.title,
                                               justify="center")
        self.typewriter_block = TypewriterText(150, 200, 430, 200, self.block, font=FONT_SMALL)
        # Load and store the mission box image
        self.mission_box_image = pygame.image.load('./Scene_files/Images/mission_box.png')

        # Adjust these buttons to your needs for the second scene
        # Define buttons for mission options

        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "MENU", BLACK, WHITE, self.to_menu
        )


    def to_menu(self):
        self.manager.switch_scene(SceneStartMenu(self.manager, self.game_clock))

    def handle_event(self, event):
        super().handle_event(event)
        self.button1.handle_event(event)


    def update(self):
        # Always update the typewriter title
        # Only update the typewriter block if typewriter title has completed
        self.typewriter_title.update()

        # Only update typewriter_block if typewriter title has completed
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
        self.typewriter_title = TypewriterText(200, 20, 400, 500, Challenge.greet(Challenge(self.title)), font = FONT,
                                               justify="center")
        self.typewriter_block = TypewriterText(150, 200, 430, 200, self.block, font=FONT_SMALL)
        self.mission_box_image = pygame.image.load('./Scene_files/Images/mission_box.png')

        # Adjust these buttons to your needs for the second scene
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.75), GREEN, BLUE, "ACCEPT", BLACK, WHITE, self.to_scene_mission_mars_play
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "MENU", BLACK, WHITE, self.to_menu
        )

    def to_scene_mission_mars_play(self):
        self.manager.switch_scene(SceneMissionMarsPlay(self.manager, self.game_clock))

    def to_menu(self):
        self.manager.switch_scene(SceneStartMenu(self.manager, self.game_clock))

    def handle_event(self, event):
        super().handle_event(event)
        self.button1.handle_event(event)
        self.button2.handle_event(event)

    def update(self):
        # Always update the typewriter title
        self.typewriter_title.update()

        # Only update typewriter_block if typewriter title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.update()

    def draw(self, screen):
        screen.fill([255, 255, 255])
        screen.blit(BackGround_mars.image, BackGround_mars.rect)
        screen.blit(self.mission_box_image, (75, 120))
        self.typewriter_title.draw(screen)

        # Only draw typewriter_block if typewriter title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.draw(screen)

        self.button1.draw(screen)
        self.button2.draw(screen)
        super().draw(screen)


########################################################################################################################


class SceneMissionMarsPlay(Scene):
    def __init__(self, manager, game_clock):
        super().__init__()
        self.manager = manager
        self.game_clock = game_clock
        self.title = "Capture Mars Mission"
        self.block = ""
        self.typewriter_title = TypewriterText(200, 20, 400, 500, self.title,
                                               justify="center")
        self.typewriter_block = TypewriterText(150, 200, 430, 200, self.block, font=FONT_SMALL)
        self.mission_box_image = pygame.image.load('./Scene_files/Images/mission_box.png')

        # Adjust these buttons to your needs for the second scene

        self.button1= Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "MENU", BLACK, WHITE, self.to_menu
        )

    def to_menu(self):
        self.manager.switch_scene(SceneStartMenu(self.manager, self.game_clock))

    def handle_event(self, event):
        super().handle_event(event)
        self.button1.handle_event(event)


    def update(self):
        # Always update the typewriter title
        self.typewriter_title.update()

        # Only update typewriter_block if typewriter title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.update()

    def draw(self, screen):
        screen.fill([255, 255, 255])
        screen.blit(BackGround_mars.image, BackGround_mars.rect)
        screen.blit(self.mission_box_image, (75, 120))
        self.typewriter_title.draw(screen)

        # Only draw typewriter_block if typewriter title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.draw(screen)

        self.button1.draw(screen)
        super().draw(screen)

########################################################################################################################
#######################################################################################################################
# Mission 4: Payload
class SceneMissionPayload(Scene):
    def __init__(self, manager, game_clock):
        super().__init__()
        self.manager = manager
        self.game_clock = game_clock
        self.title = "Payload Challenge"
        self.block = "Play the stratobus tetris game!"
        self.typewriter_title = TypewriterText(130, 6, 550, 500, Challenge.greet(Challenge(self.title)),
                                               justify="center")
        self.typewriter_block = TypewriterText(150, 200, 430, 200, self.block, font=FONT_SMALL)
        self.mission_box_image = pygame.image.load('./Scene_files/Images/mission_box.png')

        # Adjust these buttons to your needs for the second scene
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.75), GREEN, BLUE, "ACCEPT", BLACK, WHITE, self.to_play_payload_challenge
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "MENU", BLACK, WHITE, self.to_menu
        )

    def to_play_payload_challenge(self):
        script_path = "Missions/payload_challenge.py"

        # Launch the game in a separate process
        subprocess.Popen([sys.executable,script_path])

    def to_controls(self):
        self.manager.switch_scene(SceneControls(self.manager, self.game_clock))

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
        screen.blit(BackGround_payload.image, BackGround_payload.rect)
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
# Mission 5: Locate ISS

class SceneMissionISS(Scene):
    def __init__(self, manager, game_clock):
        super().__init__()
        self.manager = manager
        self.game_clock = game_clock
        self.title = "Locate ISS"
        self.block = "Where above Earth is the ISS?"
        self.typewriter_title = TypewriterText(130, 20, 550, 500, Challenge.greet(Challenge(self.title)),
                                               justify="center")
        self.typewriter_block = TypewriterText(150, 200, 430, 200, self.block, font=FONT_SMALL)
        self.mission_box_image = pygame.image.load('./Scene_files/Images/mission_box.png')

        # Adjust these buttons to your needs for the second scene
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.75), GREEN, BLUE, "ACCEPT", BLACK, WHITE,
            self.to_scene_mission_iss_play
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "MENU", BLACK, WHITE, self.to_menu
        )

    def to_scene_mission_iss_play(self):
        self.manager.switch_scene(SceneMissionISSPlay(self.manager, self.game_clock))

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
        screen.blit(BackGround_iss.image, BackGround_iss.rect)
        screen.blit(self.mission_box_image, (75, 120))
        self.typewriter_title.draw(screen)

        # Only draw typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.draw(screen)

        self.button1.draw(screen)
        self.button2.draw(screen)
        super().draw(screen)

########################################################################################################################

class SceneMissionISSPlay(Scene):
    def __init__(self, manager, game_clock):
        super().__init__()
        self.manager = manager
        self.game_clock = game_clock
        self.title = "Locate ISS Mission"
        self.block = ""
        self.typewriter_title = TypewriterText(130, 20, 550, 500, self.title,
                                               justify="center")
        self.typewriter_block = TypewriterText(150, 200, 430, 200, self.block, font=FONT_SMALL)
        self.mission_box_image = pygame.image.load('./Scene_files/Images/mission_box.png')

        # Adjust these buttons to your needs for the second scene
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "MENU", BLACK, WHITE, self.to_menu
        )

    def to_menu(self):
        self.manager.switch_scene(SceneStartMenu(self.manager, self.game_clock))

    def handle_event(self, event):
        super().handle_event(event)
        self.button1.handle_event(event)


    def update(self):
        # Always update the typewriter_title
        self.typewriter_title.update()

        # Only update typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.update()

    def draw(self, screen):
        screen.fill([255, 255, 255])
        screen.blit(BackGround_iss.image, BackGround_iss.rect)
        screen.blit(self.mission_box_image, (75, 120))
        self.typewriter_title.draw(screen)

        # Only draw typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.draw(screen)

        self.button1.draw(screen)
        super().draw(screen)





########################################################################################################################
########################################################################################################################
# Mission 6: Asteroid dodge


class SceneMissionDodge(Scene):
    def __init__(self, manager, game_clock):
        # Initialise the Asteroid Challenge mission scene.
        # Call the superclass (Scene)
        super().__init__()
        # Store the SceneManager and game clock
        self.manager = manager
        self.game_clock = game_clock
        # Title for the scene
        self.title = "Asteroid Dodge"
        self.block = "In this challenge you have to navigate through an asteroid storm."
        self.typewriter_title = TypewriterText(130, 20, 550, 500, Challenge.greet(Challenge(self.title)),
                                               justify="center")
        self.typewriter_block = TypewriterText(150, 200, 430, 200, self.block, font=FONT_SMALL)
        # Load and store the mission box image
        self.mission_box_image = pygame.image.load('./Scene_files/Images/mission_box.png')

        # Define buttons for mission operations
        # Adjust these buttons to your needs for the second scene
        # button1 commented out for now as not set up yet
        # self.button1 = Button(
        #     "center", (SCREEN_HEIGHT * 0.75), GREEN, BLUE, "ACCEPT", BLACK, WHITE, self.to_play_asteroid_dodge
        # )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "MENU", BLACK, WHITE, self.to_menu
        )

    # not set up yet
    # def to_play_asteroid_dodge(self):
    #     script_path = "Missions/asteroid_dodge.py"
    #     # Launch the game in a separate process
    #     subprocess.Popen([sys.executable, script_path])

    def to_menu(self):
        # Switch to the Start Menu scene
        self.manager.switch_scene(SceneStartMenu(self.manager, self.game_clock))

    def handle_event(self, event):
        # Handle events for the scene
        super().handle_event(event)
        # button1 commented out for now as not set up yet
        # self.button1.handle_event(event)
        self.button2.handle_event(event)

    # Update the scene's elements
    # Update the typewriter's title
    # Update the typewriter block if typewriter title has completed
    def update(self):
        # Always update the typewriter_title
        self.typewriter_title.update()

        # Only update typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.update()

    # Draw the scene's elements on the screen
    # Fill the screen with a white background and draw background image
    # Draw typewriter title, typewriter block, buttons, and additional UI elements
    def draw(self, screen):
        screen.fill([255, 255, 255])
        screen.blit(BackGround_asteroid.image, BackGround_asteroid.rect)
        screen.blit(self.mission_box_image, (75, 120))
        self.typewriter_title.draw(screen)

        # Only draw typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.draw(screen)
        # button1 commented out for now as not set up yet
        # self.button1.draw(screen)
        self.button2.draw(screen)
        super().draw(screen)


########################################################################################################################
########################################################################################################################
# Mission 7: Quiz


class SceneQuiz(Scene):
    def __init__(self, manager, game_clock):
        super().__init__()
        self.manager = manager
        self.game_clock = game_clock
        self.title = "Quiz"
        quizgame_instance = QuizGame("Missions/quiz_SQLite/my.db", "Missions/quiz_SQLite/Quiz_game.sql")
        self.block = f"In this challenge you will need to answer {quizgame_instance.num_questions_to_answer} multiple-choice space questions from the database of trivia!|| Enter your name at the end to join the leaderboard."
        self.typewriter_title = TypewriterText(130, 20, 550, 500, Challenge.greet(Challenge(self.title)),
                                               justify="center")
        self.typewriter_block = TypewriterText(150, 200, 430, 200, self.block, font=FONT_SMALL)
        self.mission_box_image = pygame.image.load('./Scene_files/Images/mission_box.png')

        # Adjust these buttons to your needs for the second scene
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.75), GREEN, BLUE, "ACCEPT", BLACK, WHITE, self.to_scene_mission_quiz_input
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "MENU", BLACK, WHITE, self.to_menu
        )

    def to_scene_mission_quiz_input(self):
        self.manager.switch_scene(SceneQuizInput(self.manager, self.game_clock))

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
        screen.blit(BackGround_final.image, BackGround_final.rect)
        screen.blit(self.mission_box_image, (75, 120))
        self.typewriter_title.draw(screen)

        # Only draw typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.draw(screen)

        self.button1.draw(screen)
        self.button2.draw(screen)
        super().draw(screen)


########################################################################################################################


class SceneQuizInput(Scene):
    question_number = 0
    user_score = 0

    def __init__(self, manager, game_clock):
        super().__init__()
        self.manager = manager
        self.game_clock = game_clock
        self.quizgame_instance = QuizGame("Missions/quiz_SQLite/my.db", "Missions/quiz_SQLite/Quiz_game.sql")
        self.user_answer_number = None
        self.question_and_answers_list = self.quizgame_instance.get_provided_question(SceneQuizInput.question_number)
        self.correct = None

        # title
        self.title = "Quiz"
        self.typewriter_title = TypewriterText(130, 20, 550, 500, self.title, justify="center")

        # display text box for question
        # define the box image
        self.display_bl_image = pygame.image.load('./Scene_files/Images/display_bl.png')
        # define a header saying the question number
        self.typewriter_display_head = TypewriterText(55, 105, 200, 100,
                                                      f"Question {SceneQuizInput.question_number + 1}", font=FONT_SMALL,
                                                      colour=(0, 0, 0, 0))
        # Pull the question (the first returned item from get_provided_question() in Quizgame
        self.display_text1 = self.question_and_answers_list[0]
        self.typewriter_display1 = TypewriterText(55, 170, 160, 300, self.display_text1, font=FONT_VSMALL,
                                                  colour=(0, 0, 0, 0))

        # answer buttons
        self.answer_box = pygame.image.load('./Scene_files/Images/trivia_box4_s.png')
        self.answer1 = self.question_and_answers_list[1][0].strip()
        self.answer2 = self.question_and_answers_list[1][1].strip()
        self.answer3 = self.question_and_answers_list[1][2].strip()
        self.answer4 = self.question_and_answers_list[1][3].strip()
        self.answer_button1 = Button(
            "right", (SCREEN_HEIGHT * 0.2), YELLOW, BLUE, self.answer1, BLACK, WHITE,
            lambda: (setattr(self, 'user_answer_number', 1), self.highlight_answer_button1()), FONT_SMALL
        )
        self.answer_button2 = Button(
            "right", (SCREEN_HEIGHT * 0.28), YELLOW, BLUE, self.answer2, BLACK, WHITE,
            lambda: (setattr(self, 'user_answer_number', 2), self.highlight_answer_button2()), FONT_SMALL
        )
        self.answer_button3 = Button(
            "right", (SCREEN_HEIGHT * 0.36), YELLOW, BLUE, self.answer3, BLACK, WHITE,
            lambda: (setattr(self, 'user_answer_number', 3), self.highlight_answer_button3()), FONT_SMALL
        )
        self.answer_button4 = Button(
            "right", (SCREEN_HEIGHT * 0.44), YELLOW, BLUE, self.answer4, BLACK, WHITE,
            lambda: (setattr(self, 'user_answer_number', 4), self.highlight_answer_button4()), FONT_SMALL
        )

        # Submit and menu buttons
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.75), GREEN, BLUE, "SUBMIT", BLACK, WHITE, self.user_submit
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "MENU", BLACK, WHITE, self.to_menu
        )

        # result message and boxes, next question and end buttons
        self.result_message = None
        self.display_box_image_green = pygame.image.load('./Scene_files/Images/ans_box_2.png')
        self.display_box_image_orange = pygame.image.load('./Scene_files/Images/ans_box_3.png')
        self.button_next = Button(
            "center", (SCREEN_HEIGHT * 0.75), ORANGE, BLUE, "NEXT QUESTION", BLACK, WHITE,
            lambda: (setattr(self, 'correct', None), self.to_scene_quiz_input())[1]
        )
        self.button_end = Button(
            "center", (SCREEN_HEIGHT * 0.75), ORANGE, BLUE, "SEE MY RESULTS", BLACK, WHITE,
            lambda: (setattr(self, 'correct', None), self.to_scene_quiz_leaderboard())[1]
        )

    def user_submit(self):
        # run the check answer method from the Quiz class
        result = QuizGame.check_answer(self.quizgame_instance, self.question_and_answers_list, self.user_answer_number)
        # prepare the result message box
        # check answer returns two values, the message at index [0] and whether it was correct/true at index [1]
        if result[1] is True:
            self.correct = True
            SceneQuizInput.user_score += 1
        else:
            self.correct = False
        self.result_message = TypewriterText(420, 370, 250, 200, result[0] + "                          ",
                                             font=FONT_VSMALL, colour=(0, 0, 0, 0))
        SceneQuizInput.question_number += 1
        print(SceneQuizInput.user_score)


    # code for highlighting the button answer choice when clicked
    def highlight_answer_button1(self):
        self.answer_button1 = Button(
            "right", (SCREEN_HEIGHT * 0.2), BLUE, BLUE, self.answer1, WHITE, WHITE, self.highlight_answer_button1,
            FONT_SMALL
        )

    def highlight_answer_button2(self):
        self.answer_button2 = Button(
            "right", (SCREEN_HEIGHT * 0.28), BLUE, BLUE, self.answer2, WHITE, WHITE, self.highlight_answer_button2,
            FONT_SMALL
        )

    def highlight_answer_button3(self):
        self.answer_button3 = Button(
            "right", (SCREEN_HEIGHT * 0.36), BLUE, BLUE, self.answer3, WHITE, WHITE, self.highlight_answer_button3,
            FONT_SMALL
        )

    def highlight_answer_button4(self):
        self.answer_button4 = Button(
            "right", (SCREEN_HEIGHT * 0.44), BLUE, BLUE, self.answer4, WHITE, WHITE, self.highlight_answer_button4,
            FONT_SMALL
        )

    def to_menu(self):
        self.manager.switch_scene(SceneStartMenu(self.manager, self.game_clock))

    def to_scene_quiz_input(self):
        self.manager.switch_scene(SceneQuizInput(self.manager, self.game_clock))

    def to_scene_quiz_leaderboard(self):
        self.manager.switch_scene(SceneQuizLeaderboard(self.manager, self.game_clock))

    def handle_event(self, event):
        super().handle_event(event)
        # answer buttons
        self.answer_button1.handle_event(event)
        self.answer_button2.handle_event(event)
        self.answer_button3.handle_event(event)
        self.answer_button4.handle_event(event)
        # If the result message is not shown yet, you can still handle these buttons (submit, menu)
        if self.result_message is None:
            self.button1.handle_event(event)
            self.button2.handle_event(event)
        # If the result message is already shown, then handle the next question and end buttons
        elif self.result_message is not None:
            if SceneQuizInput.question_number <= 9 and self.correct is not None:
                if self.button_next.handle_event(event):
                    self.to_scene_quiz_input()
            elif SceneQuizInput.question_number == 10 and self.correct is not None:
                if self.button_end.handle_event(event):
                    # to leaderboard scene
                    self.to_scene_quiz_leaderboard()

    def update(self):
        # Always update the typewriter_title
        self.typewriter_title.update()

        # stagger the typewriting
        if self.typewriter_title.completed:
            self.typewriter_display_head.update()
        if self.typewriter_display_head.completed:
            self.typewriter_display1.update()

        #  if the result message has been made by the user pressing the submit button
        if self.result_message:
            self.result_message.update()

    def draw(self, screen):
        screen.fill([255, 255, 255])
        screen.blit(BackGround_final.image, BackGround_final.rect)
        screen.blit(self.display_bl_image, (30, 70))

        self.typewriter_title.draw(screen)

        # Only draw stagger the typewriting
        if self.typewriter_title.completed:
            self.typewriter_display_head.draw(screen)
        if self.typewriter_display_head.completed:
            self.typewriter_display1.draw(screen)
        if self.typewriter_display1.completed:
            screen.blit(self.answer_box, (380, 70))
            self.answer_button1.draw(screen)
            self.answer_button2.draw(screen)
            self.answer_button3.draw(screen)
            self.answer_button4.draw(screen)

        self.button1.draw(screen)
        self.button2.draw(screen)

        # Draw the result_message if it's not None
        if self.result_message:
            if self.correct is True:
                screen.blit(self.display_box_image_green, (380, 345))
            else:
                screen.blit(self.display_box_image_orange, (380, 345))
            self.result_message.draw(screen)
        if SceneQuizInput.question_number <= 9 and self.correct is not None:
            self.button_next.draw(screen)
        elif SceneQuizInput.question_number == 10 and self.correct is not None:
            self.button_end.draw(screen)
        super().draw(screen)


########################################################################################################################

# This class represents the scene where players enter their name to be entered onto the leaderboard
class SceneQuizLeaderboard(Scene):
    def __init__(self, manager, game_clock):
        # Call the superclass (Scene) this contains the mute button
        super().__init__()
        # Store the SceneManager and game clock
        self.manager = manager
        self.game_clock = game_clock

        # Title for the scene
        self.title = "Quiz Results"
        # Create typewriter text for the title
        self.typewriter_title = TypewriterText(130, 20, 550, 500, self.title, justify="center")
        self.quiz_instance = QuizGame("Missions/quiz_SQLite/my.db", "Missions/quiz_SQLite/Quiz_game.sql")

        # Input box elements
        self.trivia_box1_image = pygame.image.load('./Scene_files/Images/trivia_box1.png')
        self.trivia_box2_image = pygame.image.load('./Scene_files/Images/trivia_box1.png')
        self.typewriter_input_head = TypewriterText(70, 125, 150, 100, "Input your name to enter the leaderboard",
                                                    font=FONT_SMALL, colour=(0, 0, 0, 0))
        self.typewriter_input_box = TypewriterText(55, 265, 200, 100, "User input", font=FONT_SMALL,
                                                   colour=(0, 0, 0, 0))
        self.user_input = TextInput(55, 325, 300, 25)
        self.click_sound = Button.click_sound

        # Display text box elements
        # A boolean that will conditionally allow the leaderboard to appear once self.user_input is submitted
        self.submitted = False
        self.player_input = ""
        self.display_bl_image = pygame.image.load('./Scene_files/Images/display_bl.png')
        self.typewriter_display_head = TypewriterText(460, 105, 200, 100, "Score", font=FONT_SMALL, colour=(0, 0, 0, 0))
        self.display_text1 = f"{self.quiz_instance.end_message(self.player_input, SceneQuizInput.user_score)[0]}" \
                             f"|{self.quiz_instance.end_message(self.player_input, SceneQuizInput.user_score)[1]}"
        self.typewriter_display1 = TypewriterText(460, 170, 150, 300, self.display_text1, font=FONT_VSMALL,
                                                  colour=(0, 0, 0, 0))



        # Submit and menu button
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.75), GREEN, BLUE, "SUBMIT", BLACK, WHITE, self.user_submit
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "MENU", BLACK, WHITE, self.to_menu
        )

    def user_submit(self):
        # Get the current text input from the user using the user_answer method from TextInput
        self.player_input = self.user_input.user_answer()
        # Get the current text input from the user using the user_answer method from TextInput
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 1.1), GREEN, BLUE, "", BLACK, WHITE, None
        )
        self.submitted = True
        self.quiz_instance.update_leaderboard(self.player_input, SceneQuizInput.user_score)
        # close the database that was opened in Quizgame
        self.quiz_instance.close()

    # Switch to the Start Menu scene
    def to_menu(self):
        self.manager.switch_scene(SceneStartMenu(self.manager, self.game_clock))
        SceneQuizInput.question_number = 0

    # Handle events for the scene
    def handle_event(self, event):
        super().handle_event(event)
        # Handle events for buttons
        self.button1.handle_event(event)
        self.button2.handle_event(event)
        # Handle events for keyboard entry to user input
        self.user_input.handle_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                self.click_sound.play()
                self.user_submit()

    def update(self):
        # Always update the typewriter_title
        self.typewriter_title.update()

        # Stagger the typewriting
        if self.typewriter_title.completed:
            self.typewriter_display_head.update()
            self.typewriter_input_head.update()
        if self.typewriter_display_head.completed:
            self.typewriter_input_box.update()
        if self.typewriter_input_box.completed:
            self.typewriter_display1.update()



    def draw(self, screen):
        # Draw the scene's elements on the screen
        # Fill the screen with a white background and draw background image
        # Draw typewriter title, staggered typewriter text segments, buttons, user input, and result message
        screen.fill([255, 255, 255])
        screen.blit(BackGround_asteroid.image, BackGround_asteroid.rect)
        screen.blit(self.display_bl_image, (430, 70))
        screen.blit(self.trivia_box1_image, (30, 70))
        screen.blit(self.trivia_box2_image, (30, 250))
        self.typewriter_title.draw(screen)

        # Only draw stagger the typewriting
        if self.typewriter_title.completed:
            self.typewriter_display_head.draw(screen)
            self.typewriter_input_head.draw(screen)
        if self.typewriter_display_head.completed:
            self.typewriter_input_box.draw(screen)
            self.user_input.draw(screen)
            self.button1.draw(screen)
            self.button2.draw(screen)
        if self.submitted:
            self.typewriter_display1.draw(screen)
        super().draw(screen)

########################################################################################################################
########################################################################################################################
