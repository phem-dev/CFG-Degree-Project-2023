import sys # for system exit
import subprocess # for ISS mission
import requests # for mars mission - directly coded
from collections import deque # for quiz question list
from io import BytesIO # for mars mission - directly coded

# configurations
from settings import *
# Superclass and constants
from Scene_files.SceneManager import Scene
# functional classes
from Utils.Typewriter import TypewriterText
from Utils.Button import Button
from Utils.TextInput import TextInput
from Scene_files.background import *
# Mission classes
import Missions.Mission1_Asteroids
import Missions.quiz_SQLite.quiz
from Missions.Mission1_Asteroids import Challenge, Asteroids
from Missions.Mission2_Satellite_Images import Satellite
from Missions.quiz_SQLite.quiz import QuizGame



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
            "center", (SCREEN_HEIGHT * 0.72), GREEN, BLUE, "PLAY", BLACK, WHITE, self.to_welcome
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.84), ORANGE, BLUE, "EXIT", BLACK, WHITE, sys.exit
        )

        pygame.time.set_timer(pygame.USEREVENT + 1,
                              1000)  # This will trigger a USER EVENT after a set time. (the + 1 is used as ID for that USER EVENT in case there are more)

    # Actions as functions to be called on button clicks
    def to_welcome(self):
        self.manager.switch_scene(WelcomeScene(self.manager, self.game_clock))

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
# Intro page giving some background info about the game
class WelcomeScene(Scene):
    def __init__(self, manager, game_clock):
        super().__init__()
        self.manager = manager
        self.game_clock = game_clock

        # Create a button to move to the Missions scene
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.72), GREEN, BLUE, "PLAY", BLACK, WHITE, self.to_start_menu
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.84), ORANGE, BLUE, "EXIT", BLACK, WHITE, sys.exit
        )
        self.typewriter = TypewriterText(280, 125, 250, 500, "Welcome to the Stratobus Missions!", FONT_MEDIUM, WHITE, justify="center")
        self.typewriter_block = TypewriterText(250, 190, 320, 500, "Welcome to the Stratobus Missions!,Welcome to the Stratobus Missions!,Welcome to the Stratobus Missions!,Welcome to the Stratobus Missions!", FONT_SMALL, WHITE,
                                         justify="center")

        # draw text box (asteroids box?), change style for title, write text
        self.mission_box = pygame.image.load('./Scene_files/Images/mission_box.png')
        self.mission_box = pygame.transform.scale(self.mission_box, (500, 350))

    def to_start_menu(self):
        self.manager.switch_scene(SceneStartMenu(self.manager, self.game_clock))

    def handle_event(self, event):
        # Handle events specific to the controls menu scene
        super().handle_event(event)
        self.button1.handle_event(event)
        self.button2.handle_event(event)

    def update(self):
        # Update the scene's elements - if timer has finished, update the typewriter effect
        self.typewriter.update()
        self.typewriter_block.update()

    def draw(self, screen):
        # Draw the scene's elements on the screen

        # Fill the screen with a white background and draw background image
        # If the timer has finished, draw buttons and typewriter text
        # Finally, call the base class's draw method for additional UI elements
        screen.fill([255, 255, 255])
        screen.blit(BackGround_home.image, BackGround_home.rect)
        screen.blit(self.mission_box, (150, 50))  # position for text box
        # If timer has finished, draw buttons and typewriter text
        self.button1.draw(screen)
        self.button2.draw(screen)
        self.typewriter.draw(screen)
        self.typewriter_block.draw(screen)

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
        self.manager.switch_scene(SceneMissionSatellite(self.manager, self.game_clock))

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
        print(result_message)
        print(self.attempts)
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
        self.manager.switch_scene(SceneMissionSatellite(self.manager, self.game_clock))

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
# Mission 2: Satellite Imaging

