# run in terminal using: python3 -m unittest Missions.Mission6_blast_files.test_mission6_blast


import unittest
from unittest.mock import patch, MagicMock
from Missions.Mission6_blast_files.mission6_blast import Background
from Scene_files.background import *


class TestAsteroidBlast(unittest.TestCase):

    @patch('Missions.Mission6_blast_files.mission6_blast.pygame')
    def test_background(self, mock_pygame):
        self.mock_screen = MagicMock()
        mock_pygame.display.set_mode.return_value = self.mock_screen
        # initializing class object to test
        self.BackGround = Background(os.path.join(root_dir, 'Missions/Mission6_blast_files/Mission6_asteroid_blast_assets/asteroid_bg.png'), [0, 0])

if __name__ == '__main__':
    unittest.main()

