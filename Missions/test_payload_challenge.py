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
        # compare current rotation with expected
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

    
    # def test_handle_intersections_no_intersect(self):
    #     game = GamePlay(800, 600)
    #     tetromino = Tetromino(1, 1)
    #     game.field = [[0, 0, 0, 0],
    #                   [0, 0, 0, 0],
    #                   [0, 0, 0, 0],
    #                   [0, 0, 0, 0]]
    #     game.tetromino = tetromino
    #     result = game.handle_intersections()
    #     self.assertFalse(result)


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



    # def test_halt_tetromino_gameover(self):
    #     game = GamePlay(800, 600)
    #     tetromino = Tetromino(1, 1)
    #     game.field = [[0, 0, 0, 0],
    #                   [0, 1, 0, 0],
    #                   [0, 0, 0, 0],
    #                   [0, 0, 0, 0]]
    #     game.tetromino = tetromino
    #     result = game.halt_tetromino()
    #     self.assertEqual(game.state, "gameover")


        # def test_halt_tetromino_resume(self):
    #     game = GamePlay(800, 600)
    #     tetromino = Tetromino(1, 1)
    #     game.field = [[0, 0, 0, 0],
    #                   [0, 1, 0, 0],
    #                   [0, 0, 0, 0],
    #                   [0, 0, 0, 0]]
    #     game.tetromino = tetromino
    #     result = game.halt_tetromino()
    #     self.assertEqual(game.state, "gameover")


    # def test_delete_line_single(self):
    #     game = GamePlay(800, 600)
    #     game.field = [[1, 1, 1, 1],
    #                   [0, 0, 0, 0],
    #                   [0, 0, 0, 0],
    #                   [0, 0, 0, 0]]
    #     game.score = 0
    #     game.delete_line()
    #     self.assertEqual(game.field, [[0, 0, 0, 0],
    #                   [1, 1, 1, 1],
    #                   [0, 0, 0, 0],
    #                   [0, 0, 0, 0]])
    #     self.assertEqual(game.state, 1)


    # def test_delete_line_multiple(self):
    #     game = GamePlay(800, 600)
    #     game.field = [[1, 1, 1, 1],
    #                   [1, 1, 1, 1],
    #                   [0, 0, 0, 0],
    #                   [0, 0, 0, 0]]
    #     game.score = 0
    #     game.delete_line()
    #     self.assertEqual(game.field, [[0, 0, 0, 0],
    #                   [0, 0, 0, 0],
    #                   [1, 1, 1, 1],
    #                   [1, 1, 1, 1]])
    #     self.assertEqual(game.state, 4)

    
    # def test_delete_line_none(self):
    #     game = GamePlay(800, 600)
    #     game.field = [[1, 0, 1, 0],
    #                   [0, 1, 0, 1],
    #                   [1, 0, 1, 0],
    #                   [0, 1, 0, 1]]
    #     game.score = 0
    #     game.delete_line()
    #     self.assertEqual(game.field, [[1, 0, 1, 0],
    #                                    [0, 1, 0, 1],
    #                                    [1, 0, 1, 0],
    #                                    [0, 1, 0, 1]])
    #     self.assertEqual(game.state, 0)

#    def test_move_space_with_intersection(self):
#         # Assuming you have a Game class with known attributes and methods
#         # Initialize your Game object here or replace it with actual initialization
        
#         # Create a scenario where there should be an intersection
#         game = Game()
#         tetromino = Tetromino()
        
#         # Modify the tetromino's position and the game field to create an intersection
#         tetromino.x = 1
#         tetromino.y = 1
#         game.field = [[0, 0, 0, 0],
#                       [0, 1, 0, 0],
#                       [0, 0, 0, 0],
#                       [0, 0, 0, 0]]
        
#         # Set the tetromino for the game
#         game.tetromino = tetromino
        
#         # Call the method you want to test
#         game.move_space()
        
#         # Assert that the tetromino should be halted (y coordinate adjusted back)
#         self.assertEqual(game.tetromino.y, 0)

#     def test_move_space_without_intersection(self):
#         # Assuming you have a Game class with known attributes and methods
#         # Initialize your Game object here or replace it with actual initialization
        
