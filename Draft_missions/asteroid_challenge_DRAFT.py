# laying out the structure of the Stratobus Mission challenges the player will face. OOP - each challenge is a class instance
import requests
from stratobus_challenges_config import today_date_string, api_key, short_url

class Challenge:
    def __init__(self, challenge_name, challenge_description):
        self.challenge_name = challenge_name
        self.challenge_description = challenge_description

    def greet(self):  # outputs a greeting + challenge description
        return f"Welcome to the {self.challenge_name} challenge! {self.challenge_description}"

class Asteroids(Challenge):
    def success(self):  # do we want to add this as an att to the parent class so it's consistent across all challenges?
        return "Mission Completed - congratulations!"
        # return to base

    def fail(self):  # as above
        inp = input("Oh no, Mission Failed! Do you want to try again? Enter Y for Yes or N to quit")
        if inp == "Y":
            pass
            # re-run whole code
        elif inp == "N":
            pass
            # quit game
        else:
            return "Oops - unexpected input! Re-launching game, we're counting on you!"
        # re-run whole code

    def display_asteroid_data(self, asteroid_output):
        return '\n'.join(asteroid_output)


# refactor the below and split up even further. need 1 fn per output
    def player_enter_asteroid_distance(self, asteroid_distances, asteroid_output):
        print(self.display_asteroid_data(asteroid_output))
        attempts = 3
        while attempts > 0:
            inp = input(f"For any of the 3 asteroids that passed near Earth today, enter the miss distance rounded to the nearest km. You have {attempts} attempts remaining... ")
            if inp.isnumeric():
                if int(inp) in asteroid_distances:
                    print(self.success())  # print statement here - will this work in pygame?
                    break
                else:
                    attempts -= 1
                    print(f"Incorrect data - try again. {attempts} attempts remaining... ")
            else:
                attempts -= 1
                print(f"Oops, it looks like you entered something that isn't a number! {attempts} attempts remaining... ")  # move this?
        if attempts == 0:
            print(self.fail()) # print statement here - will this work in pygame?

    def get_all_asteroid_data(self):
        response = requests.get(short_url)
        data = response.json()

        self.get_3_asteroid_data(data=data, today_date_string=today_date_string)

    def get_3_asteroid_data(self, data, today_date_string):
        asteroid_distances = []
        asteroid_output = []

        try:
            asteroid_miss_distance_raw = float(data['near_earth_objects'][today_date_string][0]['close_approach_data'][0]['miss_distance']["kilometers"])
            asteroid_miss_distance_rounded = round(asteroid_miss_distance_raw, 2)
            asteroid_output.append(f"First asteroid miss distance (km) = {asteroid_miss_distance_rounded}")
            asteroid_distances.append(round(asteroid_miss_distance_raw, 0))
        except: return "No asteroids passed near the Earth today."

        try:
            second_asteroid_miss_distance_raw = float(data['near_earth_objects'][today_date_string][1]['close_approach_data'][0]['miss_distance']["kilometers"])
            second_asteroid_miss_distance_rounded = round(second_asteroid_miss_distance_raw, 2)
            asteroid_output.append(f"Second asteroid miss distance (km) = {second_asteroid_miss_distance_rounded}")
            asteroid_distances.append(round(second_asteroid_miss_distance_raw, 0))
        except: pass

        try:
            third_asteroid_miss_distance_raw = float(data['near_earth_objects'][today_date_string][2]['close_approach_data'][0]['miss_distance']["kilometers"])
            third_asteroid_miss_distance_rounded = round(third_asteroid_miss_distance_raw, 2)
            asteroid_output.append(f"Third asteroid miss distance (km) = {third_asteroid_miss_distance_rounded}")
            asteroid_distances.append(round(third_asteroid_miss_distance_raw, 0))
        except: pass

        self.player_enter_asteroid_distance(asteroid_distances, asteroid_output)


# the below lines create a class object for the asteroid challenge and run it
asteroid_challenge = Asteroids("Asteroid Proximity Sensor", "In this challenge you will track 3 asteroids and see how close they passed by Earth. Report the data back to base to complete the mission!")  # create new class object, adding the name of the challenge
print(asteroid_challenge.greet())
asteroid_challenge.get_all_asteroid_data()

