import unittest
from unittest.mock import patch, MagicMock
from Missions.Mission5_ISS import ISSTracker


class TestISSTracker(unittest.TestCase):
    @patch('requests.get')  # Mock the requests.get function
    def test_get_iss_location(self, mock_requests_get):
        # Mock the response JSON data
        mock_response = {"iss_position": {"latitude": "45.0", "longitude": "-75.0"}}
        mock_requests_get.return_value.json.return_value = mock_response

        # Create an instance of ISSTracker
        tracker = ISSTracker()
        lat, lon = tracker.get_iss_location()

        # Check if the latitude and longitude are as expected
        self.assertEqual(lat, 45.0)
        self.assertEqual(lon, -75.0)

    @patch('geopy.geocoders.Nominatim.reverse')  # Mock the geopy.geocoders.Nominatim.reverse method
    @patch.object(ISSTracker, 'translate_to_english')  # Mock the translate_to_english method
    def test_get_closest_country(self, mock_translate, mock_reverse):
        # Create a mock Location object with relevant data
        mock_location = MagicMock()
        mock_location.raw = {'address': {'country': 'Some Country'}}
        mock_reverse.return_value = [mock_location]

        # Mock the translation function's behavior
        mock_translate.return_value = 'Translated Country'

        # Create an instance of ISSTracker
        tracker = ISSTracker()
        closest_country = tracker.get_closest_country(45.0, -75.0)

        # Check if the closest country name is as expected
        self.assertEqual(closest_country, 'Translated Country')


# Running the unit tests
if __name__ == '__main__':
    unittest.main()
