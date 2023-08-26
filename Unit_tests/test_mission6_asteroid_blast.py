import unittest
from unittest.mock import Mock, patch, MagicMock
import Missions.Mission6_Asteroid_Blast as mission6
from Missions.asteroid_blast_files import *


class TestAsteroidBlast(unittest.TestCase):
    # @patch('Missions.asteroid_blast_files')
    # @patch('Missions.Mission6_Asteroid_Blast.pygame')
    @patch('pygame.font.Font.render')
    @patch('pygame.Surface.blit')
    def test_show_score(self, mock_blit, mock_render):
        # Create a mock screen
        mock_screen = Mock()

        # Set up the mock font and render return values
        mock_font = Mock()
        mock_render.return_value = mock_surface = Mock()
        mock_surface.get_rect.return_value = Mock(left=0, top=0)

        # Call the function you want to test
        mission6.show_score(10, 10)

        # Assert the expected behavior
        mock_render.assert_called_once_with("Score: 0", True, (255, 255, 255))
        mock_blit.assert_called_once_with(mock_surface, (10, 10))

    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here
    #
    #
    # def test_show_score(self):
    #     self.assertEqual(True, False)
    #
    # def test_game_over_text(self):
    #
    #
    # def test_ship(self):
    #
    #
    # def test_asteroid(self):
    #
    #
    # def test_fire_bullet(self):
    #
    #
    # def test_is_collision(self):
    #     self.assertTrue(is_collision(100, 100, 110, 110))
    #     self.assertFalse(is_collision(100, 100, 200, 200))
    #
    # def test_is_game_over(self):
    #     self.assertTrue(is_game_over(100, 100, 110, 110))
    #     self.assertFalse(is_game_over(100, 100, 200, 200))
    #
    # #
    # def test_is_game_over(self):


    # @patch('Missions.Mission6_Asteroid_Blast.pygame')
    # def test_background(self, mock_pygame):
    #     self.mock_screen = MagicMock()
    #     mock_pygame.display.set_mode.return_value = self.mock_screen
    #     # initializing class object to test
    #     self.BackGround = Background('Missions/asteroid_blast_files/asteroid_bg.png', [0,0])




if __name__ == '__main__':
    unittest.main()
