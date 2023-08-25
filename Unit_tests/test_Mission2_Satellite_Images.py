import unittest
from unittest.mock import patch
from Missions.Mission2_Satellite_Images import Satellite


class TestAsteroidsChallenge(unittest.TestCase):

    def setUp(self):
        # Initializing class object to test
        self.challenge = Satellite("Satellite Imaging")

    def test_greet(self):
        # Testing greet method
        expected_output = ("Welcome to the Satellite Imaging challenge!|",
                           self.challenge.challenge_description,
                           ("Capturing Satellite Images", self.challenge.download_images()))

        self.assertEqual(self.challenge.greet(), expected_output)

    def test_capture_images(self):
        expected_messages = ("Capturing Satellite Images", self.challenge.download_images())
        self.assertEqual(self.challenge.capture_images(), expected_messages)

    @patch("random.randint", return_value=1)  # Mocking random.randint to always return 1
    def test_random_question(self, mock_randint):
        expected_question = {"Select the city with the most cloud|coverage...": 2}
        self.assertEqual(self.challenge.random_question(), expected_question)

    def test_success(self):
        expected_success_message = "Correct - Mission Completed!"
        self.assertEqual(self.challenge.success(), expected_success_message)

    @patch("random.randint", return_value=1)  # Mocking random.randint to always return 1
    def test_fail(self, mock_randint):
        expected_fail_message = ("Oh no, incorrect answer! Let's try again...",
                                 {"Select the city with the most cloud|coverage...": 2})
        self.assertEqual(self.challenge.fail(), expected_fail_message)



if __name__ == '__main__':
    unittest.main()
