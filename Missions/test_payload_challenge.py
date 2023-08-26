import unittest
import pygame
from payload_challenge import Tetromino, GamePlay, colours 

class TestTetromino(unittest.TestCase):

    # Check Tetromino object is initialised with correct class attributes
    def test_tetromino(self):
        tetromino = Tetromino(0, 0)
        self.assertEqual(tetromino.x, 0)
        self.assertEqual(tetromino.y, 0)
        self.assertIn(tetromino.type, range(len(Tetromino.tetrominoes)))
        self.assertIn(tetromino.colour, range(1, len(colours)))
        self.assertEqual(tetromino.rotation, 0)


    # Check display_tetrominoes() returns expected coniguration of a tetromino
    def test_display_tetrominoes(self):
        tetromino = Tetromino(0, 0)
        tetromino.type = 0
        tetromino.rotation = 1
        configuration = tetromino.tetrominoes[tetromino.type][tetromino.rotation]
        # Return current configuration of tetromino 
        result = tetromino.display_tetrominoes()
        self.assertEqual(result, configuration)


    # Check rotate_tetrominoes() returns next rotation
    def test_rotate_tetrominoes(self):
        tetromino = Tetromino(0, 0)
        initial_rotation = tetromino.rotation
        tetromino.rotate_tetrominoes()
        # Compare current rotation with expected
        self.assertEqual(tetromino.rotation, (initial_rotation + 1) % len(tetromino.tetrominoes[tetromino.type]))


class TestGamePlay(unittest.TestCase):

    # Set up conditions required for following test cases 
    def setUp(self):
        pygame.init()
        self.game = GamePlay(800, 600)

    # Check initial state of GamePlay object matches expected values for start of game
    def test_gameplay_start(self):
        self.assertEqual(self.game.height, 800)
        self.assertEqual(self.game.width, 600)
        self.assertEqual(self.game.level, 2)
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.state, "start")
        self.assertIsNotNone(self.game.field)
        self.assertIsNone(self.game.tetromino)


    def test_new_tetrominoes(self):
        self.game.new_tetrominoes()
        # Check new tetromino has been created
        self.assertIsNotNone(self.game.tetromino)


if __name__ == '__main__':
    unittest.main()
