# laying out the structure of the Stratobus Mission challenges the player will face. OOP - each challenge is a class instance
#refactored to have 1 Return statement per fn and no Input variables
import requests
from Missions.Mission_config import today_date_string, api_key, short_url

class Challenge:
    def __init__(self, challenge_name,
                 # challenge_description
                 ):
        self.challenge_name = challenge_name
        # self.challenge_description = challenge_description

    def greet(self):  # outputs a greeting + challenge description
        # return f"Welcome to the {self.challenge_name} challenge! {self.challenge_description}"
        return f"Welcome to the {self.challenge_name} challenge!"


class Asteroids(Challenge):
    def success(self):  # do we want to add this as an att to the parent class so it's consistent across all challenges?
        return "Mission Completed - congratulations!"
        # ALSO go to next mission

    # def fail(self):  # as above
    #     inp = input("Oh no, Mission Failed! Do you want to try again? Enter Y for Yes or N to quit")
    #     if inp == "Y":
    #         pass
    #         return self.player_enter_asteroid_distance(self, asteroid_distances, asteroid_output)
    #         # re-run whole code
    #     elif inp == "N":
    #         pass
    #         # quit game
    #     else:
    #         fail_message = "Oops - unexpected input! Re-launching game, we're counting on you!"
    #         return fail_message, self.player_enter_asteroid_distance(self, asteroid_distances, asteroid_output)
    #         # re-run whole code

    def fail(self):
        # Simulate logic for handling player input event in PyGame
        player_input_event = None  # Replace with actual event handling logic

        if player_input_event:  # If the player makes an input
            player_input = player_input_event  # Replace with actual player input

            if player_input == "Y":
                fail_message_retry = "We knew we could count on you! Retrying mission..."
                return fail_message_retry, self.prompt_display_asteroid_data(asteroid_distances, asteroid_output)

            elif player_input == "N":
                quit_game_event = True  # Set this flag to quit the game
                return None  # Return None to indicate no further action is needed

            else:
                fail_message = "Oops - unexpected input! Re-launching game, we're counting on you!"
                return fail_message, self.prompt_display_asteroid_data(asteroid_distances, asteroid_output)

        return None  # Return None if no player input event has occurred yet

    def display_asteroid_data(self, asteroid_output):
        return '\n'.join(asteroid_output)

    def prompt_display_asteroid_data(self, asteroid_distances, asteroid_output, attempts=3):
        display_message = self.display_asteroid_data(asteroid_output)
        player_input = ""  # Initialize player input
        return self.asteroid_distance_prompt(asteroid_distances), display_message

    def asteroid_distance_prompt(self
                                 # , asteroid_distances
                                ):
        #print("58") debugging
        return f"For any of the 3 asteroids that passed near Earth today, enter the miss distance rounded to the nearest km. You have 3 attempts... "\
            #, self.player_enter_asteroid_distance(asteroid_distances)

    def player_enter_asteroid_distance(self, asteroid_distances):
        #print("67")  # debugging
        attempts = 3
        while attempts > 0:
            # Simulate logic for handling player input event in PyGame
            player_input_event = None # Add actual event handling logic

            if player_input_event:  # If the player makes an input
                player_input = player_input_event  # Replace with actual player input

                if player_input.isnumeric():
                    if int(player_input) in asteroid_distances:
                        success_message = self.success()  # Get the success message
                        return success_message  # Return the success message to display in the game

                    else:
                        attempts -= 1
                        incorrect_message = f"Incorrect data - try again. {attempts} attempts remaining..."
                        return incorrect_message  # Return the incorrect message to display in the game

                else:
                    attempts -= 1
                    not_numeric_message = f"Oops, it looks like you entered something that isn't a number! {attempts} attempts remaining..."
                    return not_numeric_message  # Return the not numeric message to display in the game

            # "Simulate game loop update here" - according to chatgpt (lol)

        fail_message = self.fail()  # Get the fail message
        return fail_message  # Return the fail message to display in the game

    def get_all_asteroid_data(self):
        response = requests.get(short_url)
        data = response.json()
        self.get_3_asteroid_data(data=data, today_date_string=today_date_string)
        return data

    def get_3_asteroid_data(self, data, today_date_string):
        asteroid_distances = []
        asteroid_output = []
        try:
            asteroid_miss_distance_raw = float(data['near_earth_objects'][today_date_string][0]['close_approach_data'][0]['miss_distance']["kilometers"])
            asteroid_miss_distance_rounded = round(asteroid_miss_distance_raw, 2)
            asteroid_output.append(f"1st = {asteroid_miss_distance_rounded}km")
            asteroid_distances.append(round(asteroid_miss_distance_raw, 0))
            #print("109")
        except: return "No asteroids passed near the Earth today."

        try:
            second_asteroid_miss_distance_raw = float(data['near_earth_objects'][today_date_string][1]['close_approach_data'][0]['miss_distance']["kilometers"])
            second_asteroid_miss_distance_rounded = round(second_asteroid_miss_distance_raw, 2)
            asteroid_output.append(f"2nd = {second_asteroid_miss_distance_rounded}km")
            asteroid_distances.append(round(second_asteroid_miss_distance_raw, 0))
            #print("116")
        except: pass

        try:
            third_asteroid_miss_distance_raw = float(data['near_earth_objects'][today_date_string][2]['close_approach_data'][0]['miss_distance']["kilometers"])
            third_asteroid_miss_distance_rounded = round(third_asteroid_miss_distance_raw, 2)
            asteroid_output.append(f"3rd = {third_asteroid_miss_distance_rounded}km")
            asteroid_distances.append(round(third_asteroid_miss_distance_raw, 0))
            #print("125")
        except: pass
        #print(f"127, {asteroid_output}")  # debugging use only
        # return self.asteroid_distance_prompt(asteroid_distances)
        return " ".join(asteroid_output)


asteroid_challenge = Asteroids("Asteroid Proximity Sensor",
                               # "In this challenge you will track 3 asteroids and see how close they passed by Earth. Report the data back to base to complete the mission!"
                                )
# create new class object, adding the name of the challenge
# print(asteroid_challenge.greet())  # can remove "print" for pygame implementation - just to see the output during dev
# print(asteroid_challenge.get_all_asteroid_data())