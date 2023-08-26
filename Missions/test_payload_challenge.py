import unittest
import pygame
from payload_challenge import Tetromino, GamePlay, colours 

class TestTetromino(unittest.TestCase):

    def test_tetromino(self):
        tetromino = Tetromino(0, 0)
        self.assertEqual(tetromino.x, 0)
        self.assertEqual(tetromino.y, 0)
        self.assertIn(tetromino.type, range(len(Tetromino.tetrominoes)))
        self.assertIn(tetromino.colour, range(1, len(colours)))
        self.assertEqual(tetromino.rotation, 0)

    def test_display_tetrominoes(self):
        tetromino = Tetromino(0, 0)
        tetromino.type = 0
        tetromino.rotation = 1
        configuration = tetromino.tetrominoes[tetromino.type][tetromino.rotation]
        result = tetromino.display_tetrominoes()
        self.assertEqual(result, configuration)


    def test_rotate_tetrominoes(self):
        tetromino = Tetromino(0, 0)
        initial_rotation = tetromino.rotation
        tetromino.rotate_tetrominoes()
        self.assertEqual(tetromino.rotation, (initial_rotation + 1) % len(tetromino.tetrominoes[tetromino.type]))

class TestGamePlay(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.game = GamePlay(20, 10)

    def test_gameplay(self):
        self.assertEqual(self.game.height, 20)
        self.assertEqual(self.game.width, 10)
        self.assertEqual(self.game.level, 2)
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.state, "start")
        self.assertIsNotNone(self.game.field)
        self.assertIsNone(self.game.tetromino)

    def test_new_tetrominoes(self):
        self.game.new_tetrominoes()
        self.assertIsNotNone(self.game.tetromino)

    
    def test_handle_intersections_no_intersect(self):
        game = GamePlay(800, 600)
        tetromino = Tetromino(1, 1)
        game.field = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
        game.tetromino = tetromino
        result = game.handle_intersections()
        self.assertFalse(result)


    # def test_handle_intersections_with_intersect(self):
    #     game = GamePlay(800, 600)
    #     tetromino = Tetromino(1, 1)
    #     game.field = [[0, 0, 0, 0],
    #                   [0, 1, 0, 0],
    #                   [0, 0, 0, 0],
    #                   [0, 0, 0, 0]]
    #     game.tetromino = tetromino
    #     result = game.handle_intersections()
    #     self.assertTrue(result)



    def test_halt_tetromino(self):
        pass


    def test_delete_line(self):
        pass



if __name__ == '__main__':
    unittest.main()
