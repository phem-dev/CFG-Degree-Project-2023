import unittest
from unittest.mock import Mock, patch, MagicMock
from Missions.Mission3_mars_files.mission3_mars import MarsRoverViewer

class TestMarsRoverViewer(unittest.TestCase):

    # Using patch to mock the pygame and requests modules for testing
    @patch('Missions.Mission3_mars_files.mission3_mars.pygame')
    @patch('Missions.Mission3_mars_files.mission3_mars.requests')
    def setUp(self, mock_requests, mock_pygame):
        # Creating a mock screen using MagicMock to simulate Pygame screen
        self.mock_screen = MagicMock()
        mock_pygame.display.set_mode.return_value = self.mock_screen
        # Creating an instance of MarsRoverViewer for testing
        self.viewer = MarsRoverViewer()

    # Testing valid input for the is_valid function
    def test_is_valid_valid_input(self):
        self.assertTrue(self.viewer.is_valid("2"))

    # Testing invalid input for the is_valid function
    def test_is_valid_invalid_input(self):
        self.assertFalse(self.viewer.is_valid("abc"))

    # Testing successful fetch of previous images from NASA API
    @patch('Missions.Mission3_mars_files.mission3_mars.requests.get')
    def test_fetch_previous_images_success(self, mock_get):
        # Creating a mock response with image data
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "photos": [
                {"img_src": "image_url_1"},
                {"img_src": "image_url_2"}
            ]
        }
        mock_get.return_value = mock_response

        # Calling the fetch_previous_images function
        images_data = self.viewer.fetch_previous_images("RHAZ", num_images=2)
        self.assertEqual(len(images_data), 2)

    # Testing failure to fetch previous images from NASA API
    @patch('Missions.Mission3_mars_files.mission3_mars.requests.get')
    def test_fetch_previous_images_failure(self, mock_get):
        # Creating a mock response with status code 404
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Calling the fetch_previous_images function
        images_data = self.viewer.fetch_previous_images("RHAZ", num_images=2)
        self.assertIsNone(images_data)


# Running the unit tests
if __name__ == '__main__':
    unittest.main()