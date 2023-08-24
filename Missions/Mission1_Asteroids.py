import requests
from Missions.Mission_config import today_date_string, short_url

class Challenge:
    def __init__(self, challenge_name):
        self.challenge_name = challenge_name

    def greet(self):
        """Displays a greeting to the asteroids mission

        Returns: String - welcome message
        """
        return f"Welcome to the {self.challenge_name} challenge!"  # Output welcome message


class Asteroids(Challenge):
    def success(self):
        """Success message if player correctly inputs asteroid distance

        Returns: String - "mission completed" message
        """

        return "Mission Completed |Congratulations!"

    def fail(self):
        """Fail message if player uses all attempts

        Returns: String - "Oh no, Mission Failed!" message
        """
        return "Oh no, Mission Failed!"

    def display_asteroid_data(self, asteroid_output):
        """Outputs asteroid data for the player to round to nearest km and input

        Args:
            asteroid_output: passed from another fn

        Returns: readable output for the 3 asteroid miss distances on the given day
        """
        return '\n'.join(asteroid_output)  # Output asteroid data in readable format

    def prompt_display_asteroid_data(self, asteroid_distances, asteroid_output, attempts=3):
        """Takes player input for rounded asteroid distance

        Args:
            asteroid_distances: passed from other fn
            asteroid_output: passed from other fn
            attempts: passed from other fn

        Returns: prompt asking player to enter asteroid data

        """
        display_message = self.display_asteroid_data(asteroid_output)
        return self.asteroid_distance_prompt(), display_message  # display prompt asking player to enter answer, and
        # asteroid data

    def asteroid_distance_prompt(self):
        return f"For any of the 3 asteroids that passed near Earth today, enter the miss distance rounded to the nearest km. |You have 3 attempts... "\

    def player_enter_asteroid_distance(self, asteroid_distances, player_input, attempts):
        """For the player to enter the rounded asteroid miss distance (any 1 of the 3 daily asteroids will be
        accepted). Player gets 3 attempts to enter correct number else mission failed.

        Args:
            asteroid_distances: passed from other function
            player_input: passed from other function
            attempts: passed from other function

        Returns: success or failure message

        """
        while attempts >= 1:
            if all(x.isnumeric() for x in player_input):  # checking thst input contains only numbers
                if int(player_input) in asteroid_distances:  # checks player input against available data
                    success_message = self.success()  # get the success message
                    return success_message, attempts  # display success message
                else:
                    attempts -= 1  # player has used 1 attempt
                    if attempts == 1:  # for grammatical correctness if last attempt
                        incorrect_message = f"Incorrect data - try again. |{attempts} attempt remaining..."
  
                        return incorrect_message, attempts  # Return the incorrect message to display in the game
                    incorrect_message = f"Incorrect data - try again. |{attempts} attempts remaining..."
                    return incorrect_message, attempts  # Return the incorrect message to display in the game

            else:
                attempts -= 1  # still use 1 attempt if non-numeric data is entered
                not_numeric_message = f"Oops, it looks like you entered something that isn't a number! {attempts} attempts remaining..."
                return not_numeric_message, attempts  # return the not-numeric message to display in the game

        return Asteroids.fail(self), attempts  # return the fail message to display to the player

    def get_all_asteroid_data(self):
        """Calls NASA API for 3 asteroids that have missed Earth on the current day. There are always asteroids
        recorded in this data (no minimum miss distance on NASA side). Uses API endpoint from
        Missions_config.py file

        Returns: json data that will be filtered in get_3_asteroid_data function
        """
        response = requests.get(short_url)  # call API
        data = response.json()  # format as json
        self.get_3_asteroid_data(data=data, today_date_string=today_date_string)  # get asteroid distances from today using datetime library in Mission_config.py
        return data

    def get_3_asteroid_data(self, data, today_date_string):
        """Filters json data from NASA API to pull just 3 asteroid miss distances from the current day, appends
        this to list that is compared against player input

        Args:
            data: passed from other function
            today_date_string: passed from other function

        Returns: asteroid_output for human-readable printing of this data for the player; asteroid_distances list
        of rounded asteroid distances the player can enter to complete the mission
        """
        asteroid_output = []  # for displaying the current day's asteroid miss distances to player
        asteroid_distances = []  # list of potential answers that are considered correct
        try:
            asteroid_miss_distance_raw = float(data['near_earth_objects'][today_date_string][0]['close_approach_data'][0]['miss_distance']["kilometers"])  # locate 1st asteroid miss dist in json
            asteroid_miss_distance_rounded = round(asteroid_miss_distance_raw, 2)  # round to 2 decimal places
            asteroid_output.append(f"1st = {asteroid_miss_distance_rounded}km")  # append to output list
            asteroid_distances.append(round(asteroid_miss_distance_raw, 0))  # round to nearest whole num and append to possible answer list
        except: return "No asteroids passed near the Earth today."  # if no asteroids today. should in theory never happen as there is no minimum miss distance for an asteroid to be recorded in API

        try:  # same logic as above but for second asteroid of current day
            second_asteroid_miss_distance_raw = float(data['near_earth_objects'][today_date_string][1]['close_approach_data'][0]['miss_distance']["kilometers"])
            second_asteroid_miss_distance_rounded = round(second_asteroid_miss_distance_raw, 2)
            asteroid_output.append(f"2nd = {second_asteroid_miss_distance_rounded}km")
            asteroid_distances.append(round(second_asteroid_miss_distance_raw, 0))
        except: return "No more asteroids passed near the Earth today."  # in tiny chance that only 1 asteroid is recorded

        try: # same logic as above but for second asteroid of current day
            third_asteroid_miss_distance_raw = float(data['near_earth_objects'][today_date_string][2]['close_approach_data'][0]['miss_distance']["kilometers"])
            third_asteroid_miss_distance_rounded = round(third_asteroid_miss_distance_raw, 2)
            asteroid_output.append(f"3rd = {third_asteroid_miss_distance_rounded}km")
            asteroid_distances.append(round(third_asteroid_miss_distance_raw, 0))
        except: return "No more asteroids passed near the Earth today." # in tiny chance that only 2 asteroids are recorded
        return " ".join(asteroid_output), asteroid_distances  # output the asteroid data and distances only for comparisons to use in the pygame user_input logic


def main():
    asteroid_challenge = Asteroids("Asteroid Proximity Sensor")  # create new class object with challenge name
    return asteroid_challenge.greet(), asteroid_challenge.get_all_asteroid_data()  # return first function - all others are linked


if __name__ == "__main__":
    main()
