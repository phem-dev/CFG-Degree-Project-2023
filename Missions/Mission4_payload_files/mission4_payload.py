import pygame
import random
from Scene_files.background import *

# Define colours for tetrominoes
colours = [
    (104, 187, 66),
    (232, 106, 23),
    (255, 204, 0),
    (157, 75, 199),
    (30, 167, 225),
    (21, 193, 231)
]

class Tetromino: 

    def __init__(self, x, y):
        """
            Initialise Tetromino class. 

            Randomly pick attributes for each tetromino.
        """
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.tetrominoes) - 1)
        self.colour = random.randint(1, len(colours) - 1)
        self.rotation = 0

    # Maps out positions in a 4 x 4 matrix for each solid tetromino. Inner list contains rotations
    tetrominoes = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]


    def display_tetrominoes(self):
        """
            Display and return current rotation of tetromino
        """
        return self.tetrominoes[self.type][self.rotation]
    
    def rotate_tetrominoes(self):
        """
            Rotate tetromino
        """
        self.rotation = (self.rotation + 1) % len(self.tetrominoes[self.type])


class GamePlay:

    def __init__(self, height, width):
        """
            Initialise GamePlay class with and set attributes. 

            Draw a game field of height * width with no tetrominoes in the field and 
            game state set to "start". 
        """
        self.height = height
        self.width = width
        self.level = 2
        self.score = 0
        # Are we playing the game?
        self.state = "start"
        # Contains 0 where field is empty, colours where there are tetrominoes
        self.field = []
        self.x = 300
        self.y = 60
        self.zoom = 20
        self.tetromino = None

        for _ in range(height):
            new_line = []
            for _ in range(width):
                new_line.append(0)
            self.field.append(new_line)


    def new_tetrominoes(self):
        """
            Create new tetrominoes at co-ords of 3, 0.
        """
        self.tetromino = Tetromino(3, 0)


    def handle_intersections(self):
        """
            Handle intersections of tetrominoes. 

            Check the current position of the tetromino and whether it has any collisions
            with the game boundaries or other tetrominoes. 

            If there is a collision, set intersects to True. Else, intersects = False. 
        """
        intersects = False
        for i in range(4):
            for j in range(4):
                # Check if each tetromino is within bounds of game
                if i * 4 + j in self.tetromino.display_tetrominoes():
                    # Check if tetromino intersects with another. If 0, safe to move. 
                    if i + self.tetromino.y > self.height - 1 or j + self.tetromino.x > self.width - 1 or j + self.tetromino.x < 0 or self.field[i + self.tetromino.y][j + self.tetromino.x] > 0:
                        intersects = True
        return intersects
    

    def halt_tetromino(self):
        """
            Pause tetromino in the field. 
            
            If there is a complete horizontal line, delete the line and create a new tetromino. 
            
            If handle_intersections() is True, set game.state to "gameover".
        """
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.tetromino.display_tetrominoes():
                    self.field[i + self.tetromino.y][j + self.tetromino.x] = self.tetromino.colour
        self.delete_line()
        self.new_tetrominoes()
        if self.handle_intersections():
            game.state = "gameover"

    # Check if there is a complete horizontal line
    def delete_line(self):
        """
            Check if there is a complete horizontal line in the game field. 

            If zeros == 0, the row is filled with non-zero values, indicating a complete line. 

            If there is a complete line, delete the line and increase the score by 1 for each line deleted.

        """

        # Create a count for number of lines deleted
        lines = 0 
        # Iterate over rows in the game field
        for i in range(1, self.height):
            zeros = 0
            # Iterate over columns within each row
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            # Handle line deletion
            if zeros == 0:
                lines += 1
                for k in range(i, 0, -1):
                    for j in range(self.width):
                        self.field[k][j] = self.field[k - 1][j]

        # Square score - clearing multiple lines at once scores the player more points     
        self.score += lines ** 2
    
    # Move tetrominoes - define last position, change co-ords and check handle_intersections(). If True, return to previous state. 
    def move_space(self):
        """
            Move tetromino down the field until it encounters an intersection: 

                While handle_intersections() is false: Increment verticle position of current tetromino by 1 to move the the tetromino down the game board. 

                Once tetromino encounters an intersection, decrement vertical position by 1 to reach last valid position. 

                Call halt_tetromino method. 
        """
        while not self.handle_intersections():
            self.tetromino.y += 1
        self.tetromino.y -= 1
        self.halt_tetromino()

    def move_down(self):
        """
            Move tetromino down one row. 

            If handle_intersections() == True
                Move tetromino to last valid position
                Call halt_tetromino() method 
        """
        self.tetromino.y += 1
        if self.handle_intersections():
            self.tetromino.y -= 1
            self.halt_tetromino()

    def move_to_side(self, dx):
        """
            Args: dx = horizontal distance tetromino should move
            +ve = move right
            -ve = move left 

            Store current horizontal position of tetromino 
            (in case it needs to be moved back). 
            Update horizontal position of tetromino depending on value of dx. 
            Check for intersections. If handle_intersections() == True, 
            move tetromino back to old position. 

        """
        old_x = self.tetromino.x
        self.tetromino.x += dx
        if self.handle_intersections():
            self.tetromino.x = old_x 
    
    def rotate_tetrominoes(self):
        """
            Try to rotate tetromino. 

            If rotation results in handle_intersections() == True, 
            return tetromino to previous_rotation. 
        """
        previous_rotation = self.tetromino.rotation
        self.tetromino.rotate_tetrominoes()
        if self.handle_intersections():
            self.tetromino.rotation = previous_rotation

