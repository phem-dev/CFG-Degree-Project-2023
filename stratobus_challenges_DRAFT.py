# laying out the structure of the Stratobus Mission challenges the player will face. OOP - each challenge is a class instance
import requests
from datetime import date


class Challenge:
    def __init__(self, challenge_name):# is this bit needed?? adding any attributes to the challenges
        self.challenge_name = challenge_name

    def greet(self): # only if we want a generic greeting as the player gets to each challenge. Can use interpolation to insert the name of the challenge into the Welcome statement
        print("Welcome to the X challenge!")
        # call funct body

    def exit(self):# as above
        print("Goodbye!")

class Asteroids(Challenge):
    def success(self):
        print("success")
        # body

    def fail(self):
        print("fail")
        # body


    def player_enter_asteroid_distance(self, asteroid_distances):
        attempts = 3
        while attempts > 0:
            inp = input(f"For any of the 3 asteroids that passed near Earth today, enter the miss distance rounded to the nearest km. You have {attempts} attempts remaining... ")
            if inp.isnumeric():
                if int(inp) in asteroid_distances:
                    self.success() #call Success function from above if player inputs correct number
                    break
                else:
                    attempts -= 1
                    print(f"Incorrect data - try again. {attempts} attempts remaining... ")#add attempt number here too using interpolation?
            else:
                attempts -= 1
                print(f"Oops, it looks like you entered something that isn't a number! {attempts} attempts remaining... ")#move this so that
        if attempts == 0:
            self.fail()


    def get_3_asteroid_data(self):
        asteroid_distances = []
        today_date = date.today()
        today_date_string = str(today_date)

        api_key = "nFd7Ku7gaRTV7eeYliSeSsYFVOP4oN7U6J80KbFP"
        short_url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={today_date}&end_date={today_date}&api_key={api_key}"

        response = requests.get(short_url)
        data = response.json()
        try:
            first_asteroid_miss_distance_raw = float(data['near_earth_objects'][today_date_string][0]['close_approach_data'][0]['miss_distance']["kilometers"])
            first_asteroid_miss_distance_rounded = round(first_asteroid_miss_distance_raw, 2)
            print(f"First asteroid miss distance (km) = {first_asteroid_miss_distance_rounded}")
            asteroid_distances.append(int(first_asteroid_miss_distance_raw))
        except:
            return "No asteroids passed near the Earth today."

        try:
            second_asteroid_miss_distance_raw = float(data['near_earth_objects'][today_date_string][1]['close_approach_data'][0]['miss_distance']["kilometers"])
            second_asteroid_miss_distance_rounded = round(second_asteroid_miss_distance_raw, 2)
            print(f"Second asteroid miss distance (km) = {second_asteroid_miss_distance_rounded}")
            asteroid_distances.append(int(second_asteroid_miss_distance_raw))
        except:
            pass

        try:
            third_asteroid_miss_distance_raw = float(data['near_earth_objects'][today_date_string][2]['close_approach_data'][0]['miss_distance']["kilometers"])
            third_asteroid_miss_distance_rounded = round(third_asteroid_miss_distance_raw, 2)
            print(f"Third asteroid miss distance (km) = {third_asteroid_miss_distance_rounded}")
            asteroid_distances.append(int(third_asteroid_miss_distance_raw))
        except:
            pass

        self.player_enter_asteroid_distance(asteroid_distances)


#the below lines create a class object for the asteroid challenge and run it
asteroid_challenge = Asteroids("Asteroid Proximity Sensor") #create new class object, adding the name of the challenge
asteroid_challenge.get_3_asteroid_data()
