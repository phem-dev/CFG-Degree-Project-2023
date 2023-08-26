import random
# This file originally called the Sentinel Process API to download most recent images each time the game is played, but
# due to recurring API credential issues the API was called during dev instead and images saved into the game files

class Challenge:
    def __init__(self, challenge_name):
        self.challenge_name = challenge_name  # challenge name
        self.question_key = None  # Placeholder for question key data
        self.city_mapping = {1: "reyk",  # Map the player's choice to each city code:
                               2: "lima",
                               3: "beij"}

        self.cities = {  # mapping to output full city names & countries
            1: "Reykjavik, Iceland",
            2: "Lima, Peru",
            3: "Beijing, China"
        }

        self.display_question = None  # store the question to be displayed from the options below
        self.correct_ans = None  # store the correct answer (placeholder)

        self.challenge_description = "In this challenge, you will use the Stratobus' Satellite links to capture photos" \
                                     "of three cities and report certain data back to base."


class Satellite(Challenge):
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
        ready_message = "The Satellite is primed and ready! Press 'Capture Images' to take photos."
        capture_confirmation = "Capturing Satellite Images"
        return capture_confirmation, self.download_images()

    def download_images(self):
        """Displays a message to user confirming images are being downloaded. This could be a window popup with flashing
        ellipses for added interactivity?"""
        downloading_messages = []
        for key, value in self.cities.items():
            downloading_message = f"Downloading image {key}: {value}...|"
            downloading_messages.append(downloading_message)
        return downloading_messages

    def random_question(self):
        question_num = random.randint(1, 3)
        question_prompt = None
        correct_answer = None
        if question_num == 1:
            question_prompt = "Select the city with the most cloud|coverage..."
            correct_answer = 2
        elif question_num == 2:
            question_prompt = "Select the image that best displays a body of water..."
            correct_answer = 1
        elif question_num == 3:
            question_prompt = "Select the city that is closest to Tokyo, Japan..."
            correct_answer = 3

        question_answer = {question_prompt: correct_answer}
        return question_answer

    def success(self):
        correct_response_message = "Correct - Mission Completed!"
        return correct_response_message
        # move to next challenge

    def fail(self):
        incorrect_response_message = "Oh no, incorrect answer! Let's try again..."
        return incorrect_response_message, self.random_question()
        # display incorrect_response and randomly display another question. This can be the same question as before


def main():
    satellite_challenge = Satellite("Satellite Imaging")
    return satellite_challenge.greet(), satellite_challenge.random_question()


if __name__ == "__main__":
    main()
