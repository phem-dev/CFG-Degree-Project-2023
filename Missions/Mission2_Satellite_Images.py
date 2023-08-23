import pygame
from io import BytesIO
import random

class Challenge:
    def __init__(self, challenge_name):
        pygame.init()  # initialise PyGame

        # Set up the display:
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.challenge_name = challenge_name  # challenge name
        self.question_key = None  # Placeholder for question key data
        self.city_mapping = {1: "reyk",  # Map the player's choice to each city code:
                               2: "lima",
                               3: "beij"}

        self.cities = {  # mapping to output full city names & countries
            1: "Reykjavík, Iceland",
            2: "Lima, Peru",
            3: "Beijing, China"
        }

        self.display_question = None  # store the question to be displayed from the options below
        self.correct_ans = None  # store the correct answer (placeholder)

        self.challenge_description = "In this challenge, you will use the Stratobus' Satellite links to capture photos" \
                                     "of three cities and report certain data back to base."

    def greet(self):
        """Outputs a greeting to the challenge
        Returns: Player-friendly greeting with challenge name
        """
        return f"Welcome to the {self.challenge_name} challenge!|", self.challenge_description, self.capture_images()

    def capture_images(self):
        """Added interactivity to simulate user taking the photos themselves. 'Capture Images' will be a button for user
        to click
        Returns: Confirmation message + move to the next function.
        """
        ready_message = "The Satellite is primed and ready! Press 'Capture Images' to take photos"  # display this first
        # pygame button = "Capture Images"
        # when button clicked -> return capture_confirmation
        capture_confirmation = "Capturing Satellite Images"
        return capture_confirmation, self.download_images()

    def download_images(self):
        """Displays a message to user confirming images are being downloaded. This could be a window popup with flashing
        ellipses for added interactivity?"""
        downloading_messages = []
        for key, value in self.cities.items():
            downloading_message = f"Downloading image {key}: {value}...|"
            downloading_messages.append(downloading_message)
        return downloading_messages, self.render_images()

    def render_images(self):
        """Initialise a PyGame object for each photo and display to user. Either each photo will be clickable, or each
        will have a clickable button underneath to select that photo

        Returns: 3 x PyGame objects (images)
        """

        # function body to display images as pygame object for player to see
        # images are stored as "sentinel_image_1/2/3.jpg" in Missions folder
        # will need to be resized, then 'pass' replaced with PyGame objects
        pass


    def random_question(self):
        question_num = random.randint(1,3)
        self.display_question = f"question_{question_num}"
        return self.display_question, self.correct_answer()

    def correct_answer(self):
        if self.display_question == "question_1":
            return 2
        elif self.display_question == "question_2":
            return 1
        elif self.display_question == "question_3":
            return 3

    def question_1(self):
        """Question option 1 - 'Select the city with the most cloud coverage...', ans = 2"""
        question_prompt = "Select the city with the most cloud coverage..."
        self.correct_ans = 2

    def question_2(self):
        """Question option 2 - 'Select the image that best displays a body of water...', ans = 1"""
        question_prompt = "Select the image that best displays a body of water..."
        self.correct_ans = 1

    def question_3(self):
        """Question option 3 - 'Select the city that is closest to Tokyo, Japan...', ans = 3"""
        question_prompt = "Select the city that is closest to Tokyo, Japan..."
        self.correct_ans = 3

    def answer(self, correct_ans):
        """Takes player's answer and determines if correct
                Args:
                    correct_ans: correct answer, hardcoded per question

                Returns: success or fail message
                """
        player_input = None  # pygame object for button choice OR player input (preferably buttons)

        if player_input == correct_ans:
            return True
        else:
            return False

    def correct_response(self):
        correct_response_message = "Correct - Mission Completed!"
        return correct_response_message
        # move to next challenge

    def incorrect_response(self):
        incorrect_response_message = "Oh no, incorrect answer! Let's try again..."
        return incorrect_response_message, self.random_question()
        # display incorrect_response and randomly display another question. This can be the same question as before


def main():
    pygame.init()
    satellite_challenge = Challenge("Satellite Imaging")
    question, correct_ans = satellite_challenge.random_question()
    result = satellite_challenge.answer(correct_ans)

    if result:
        satellite_challenge.correct_response()
    else:
        satellite_challenge.incorrect_response()

    return satellite_challenge.greet(), satellite_challenge.random_question()  # random_question removed from flow of
    # functions & inserted here for unit testing - expected_output and result were throwing different random questions


if __name__ == "__main__":
    main()
