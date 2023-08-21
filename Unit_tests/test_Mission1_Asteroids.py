import unittest
from unittest.mock import patch
from Missions.Mission1_Asteroids import Asteroids


class TestAsteroidsChallenge(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up any common data or configuration here
        pass

    def setUp(self):
        # Set up data for each test method
        self.asteroid_challenge = Asteroids("Asteroid Proximity Sensor")

    def test_greet(self):
        expected_output = "Welcome to the Asteroid Proximity Sensor challenge!"
        result = self.asteroid_challenge.greet()
        self.assertEqual(expected_output, result)

    def test_success(self):
        expected_output = "Mission Completed |Congratulations!"
        result = self.asteroid_challenge.success()
        self.assertEqual(expected_output, result)

    def test_display_asteroid_data(self):
        asteroid_output = ["1: 100", "2: 200", "3: 300"]
        expected_output = "1: 100\n2: 200\n3: 300"
        result = self.asteroid_challenge.display_asteroid_data(asteroid_output)
        self.assertEqual(expected_output, result)

    def test_asteroid_distance_prompt(self):
        expected_output = "For any of the 3 asteroids that passed near Earth today, enter the miss distance rounded to the nearest km. |You have 3 attempts... "
        result = self.asteroid_challenge.asteroid_distance_prompt()
        self.assertEqual(expected_output, result)

    @patch('builtins.input', return_value="100")
    def test_player_enter_asteroid_distance(self, mock_input):
        asteroid_distances = ["100", "200", "300"]
        expected_output = self.asteroid_challenge.success()
        result = self.asteroid_challenge.player_enter_asteroid_distance(asteroid_distances, "100", attempts=3)
        self.assertEqual(expected_output, result)

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