#         # Create a scenario where there should be no intersection
#         game = Game()
#         tetromino = Tetromino()
        
#         # Modify the tetromino's position and the game field to avoid an intersection
#         tetromino.x = 0
#         tetromino.y = 0
#         game.field = [[0, 0, 0, 0],
#                       [0, 0, 0, 0],
#                       [0, 0, 0, 0],
#                       [0, 0, 0, 0]]
        
#         # Set the tetromino for the game
#         game.tetromino = tetromino
        
#         # Call the method you want to test
#         game.move_space()
        
#         # Assert that the tetromino should reach the bottom (y coordinate adjusted)
#         self.assertEqual(game.tetromino.y, 3)

#     def test_move_down_with_intersection(self):
#         # Assuming you have a Game class with known attributes and methods
#         # Initialize your Game object here or replace it with actual initialization
        
#         # Create a scenario where there should be an intersection
#         game = Game()
#         tetromino = Tetromino()
        
#         # Modify the tetromino's position and the game field to create an intersection
#         tetromino.x = 1
#         tetromino.y = 1
#         game.field = [[0, 0, 0, 0],
#                       [0, 1, 0, 0],
#                       [0, 0, 0, 0],
#                       [0, 0, 0, 0]]
        
#         # Set the tetromino for the game
#         game.tetromino = tetromino
        
#         # Call the method you want to test
#         game.move_down()
        
#         # Assert that the tetromino should be halted (y coordinate adjusted back)
#         self.assertEqual(game.tetromino.y, 0)

#     def test_move_down_without_intersection(self):
#         # Assuming you have a Game class with known attributes and methods
#         # Initialize your Game object here or replace it with actual initialization
        
#         # Create a scenario where there should be no intersection
#         game = Game()
#         tetromino = Tetromino()
        
#         # Modify the tetromino's position and the game field to avoid an intersection
#         tetromino.x = 0
#         tetromino.y = 0
#         game.field = [[0, 0, 0, 0],
#                       [0, 0, 0, 0],
#                       [0, 0, 0, 0],
#                       [0, 0, 0, 0]]
        
#         # Set the tetromino for the game
#         game.tetromino = tetromino
        
#         # Call the method you want to test
#         game.move_down()
        
#         # Assert that the tetromino should move down one position (y coordinate adjusted)
#         self.assertEqual(game.tetromino.y, 1)

#     def test_move_to_side_with_intersection(self):
#         # Assuming you have a Game class with known attributes and methods
#         # Initialize your Game object here or replace it with actual initialization
        
#         # Create a scenario where there should be an intersection
#         game = Game()
#         tetromino = Tetromino()
        
#         # Modify the tetromino's position and the game field to create an intersection
#         tetromino.x = 2
#         tetromino.y = 0
#         game.field = [[0, 0, 0, 0],
#                       [0, 1, 0, 0],
#                       [0, 0, 0, 0],
#                       [0, 0, 0, 0]]
        
#         # Set the tetromino for the game
#         game.tetromino = tetromino
        
#         # Call the method you want to test
#         game.move_to_side(1)
        
#         # Assert that the tetromino should be halted (x coordinate adjusted back)
#         self.assertEqual(game.tetromino.x, 2)

#     def test_move_to_side_without_intersection(self):
#         # Assuming you have a Game class with known attributes and methods
#         # Initialize your Game object here or replace it with actual initialization
        
#         # Create a scenario where there should be no intersection
#         game = Game()
#         tetromino = Tetromino()
        
#         # Modify the tetromino's position and the game field to avoid an intersection
#         tetromino.x = 0
#         tetromino.y = 0
#         game.field = [[0, 0, 0, 0],
#                       [0, 0, 0, 0],
#                       [0, 0, 0, 0],
#                       [0, 0, 0, 0]]
        
#         # Set the tetromino for the game
#         game.tetromino = tetromino
        
#         # Call the method you want to test
#         game.move_to_side(1)
        
#         # Assert that the tetromino should move to the side (x coordinate adjusted)
#         self.assertEqual(game.tetromino.x, 1)



if __name__ == '__main__':
    unittest.main()
