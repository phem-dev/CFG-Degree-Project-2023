import unittest
from unittest.mock import patch
from Missions.Mission2_Satellite_Images import SatelliteImageDownloader


class TestAsteroidsChallenge(unittest.TestCase):

    def setUp(self):
        # initialising class object to test
        self.satellite_challenge = SatelliteImageDownloader("Satellite Imaging")





if __name__ == '__main__':
    unittest.main()