class SceneMissionSatellite(Scene):
    # This class represents the mission scene for the Satellite Challenge
    def __init__(self, manager, game_clock):
        # Initialise the Satellite Challenge mission scene.
        # Call the superclass (Scene)
        super().__init__()
    # Store the SceneManager and game clock
        self.manager = manager
        self.game_clock = game_clock
    # Title for the scene
        self.title = "Satellite Imaging"
        self.block = "In this challenge, you will use the Stratobus' Satellite links to capture photos of three cities and report certain data back to base."
    # Create typewriter text for title and mission description
        self.typewriter_title = TypewriterText(130, 20, 550, 500, Challenge.greet(Challenge(self.title)), justify="center")
        self.typewriter_block = TypewriterText(150, 200, 430, 200, self.block, font=FONT_SMALL)
    # Load and store the mission box image
        self.mission_box_image = pygame.image.load('./Scene_files/Images/mission_box.png')

        # Define buttons for mission operations
        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.75), GREEN, BLUE, "ACCEPT", BLACK, WHITE, self.to_scene_mission_satellite_play
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "MENU", BLACK, WHITE, self.to_menu
        )

    def to_scene_mission_satellite_play(self):
        # Switch to the Satellite Mission Buttons scene
        self.manager.switch_scene(SceneMissionSatelliteIntro(self.manager, self.game_clock))

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

    def to_menu(self):
        self.manager.switch_scene(SceneStartMenu(self.manager, self.game_clock))

    def draw(self, screen):
        screen.fill([255, 255, 255])
        screen.blit(BackGround_satellite.image, BackGround_satellite.rect)
        screen.blit(self.mission_box_image, (75, 120))
        self.typewriter_title.draw(screen)

        # Only draw typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.draw(screen)

        self.button1.draw(screen)
        self.button2.draw(screen)
        super().draw(screen)


########################################################################################################################
# This class represents the scene where player captures satellite images

class SceneMissionSatelliteIntro(Scene):
    # This class represents the Sentinel Mission scene
    def __init__(self, manager, game_clock):
        # Initialise the Sentinel Mission scene
        # Call the superclass (Scene)
        super().__init__()
        # Store the SceneManager and game clock
        self.manager = manager
        self.game_clock = game_clock

        # Title for the scene
        self.title = "Satellite Imaging Mission"
        self.satellite_instance = Satellite(self.title)
        self.block = "The Satellite is primed and ready! Press 'Capture Images' to take some satellite photos."

        # Create typewriter text for title and mission description
        self.typewriter_title = TypewriterText(130, 20, 550, 500, self.title,
                                               justify="center")
        self.typewriter_block = TypewriterText(150, 200, 430, 200, self.block, font=FONT_SMALL)
        # Load and store the mission box image
        self.mission_box_image = pygame.image.load('./Scene_files/Images/mission_box.png')

        # Adjust these buttons to your needs for the second scene
        # Define buttons for mission options

        self.button1 = Button(
            "center", (SCREEN_HEIGHT * 0.75), GREEN, BLUE, "CAPTURE IMAGES", BLACK, WHITE, self.to_scene_mission_satellite_answer
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "MENU", BLACK, WHITE, self.to_menu
        )

    def to_scene_mission_satellite_answer(self):
        self.manager.switch_scene(SceneMissionSatelliteAnswer(self.manager, self.game_clock))

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
        screen.blit(BackGround_satellite.image, BackGround_satellite.rect)
        screen.blit(self.mission_box_image, (75, 120))
        self.typewriter_title.draw(screen)

        # Only draw typewriter_block if typewriter_title has completed
        if self.typewriter_title.completed:
            self.typewriter_block.draw(screen)

        self.button1.draw(screen)
        self.button2.draw(screen)
        super().draw(screen)