# Initialise game
pygame.init()

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)

# Set size of board
size = (800, 600)
screen = pygame.display.set_mode(size)

# pygame.display.set_caption("Stratobus Payload Challenge")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
fps = 25
game = GamePlay(20, 10)
counter = 0

pressing_down = False

# While player has not decided to exit the game: 
while not done:
    # If there is no active tetromino, create a new one 
    if game.tetromino is None:
        game.new_tetrominoes()
    counter += 1
    if counter > 100000:
        counter = 0

    # Conditions that result in a tetromino moving down the board
    if counter % (fps // game.level // 2) == 0 or pressing_down:
        if game.state == "start":
            game.move_down()

    # Event handling for key strokes 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate_tetrominoes()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                game.move_to_side(-1)
            if event.key == pygame.K_RIGHT:
                game.move_to_side(1)
            if event.key == pygame.K_SPACE:
                game.move_space()
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.K_RETURN:
                game.__init__(20, 10)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
            pressing_down = False

    screen.fill(white)
    screen.blit(BackGround_payload_new.image, BackGround_payload_new.rect)

    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, grey, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, colours[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 2])


    """
        Iterate through 4 * 4 grid.
        Check if each cell is part of an active tetromino. 
        If it is, draw a tetromino. 
        Repeat for all cells in the shape of the tetromino type, 
        taking into account current position and rotation. 
    """
    if game.tetromino is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.tetromino.display_tetrominoes():
                    pygame.draw.rect(screen, colours[game.tetromino.colour],
                                     [game.x + game.zoom * (j + game.tetromino.x) + 1,
                                      game.y + game.zoom * (i + game.tetromino.y) + 1,
                                      game.zoom - 2, game.zoom - 2])


    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 65, True, False)
    font2 = pygame.font.SysFont('Calibri', 45, True, False)
    text = font.render("Score: " + str(game.score), True, black)
    text_game_over = font1.render("Game Over", True, (255, 0, 0))
    text_esc = font2.render("Press ESC to exit", True, white)
    text_play_again = font2.render("Press RTN to play again", True, white)

    screen.blit(text, [0, 0])
    if game.state == "gameover":
        screen.blit(text_game_over, [230, 200])
        screen.blit(text_esc, [210, 270])
        screen.blit(text_play_again, [150, 330])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()

