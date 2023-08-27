# run in terminal using: python3 -m unittest Unit_tests.test_mission6_asteroid_blast


import unittest
from unittest.mock import Mock, patch, MagicMock
from Missions.Mission6_blast_ import *
from Scene_files.background import *


class TestAsteroidBlast(unittest.TestCase):

    @patch('Missions.Mission6_Asteroid_Blast.pygame')
    def test_background(self, mock_pygame):
        self.mock_screen = MagicMock()
        mock_pygame.display.set_mode.return_value = self.mock_screen
        # initializing class object to test
        self.BackGround = Background('Missions/asteroid_blast_files/asteroid_bg.png', [0, 0])


if __name__ == '__main__':
    unittest.main()