########################################################################################################################
# New scene where images are displayed and player is asked a question
class SceneMissionSatelliteAnswer(Scene):

    def __init__(self, manager, game_clock):
        # Initialise the Sentinel Mission scene
        # Call the superclass (Scene)
        super().__init__()
        # Store the SceneManager and game clock
        self.manager = manager
        self.game_clock = game_clock
        self.allow_button_clicks = True
        self.answered_correctly = False

        # Title for the scene
        self.title = "Satellite Images Received"
        self.satellite_instance = Satellite(self.title)

        # Based on the value of question_answer above, set the relevant Image button as the correct answer. The other 2
        # image buttons should be set as incorrect responses. These will vary depending on which question is randomly
        # chosen by self.satellite_instance.random_question() further down
        # BACK button should redirect to menu but not working atm

        # Render the three images onscreen above the 3 buttons
        self.satellite_image1 = pygame.image.load("./Missions/satellite_image1.jpg")
        self.satellite_image2 = pygame.image.load("./Missions/satellite_image2.jpg")
        self.satellite_image3 = pygame.image.load("./Missions/satellite_image3.jpg")

        # Resize the images
        self.satellite_image1 = pygame.transform.scale(self.satellite_image1, (190, 360))
        self.satellite_image2 = pygame.transform.scale(self.satellite_image2, (190, 360))
        self.satellite_image3 = pygame.transform.scale(self.satellite_image3, (190, 360))

        # Create typewriter text for screen title, subtitle (top of question box) and question text
        self.typewriter_title = TypewriterText(130, 20, 550, 500, self.title,
                                               justify="center")

        self.typewriter_subtitle = TypewriterText(66, 480, 210, 100, "CHOOSE CAREFULLY...", font=FONT_MEDSMALL,
                                                  colour=(0, 0, 0, 0))

        text_block = self.satellite_instance.random_question()
        for question_prompt, question_answer in text_block.items():
            self.typewriter_block = TypewriterText(70, 515, 470, 120, question_prompt,
                                                   font=FONT_MEDSMALL, colour=(0, 0, 0, 0))

        # Initialise image option buttons + back button
        self.button1 = Button(
            "left", (SCREEN_HEIGHT * 0.66), GREEN, BLUE, "IMAGE 1", BLACK, WHITE, self.incorrect_answer
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.66), GREEN, BLUE, "IMAGE 2", BLACK, WHITE, self.incorrect_answer
        )
        self.button3 = Button(
            "right", (SCREEN_HEIGHT * 0.66), GREEN, BLUE, "IMAGE 3", BLACK, WHITE, self.incorrect_answer
        )
        self.button4 = Button(645, 460, ORANGE, BLUE, "BACK", BLACK, WHITE, self.to_menu)

        # Change one of the buttons to correct_answer, depending on the question that was displayed
        correct_answer = list(text_block.values())[0]

        if correct_answer == 1:
            self.button1 = Button(
                "left", (SCREEN_HEIGHT * 0.66), GREEN, BLUE, "IMAGE 1", BLACK, WHITE, self.correct_answer
            )
        elif correct_answer == 2:
            self.button2 = Button(
                "center", (SCREEN_HEIGHT * 0.66), GREEN, BLUE, "IMAGE 2", BLACK, WHITE, self.correct_answer
            )
        elif correct_answer == 3:
            self.button3 = Button(
                "right", (SCREEN_HEIGHT * 0.66), GREEN, BLUE, "IMAGE 3", BLACK, WHITE, self.correct_answer
            )

        # Captions for all 3 images telling the player what the city & country are
        self.typewriter_caption1 = TypewriterText(60, 80, 100, 70, "Reykjavik, Iceland", font=FONT_VSMALL, colour=BLACK)
        self.typewriter_caption2 = TypewriterText(310, 80, 100, 70, "Lima, Peru", font=FONT_VSMALL, colour=BLACK)
        self.typewriter_caption3 = TypewriterText(550, 80, 100, 70, "Beijing, China", font=FONT_VSMALL, colour=BLACK)

        # Load and store the mission box image
        self.mission_box_image = pygame.image.load("./Scene_files/Images/ans_box_1.png")
        self.mission_box_image = pygame.transform.scale(self.mission_box_image, (600, 130))

        # Create text box shapes for the image captions, adjust sizing
        self.ans_box_2 = pygame.image.load("./Scene_files/Images/ans_box_2.png")
        self.ans_box_2 = pygame.transform.scale(self.ans_box_2, (170, 45))
        self.ans_box_3 = pygame.image.load("./Scene_files/Images/ans_box_3.png")
        self.ans_box_3 = pygame.transform.scale(self.ans_box_2, (170, 45))
        self.ans_box_4 = pygame.image.load("./Scene_files/Images/ans_box_4.png")
        self.ans_box_4 = pygame.transform.scale(self.ans_box_2, (170, 45))

    def correct_answer(self):  # if answer is correct, display confirmation and block remaining buttons apart from NEXT (button gets updated in handle_event function)
        self.typewriter_block = TypewriterText(70, 515, 470, 120, "Correct, Mission Completed!", font=FONT_MEDSMALL,
                                               colour=(0, 0, 0, 0))
        self.typewriter_block.update()
        self.allow_button_clicks = False
        self.answered_correctly = True

    def to_scene_mission_satellite_intro(self):
        self.manager.switch_scene(SceneMissionSatelliteIntro(self.manager, self.game_clock))

    def incorrect_answer(self):  # if incorrect, block all buttons apart from BACK
        self.typewriter_block = TypewriterText(70, 515, 470, 120, "Oh no, Mission Failed! You'll have to go back and accept the mission again...", font=FONT_MEDSMALL,
                                               colour=(0, 0, 0, 0))
        self.typewriter_block.update()
        self.allow_button_clicks = False

    def to_menu(self):  # change screen back to Menu
        self.manager.switch_scene(SceneMissionSatellite(self.manager, self.game_clock))

    def to_scene_mission_mars(self):  # if correct answer was chosen, switch to next mission (Mars)
        self.manager.switch_scene(SceneMissionMars(self.manager, self.game_clock))

    def handle_event(self, event):
        self.button4.handle_event(event)
        if self.allow_button_clicks:
            super().handle_event(event)
            self.button1.handle_event(event)
            self.button2.handle_event(event)
            self.button3.handle_event(event)

    def update(self):
        # Always update the typewriter title
        # Only update the typewriter block if typewriter title has completed
        self.typewriter_title.update()

        # Sequence for text element updating
        if self.typewriter_title.completed:
            self.typewriter_subtitle.update()
        if self.typewriter_subtitle.completed:
            self.typewriter_block.update()

        if self.typewriter_title.completed:
            self.typewriter_caption1.update()
        if self.typewriter_caption1.completed:
            self.typewriter_caption2.update()
        if self.typewriter_caption2.completed:
            self.typewriter_caption3.update()
        if self.answered_correctly:
            self.button4 = Button(645, 460, GREEN, BLUE, "NEXT", BLACK, WHITE, self.to_scene_mission_mars)

    def draw(self, screen):
        screen.fill([255, 255, 255])
        screen.blit(BackGround_satellite.image, BackGround_satellite.rect)
        screen.blit(self.mission_box_image, (30, 450))
        screen.blit(self.satellite_image1, (50, 75))
        screen.blit(self.satellite_image2, (300, 75))
        screen.blit(self.satellite_image3, (540, 75))
        screen.blit(self.ans_box_2, (50, 75))
        screen.blit(self.ans_box_3, (300, 75))
        screen.blit(self.ans_box_4, (540, 75))

        self.typewriter_title.draw(screen)

        # Sequence for text element drawing
        if self.typewriter_title.completed:
            self.typewriter_subtitle.draw(screen)
        if self.typewriter_subtitle.completed:
            self.typewriter_block.draw(screen)

        if self.typewriter_title.completed:
            self.typewriter_caption1.draw(screen)
        if self.typewriter_caption1.completed:
            self.typewriter_caption2.draw(screen)
        if self.typewriter_caption2.completed:
            self.typewriter_caption3.draw(screen)

        self.button1.draw(screen)
        self.button2.draw(screen)
        self.button3.draw(screen)
        self.button4.draw(screen)
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

        #title block
        self.title = "Capture Mars Mission"
        self.block = ""
        self.typewriter_title = TypewriterText(200, 20, 400, 500, self.title, justify="center")

        # define which button is clicked
        self.camera_choice = None
        self.pygame_image = None  # latest image
        self.pygame_image2 = None  # previous image
        self.rover_text = TypewriterText(100, 200, 300, 300, "", justify="center")
        self.camera_text = TypewriterText(100, 250, 300, 300, "", justify="center")
        self.no_image_text = TypewriterText(100, 200, 300, 300, "", justify="center")
        self.loading_text = TypewriterText(200, 350, 300, 300, "LOADING...", justify="center", font=FONT_SMALL)
        self.button_clicked = False



        # menu button
        self.button0 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "MENU", BLACK, WHITE, self.to_menu
        )
        # Camera buttons
        self.button1 = Button(
            (SCREEN_HEIGHT * 0.05), (SCREEN_HEIGHT * 0.77), YELLOW, BLUE, "Front Hazard Camera", BLACK, WHITE,  lambda: (setattr(self, 'camera_choice',  1), setattr(self, 'button_clicked', True), self.run())[1], FONT_SMALL
        )
        self.button2 = Button(
            (SCREEN_HEIGHT * 0.7), (SCREEN_HEIGHT * 0.77), YELLOW, BLUE, "Rear Hazard Camera", BLACK, WHITE,lambda: (setattr(self, 'camera_choice', 2), setattr(self, 'button_clicked', True), self.run())[1], FONT_SMALL
        )
        self.button3 = Button(
            "center", (SCREEN_HEIGHT * 0.82), YELLOW, BLUE, "Navigation Camera", BLACK, WHITE, lambda: (setattr(self, 'camera_choice', 3), setattr(self, 'button_clicked', True), self.run())[1], FONT_SMALL
        )

        # Map the player's choice to each camera:
        self.camera_mapping = {1: "FHAZ", 2: "RHAZ", 3: "MAST"}

        # Variables to display full camera name:
        self.camera_names = {
            "FHAZ": "Front Hazard Camera",
            "RHAZ": "Rear Hazard Camera",
            "MAST": "Navigation Camera"
        }

        # Function to check if the input is a valid number:
    def is_valid(self, input_str):
        try:
            int(input_str)  # Try to convert the input to an integer
            return True
        except ValueError:  # If ValueError occurs, return False
            return False

    def fetch_previous_images(self, camera, num_images=5):
        # Fetch previous images from the NASA Mars API:
        mars_api_key = "nFd7Ku7gaRTV7eeYliSeSsYFVOP4oN7U6J80KbFP"
        rover = "curiosity"

        # Variable created for the Mars API URL based on the chosen camera:
        mars_url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?camera={camera}&api_key={mars_api_key}&sol=1000&page=1&per_page={num_images}"

        # Get response from API:
        response = requests.get(mars_url)

        # If status code is 200, get image data:
        if response.status_code == 200:
            # Parse the response data as JSON:
            data = response.json()
            if "photos" in data and data["photos"]:
                img_urls = [photo["img_src"] for photo in data["photos"]]
                images_data = []

                for img_url in img_urls:
                    # fetch image:
                    image_response = requests.get(img_url)
                    if image_response.status_code == 200:
                        image_data = image_response.content
                        images_data.append(image_data)

                # Return list of image data:
                return images_data

        return None
    def fetch_latest_image(self, camera):
        # Fetch the latest image from the NASA API
        mars_api_key = "nFd7Ku7gaRTV7eeYliSeSsYFVOP4oN7U6J80KbFP"
        rover = "curiosity"
        mars_url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/latest_photos?camera={camera}&api_key={mars_api_key}"
        response = requests.get(mars_url)

        # If status code is 200, get LATEST image data:
        if response.status_code == 200:
            # Parse the response data as JSON:
            data = response.json()
            if "latest_photos" in data and data["latest_photos"]:
                latest_img_url = data["latest_photos"][0]["img_src"]
                # Fetch the latest image:
                image_response = requests.get(latest_img_url)
                if image_response.status_code == 200:
                    image_data = image_response.content

                    # Return a dictionary of data:
                    return {
                        'data': image_data,
                        'rover_name': rover.capitalize(),
                        'camera_choice_name': self.camera_names[self.camera_mapping[self.camera_choice]]
                    }

        return None

    def scale_image(self, image):
        # Scale the image to smaller dimensions:
        scaled_width = 350
        scaled_height = 350
        return pygame.transform.scale(image, (scaled_width, scaled_height))

    def run(self):
        if self.camera_choice:
            camera = self.camera_mapping[self.camera_choice]
            latest_image_data = self.fetch_latest_image(camera)
            if latest_image_data:
                # Display latest image and camera information:
                pygame_image = pygame.image.load(BytesIO(latest_image_data['data']))

                # Scale the image to smaller dimensions:
                self.pygame_image = self.scale_image(pygame_image)

                # Display text info/which camera: ------------------------------------------------------------ ***CHANGE FONT******
                self.rover_text = TypewriterText(253, 370, 300, 300,
                                                 f"Photo from Mars Rover {latest_image_data['rover_name']}", FONT_VSMALL, justify="center")
                self.camera_text = TypewriterText(253, 390, 300, 300,
                                                  f"Camera: {latest_image_data['camera_choice_name']}", FONT_VSMALL, justify="center")

            # Check if no latest image is available
            else:
                # Fetch and display photos from the code
                images_data = self.fetch_previous_images(camera)
                if images_data:
                    # Select the first image data from the list
                    selected_image_data = images_data[0]
                    pygame_image2 = pygame.image.load(BytesIO(selected_image_data))
                    self.pygame_image2 = self.scale_image(pygame_image2)
                    self.rover_text = TypewriterText(253, 370, 300, 300,
                                                     f"Photo from Mars Rover", FONT_VSMALL, justify="center")
                    self.camera_text = TypewriterText(253, 390, 300, 300,
                                                      f"Camera: {self.camera_names[camera]}", FONT_VSMALL, justify="center")
                else:
                    self.no_image_text = TypewriterText(175, 275, 300, 300, "Sorry. No images available at this time.")



    def to_menu(self):
        self.manager.switch_scene(SceneStartMenu(self.manager, self.game_clock))

    def handle_event(self, event):
        super().handle_event(event)
        self.button0.handle_event(event)
        self.button1.handle_event(event)
        self.button2.handle_event(event)
        self.button3.handle_event(event)


    def update(self):
        # Always update the typewriter title
        self.typewriter_title.update()
        if self.button_clicked:
            self.loading_text.update()
        if self.button_clicked:
            self.rover_text.update()
        if self.button_clicked:
            self.camera_text.update()
        if self.button_clicked:
            self.no_image_text.update()


    def draw(self, screen):
        screen.fill([255, 255, 255])
        screen.blit(BackGround_mars.image, BackGround_mars.rect)
        self.typewriter_title.draw(screen)

        if self.button_clicked:
            self.loading_text.draw(screen)

        self.button0.draw(screen)
        self.button1.draw(screen)
        self.button2.draw(screen)
        self.button3.draw(screen)
        super().draw(screen)

        if self.pygame_image:
            pygame.draw.rect(screen, [0, 0, 0], (225, 75, 350, 350))
            screen.blit(self.pygame_image, (225, 75))
            self.rover_text.draw(screen)
            self.camera_text.draw(screen)
        if self.pygame_image2:
            pygame.draw.rect(screen, [0, 0, 0], (225, 75, 350, 350))
            screen.blit(self.pygame_image2, (225, 75))
            self.rover_text.draw(screen)
            self.camera_text.draw(screen)


