# laying out the structure of the Stratobus Mission challenges the player will face. OOP - each challenge is a class instance
#refactored to have 1 Return statement per fn and no Input variables
import requests
from Missions.Mission_config import today_date_string, api_key, short_url

class Challenge:
    def __init__(self, challenge_name):
        self.challenge_name = challenge_name

    def greet(self):  # outputs a greeting
        return f"Welcome to the {self.challenge_name} challenge!"


class Asteroids(Challenge):

    def success(self):  # do we want to add this as an att to the parent class so it's consistent across all challenges?
        return "Mission Completed |Congratulations!"
        # ALSO go to next mission

    def fail(self):
        return "Oh no, Mission Failed!"

    def display_asteroid_data(self, asteroid_output):
        return '\n'.join(asteroid_output)

    def prompt_display_asteroid_data(self, asteroid_output):
        display_message = self.display_asteroid_data(asteroid_output)
        player_input = ""  # Initialize player input
        return self.asteroid_distance_prompt(), display_message

    def asteroid_distance_prompt(self):
        return f"For any of the 3 asteroids that passed near Earth today, enter the miss distance rounded to the nearest km. |You have 3 attempts... "

    def player_enter_asteroid_distance(self, asteroid_distances, player_input, attempts):

        while attempts >= 1:
                if player_input.isnumeric():
                    if int(player_input) in asteroid_distances:
                        success_message = self.success()  # Get the success message
                        return success_message, attempts  # Return the success message to display in the game

                    else:
                        attempts -= 1
                        if attempts == 1:
                            incorrect_message = f"Incorrect data - try again. |{attempts} attempt remaining..."
                            return incorrect_message, attempts  # Return the incorrect message to display in the game
                        incorrect_message = f"Incorrect data - try again. |{attempts} attempts remaining..."
                        return incorrect_message, attempts  # Return the incorrect message to display in the game

                else:
                    attempts -= 1
                    if attempts == 1:
                        not_numeric_message = f"Oops, it looks like you entered something that isn't a number! {attempts} attempt remaining..."
                        return not_numeric_message, attempts  # Return the not numeric message to display in the game
                    not_numeric_message = f"Oops, it looks like you entered something that isn't a number! {attempts} attempts remaining..."
                    return not_numeric_message, attempts  # Return the not numeric message to display in the game

        return Asteroids.fail(self), attempts

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
            asteroid_distances.append(int(round(asteroid_miss_distance_raw, 0)))
        except: return "No asteroids passed near the Earth today."

        try:
            second_asteroid_miss_distance_raw = float(data['near_earth_objects'][today_date_string][1]['close_approach_data'][0]['miss_distance']["kilometers"])
            second_asteroid_miss_distance_rounded = round(second_asteroid_miss_distance_raw, 2)
            asteroid_output.append(f"2nd = {second_asteroid_miss_distance_rounded}km")
            asteroid_distances.append(int(round(second_asteroid_miss_distance_raw, 0)))
        except: pass

        try:
            third_asteroid_miss_distance_raw = float(data['near_earth_objects'][today_date_string][2]['close_approach_data'][0]['miss_distance']["kilometers"])
            third_asteroid_miss_distance_rounded = round(third_asteroid_miss_distance_raw, 2)
            asteroid_output.append(f"3rd = {third_asteroid_miss_distance_rounded}km")
            asteroid_distances.append(int(round(third_asteroid_miss_distance_raw, 0)))
        except: pass

        return " ".join(asteroid_output), asteroid_distances


#asteroid_challenge = Asteroids("Asteroid Proximity Sensor")
# create new class object, adding the name of the challenge
# print(asteroid_challenge.greet())  # can remove "print" for pygame implementation - just to see the output during dev
# print(asteroid_challenge.get_all_asteroid_data())