import unittest
from unittest.mock import patch
from Missions.Mission2_Satellite_Images import Challenge

class TestAsteroidsChallenge(unittest.TestCase):

    def setUp(self):
        # Initializing class object to test
        self.challenge = Challenge("Satellite Imaging")

    def test_greet(self):
        # Testing greet method
        expected_output = ("Welcome to the Satellite Imaging challenge!|",
                           self.challenge.challenge_description,
                           ("Capturing Satellite Images", self.challenge.download_images()))

        self.assertEqual(self.challenge.greet(), expected_output)

    @patch("builtins.input", side_effect=[""])
    def test_capture_images(self, mock_input):
        # Testing capture_images method
        expected_output = ("Capturing Satellite Images", self.challenge.download_images())

        self.assertEqual(self.challenge.capture_images(), expected_output)

    def test_download_images(self):
        # Testing download_images method
        expected_output = (["Downloading image 1: Reykjavík, Iceland...|",
                            "Downloading image 2: Lima, Peru...|",
                            "Downloading image 3: Beijing, China...|"], None)  # Adding None as this function calls
        # another one in the actual code file, need to account for this in testing. Once PyGame image rendering added
        # to code file, change None here to whatever the Returned value for the render_image fn is

        self.assertEqual(self.challenge.download_images(), expected_output)

    def test_correct_answer(self):
        # Testing correct_answer method
        self.challenge.display_question = "question_1"
        self.assertEqual(self.challenge.correct_answer(), 2)

        self.challenge.display_question = "question_2"
        self.assertEqual(self.challenge.correct_answer(), 1)

        self.challenge.display_question = "question_3"
        self.assertEqual(self.challenge.correct_answer(), 3)

    @patch("builtins.input", side_effect=[1])
    def test_answer_correct(self, mock_input):
        # Testing answer method for correct answer
        correct_ans = self.challenge.correct_answer()  # Get the correct answer
        result = self.challenge.answer(correct_ans)  # Pass the correct answer to the answer method
        self.assertTrue(result)

    @patch("builtins.input", side_effect=[2])
    def test_answer_incorrect(self, mock_input):
        # Testing answer method for incorrect answer
        result = self.challenge.answer(1)
        self.assertFalse(result)

    def test_correct_response(self):
        # Testing correct_response method
        expected_output = "Correct - Mission Completed!"
        self.assertEqual(self.challenge.correct_response(), expected_output)

    def test_incorrect_response(self):
        # Testing incorrect_response method
        expected_output = "Oh no, incorrect answer! Let's try again...", self.challenge.random_question()
        self.assertEqual(self.challenge.incorrect_response(), expected_output)

if __name__ == '__main__':
    unittest.main()