########################################################################################################################
#######################################################################################################################
# Mission 4: Payload
class SceneMissionPayload(Scene):
    def __init__(self, manager, game_clock):
        super().__init__()
        self.manager = manager
        self.game_clock = game_clock
        self.title = "Payload Challenge"
        self.block = "The stored memory is running low help defragment the data storage by using the arrows keys to optimally pack the data packets in!"
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

    def run_payload_game(self):
        script_path = "payload_challenge.py"
        subprocess.call(["python", script_path])

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
            self.to_play_iss
        )
        self.button2 = Button(
            "center", (SCREEN_HEIGHT * 0.87), ORANGE, BLUE, "MENU", BLACK, WHITE, self.to_menu
        )

    def to_play_iss(self):
            script_path = "Missions/Mission5_ISS.py"

            # Launch the game in a separate process
            subprocess.Popen([sys.executable, script_path])

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
    quizgame_instance = QuizGame("Missions/quiz_SQLite/my.db", "Missions/quiz_SQLite/Quiz_game.sql")
    all_questions_and_answers_lists = quizgame_instance.fetch_random_questions(10)

    def __init__(self, manager, game_clock):
        super().__init__()
        self.manager = manager
        self.game_clock = game_clock
        self.quizgame_instance = QuizGame("Missions/quiz_SQLite/my.db", "Missions/quiz_SQLite/Quiz_game.sql")

        self.number_of_questions = 10
        self.user_answer_number = None
        self.all_questions_and_answers_lists = SceneQuizInput.all_questions_and_answers_lists
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
        self.display_question_text = self.all_questions_and_answers_lists[0][1]
        self.typewriter_display1 = TypewriterText(55, 170, 160, 300, self.display_question_text, font=FONT_VSMALL,
                                                  colour=(0, 0, 0, 0))

        # answer buttons
        self.answer_box = pygame.image.load('./Scene_files/Images/trivia_box4_s.png')
        self.answer1 = self.all_questions_and_answers_lists[0][2].strip()
        self.answer2 = self.all_questions_and_answers_lists[0][3].strip()
        self.answer3 = self.all_questions_and_answers_lists[0][4].strip()
        self.answer4 = self.all_questions_and_answers_lists[0][5].strip()
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
        result = self.quizgame_instance.check_answer(self.all_questions_and_answers_lists[0], self.user_answer_number)
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
        deque_all_questions_and_answers_lists = deque(SceneQuizInput.all_questions_and_answers_lists)
        deque_all_questions_and_answers_lists.popleft()
        SceneQuizInput.all_questions_and_answers_lists = list(deque_all_questions_and_answers_lists)


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
        self.user_input = TextInput(55, 325, 200, 25)
        self.click_sound = Button.click_sound

        # Display text box elements
        # A boolean that will conditionally allow the leaderboard to appear once self.user_input is submitted
        self.submitted = False
        self.player_input = ""
        self.display_bl_image = pygame.image.load('./Scene_files/Images/display_bl.png')
        self.typewriter_display_head = TypewriterText(460, 105, 200, 100, "Score", font=FONT_SMALL, colour=(0, 0, 0, 0))
        self.display_text1 = ""
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
        self.quiz_instance.update_leaderboard(self.player_input, SceneQuizInput.user_score)
        self.display_text1 = f"{self.quiz_instance.end_message(self.player_input, SceneQuizInput.user_score)[0]}" \
                             f"|{self.quiz_instance.end_message(self.player_input, SceneQuizInput.user_score)[1]}"
        self.typewriter_display1 = TypewriterText(460, 170, 150, 300, self.display_text1, font=FONT_VSMALL,
                                                  colour=(0, 0, 0, 0))
        self.submitted = True
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
