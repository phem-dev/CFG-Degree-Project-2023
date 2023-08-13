import pygame
import random

colours = [
    (0, 0, 225),
    (255, 0, 127),
    (255, 255, 0),
    (120, 7, 255),
    (51, 255, 51),
    (255, 128, 0)
]

class Blocks: 

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Randomly pick type and colour for each block
        self.type = random.randint(0, len(self.blocks) - 1)
        self.colour = random.randint(1, len(colours) - 1)
        self.rotation = 0

    x = 0
    y = 0

    # Maps out positions in a 4 x 4 matrix for each block 
    blocks = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]


    def display_blocks(self):
        return self.blocks[self.type][self.rotation]
    
    def rotate_blocks(self):
        self.rotation = (self.rotation - 1) % len(self.blocks(self.length))


class GamePlay:

    def __init__(self, height, width):
        self.height = height
        self.weight = width
        self.state = "Start"
        self.field = []
        self.score = 0
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    level = 2
    score = 0
    state = "Start"
    field = []
    height = 0
    weight = 0
    x = 100
    y = 60
    zoom = 20
    block = None

    def new_blocks(self, block):
        self.block = block(3, 0)








