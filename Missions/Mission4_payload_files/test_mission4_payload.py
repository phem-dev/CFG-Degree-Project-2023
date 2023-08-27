import unittest
from Missions.Mission4_payload_files.mission4_payload import Tetromino, GamePlay, colours

class TestTetromino(unittest.TestCase):ß

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

    # Test handle_intersections() with no obstacles 
    def test_handle_intersections_no_intersection(self):
        
        tetromino = Tetromino(0, 0)
        self.game.tetromino = tetromino
        self.game.field = [[0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0]]
        intersects = self.game.handle_intersections()
        self.assertFalse(intersects)

    # Test handle_intersections() with tetromino
    def test_handle_intersections_with_intersection(self):
            
            tetromino = Tetromino(0, 0)
            self.game.tetromino = tetromino
            self.game.field = [[0, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 0, 0],
                                [0, 0, 0, 0]]
            intersects = self.game.handle_intersections()
            self.assertTrue(intersects)

    
    # Test handle_intersections() with multiple tetrominoes
    def test_handle_intersections_multiple_blocks_intersection(self):

        tetromino = Tetromino(1, 1)
        self.game.tetromino = tetromino
        self.game.field = [[0, 0, 0, 0],
                            [0, 1, 1, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0]]
        intersects = self.game.håandle_intersections()
        self.assertTrue(intersects)


    
    # test halt_tetromino

    # test delete_line



    # test move_space


    # test move_down

    # test move_to_side


if __name__ == '__main__':
    unittest.main()
