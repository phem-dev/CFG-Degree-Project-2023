import unittest
from unittest.mock import patch, Mock, mock_open
from Scene_files.Scenes import SceneEnd  # Adjust import according to your module structure

# Mock the font before importing modules that depend on it
with patch('pygame.font.Font', Mock()):
    from Scene_files.Scenes import SceneEnd


class TestSceneEnd(unittest.TestCase):
    """
    Unit tests for the SceneEnd class in the Pygame game.
    """

    @patch("builtins.open", new_callable=mock_open, read_data="Bizz")
    def test_get_saved_name(self, mock_file):
        """
        Test if the get_saved_name method correctly fetches the player name from the file.
        """
        scene = SceneEnd(None, None)
        player_name = scene.get_saved_name()
        self.assertEqual(player_name, "Bizz")

    @patch("builtins.open", new_callable=mock_open, read_data="Bizz")
    def test_initialization(self, mock_file):
        """
        Test if the SceneEnd class initializes with the player name embedded in the typewriter_block text.
        """
        scene = SceneEnd(None, None)
        self.assertIn("Bizz", scene.typewriter_block.text)  # Assuming typewriter_block has a 'text' attribute

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_get_saved_name_file_not_found(self, mock_file):
        """
        Test if the get_saved_name method correctly handles the scenario when the file does not exist.
        """
        scene = SceneEnd(None, None)
        player_name = scene.get_saved_name()
        self.assertIsNone(player_name)


if __name__ == "__main__":
    unittest.main()
