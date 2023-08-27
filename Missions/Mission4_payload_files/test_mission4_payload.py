import unittest
from Missions.Mission4_payload_files.mission4_payload import Block, GamePlay, colours

class TestBlock(unittest.TestCase):

    def setUp(self):
        self.block = Block(3, 0)

    def test_initialization(self):
        self.assertEqual(self.block.x, 3)
        self.assertEqual(self.block.y, 0)
        self.assertTrue(self.block.type in range(len(self.block.blocks)))
        self.assertTrue(self.block.colour in range(1, len(colours)))

    def test_display_blocks(self):
        self.assertTrue(isinstance(self.block.display_blocks(), list))

    def test_rotate_blocks(self):
        prev_rotation = self.block.rotation
        self.block.rotate_blocks()
        self.assertEqual(self.block.rotation, (prev_rotation + 1) % len(self.block.blocks[self.block.type]))

class TestGamePlay(unittest.TestCase):

    def setUp(self):
        self.gameplay = GamePlay(20, 10)

    def test_initialization(self):
        self.assertEqual(self.gameplay.height, 20)
        self.assertEqual(self.gameplay.width, 10)
        self.assertEqual(len(self.gameplay.field), 20)
        for line in self.gameplay.field:
            self.assertEqual(len(line), 10)

    def test_new_blocks(self):
        self.gameplay.new_blocks()
        self.assertIsNotNone(self.gameplay.block)
        self.assertEqual(self.gameplay.block.x, 3)
        self.assertEqual(self.gameplay.block.y, 0)

    # You can add more methods to test specific functionalities of your game.

if __name__ == '__main__':
    unittest.main()
