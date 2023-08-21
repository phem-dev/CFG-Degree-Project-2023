import unittest
from unittest.mock import patch
from Missions.Mission2_Satellite_Images_v2 import SatelliteImageDownloader


class TestAsteroidsChallenge(unittest.TestCase):

    def setUp(self):
        # initialising class object to test
        self.satellite_challenge = SatelliteImageDownloader("Satellite Imaging")

    def test_greet(self):
        expected = "Welcome to the Satellite Imaging challenge!"
        result = self.satellite_challenge.greet()
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
