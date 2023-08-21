import unittest
from unittest.mock import patch
from Missions.Mission1_Asteroids import Asteroids


class TestAsteroidsChallenge(unittest.TestCase):

    def setUp(self):
        # initialising class object to test
        self.asteroid_challenge = Asteroids("Asteroid Proximity Sensor")

    def test_greet(self):  # testing output of greet function
        expected_output = "Welcome to the Asteroid Proximity Sensor challenge!"
        result = self.asteroid_challenge.greet()
        self.assertEqual(expected_output, result)

    def test_success(self):  # testing output of success function
        expected_output = "Mission Completed |Congratulations!"
        result = self.asteroid_challenge.success()
        self.assertEqual(expected_output, result)

    def test_display_asteroid_data(self):  # testing out put of display_asteroid_data
        asteroid_output = ["1: 100", "2: 200", "3: 300"]
        expected_output = "1: 100\n2: 200\n3: 300"
        result = self.asteroid_challenge.display_asteroid_data(asteroid_output)
        self.assertEqual(expected_output, result)

    def test_asteroid_distance_prompt(self):  # testing output of asteroid_distance_prompt
        expected_output = "For any of the 3 asteroids that passed near Earth today, enter the miss distance rounded to the nearest km. |You have 3 attempts... "
        result = self.asteroid_challenge.asteroid_distance_prompt()
        self.assertEqual(expected_output, result)

    @patch('builtins.input', return_value="100")  # check this test - failing despite correct mock input???
    def test_player_enter_asteroid_distance_valid(self, mock_input):  # testing valid player input with mocking
        asteroid_distances = ["100", "200", "300"]
        expected_output = self.asteroid_challenge.success()
        result = self.asteroid_challenge.player_enter_asteroid_distance(asteroid_distances, mock_input, attempts=3)
        self.assertEqual(expected_output, result)

    @patch('builtins.input', return_value="100")
    def test_player_enter_asteroid_distance_invalid(self, mock_input):  # testing invalid player input with mocking
        asteroid_distances = ["100", "200", "300"]
        expected_output = f"Incorrect data - try again. |2 attempts remaining...", 2
        result = self.asteroid_challenge.player_enter_asteroid_distance(asteroid_distances, mock_input, attempts=3)
        self.assertEqual(expected_output, result)

    def test_player_enter_asteroid_distance_edge(self):  # if player repeatedly enters edge input for all 3 attempts
        player_input = "one hundred"
        asteroid_distances = ["100", "200", "300"]
        expected_output = "Oh no, Mission Failed!"
        result = self.asteroid_challenge.player_enter_asteroid_distance(asteroid_distances, player_input, attempts = 3)
        self.assertEqual(expected_output, self.asteroid_challenge.fail_message)

    # test for self.asteroid_challenge.get_all_asteroid_data? requires API interaction

    def test_get_3_asteroid_data(self):
        data = {
            "near_earth_objects": {
                "2023-08-15": [
                    {
                        "close_approach_data": [
                            {
                                "miss_distance": {
                                    "kilometers": "1000"
                                }
                            }
                        ]
                    },
                    {
                        "close_approach_data": [
                            {
                                "miss_distance": {
                                    "kilometers": "2000"
                                }
                            }
                        ]
                    },
                    {
                        "close_approach_data": [
                            {
                                "miss_distance": {
                                    "kilometers": "3000"
                                }
                            }
                        ]
                    }
                ]
            }
        }
        today_date_string = "2023-08-15"
        result = self.asteroid_challenge.get_3_asteroid_data(data, today_date_string)


if __name__ == '__main__':
    unittest.main()
