import pygame
import random

# Define colours for blocks
colours = [
    (104, 187, 66),
    (232, 106, 23),
    (255, 204, 0),
    (157, 75, 199),
    (30, 167, 225),
    (21, 193, 231)
]

class Block: 

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Randomly pick type and colour for each block
        self.type = random.randint(0, len(self.blocks) - 1)
        self.colour = random.randint(1, len(colours) - 1)
        self.rotation = 0

    x = 0
    y = 0

    # Maps out positions in a 4 x 4 matrix for each solid block. Inner list contains rotations
    blocks = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]

    # Rotate figures and get current rotation
    def display_blocks(self):
        return self.blocks[self.type][self.rotation]
    
    def rotate_blocks(self):
        self.rotation = (self.rotation + 1) % len(self.blocks(self.type))


class GamePlay:

    # Create a field of the size width x height
    def __init__(self, height, width):
        self.height = 0
        self.width = 0
        self.level = 2
        self.score = 0
        # Are we playing the game?
        self.state = "start"
        # Contains 0 where field is empty, colours where there are blocks
        self.field = []
        self.x = 100
        self.y = 60
        self.zoom = 20
        self.block = None

        for h in range(height):
            new_line = []
            for w in range(width):
                new_line.append(0)
            self.field.append(new_line)

    # Create new block at co-ords of 3, 0
    def new_blocks(self):
        self.block = Block(3, 0)

    # Handle intersections of blocks
    def handle_intersections(self):
        intersects = False
        for i in range(4):
            for j in range(4):
                # Check if each block is within bounds of game
                if i * 4 + j in self.block.display_blocks():
                    # Check if block is touching another. If 0, safe to move. 
                    if i + self.block.y > self.height - 1 or j + self.block.x > self.width - 1 or j + self.block.x < 0 or self.field[i + self.block.y][j + self.block.x] > 0:
                        intersects = True
        return intersects
    
    # Pause block in the field. If there is a complete horizontal line, create a new figure. If not, game over :(
    def halt_block(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.block.display_blocks():
                    self.field[i + self.block.y][j + self.block.x] = self.block.colour
                    self.delete_line()
                    self.new_blocks()
                    if self.handle_intersections():
                        game.state = "gameover"

    # Check if there is a complete horizontal line
    def delete_line(self):
        lines = 0 
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i][j] = self.field[i - 1]
            
            self.score += lines ** 2
    
    # Move blocks - define last position, change co-ords and check handle_intersections(). If True, return to previous state. 
    def move_space(self):
        while not self.handle_intersections():
            self.block.y += 1
        self.block.y -= 1
        self.halt_block()

    def move_down(self):
        self.block.y += 1
        if self.handle_intersections():
            self.block.y -= 1
            self.halt_block()

    def move_to_side(self, dx):
        old_x = self.block.x
        self.block.x += dx
        if self.handle_intersections():
            self.block.x = old_x 
    
    def rotate_block(self):
        old_rotation = self.block.rotation
        self.block.rotate()
        if self.handle_intersections():
            self.block.rotation = old_rotation

# Initialise game
pygame.init()

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)



size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Stratobus Payload Challenge")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
fps = 25
game = GamePlay(20, 10)
counter = 0

pressing_down = False

while not done:
    if game.block is None:
        game.new_blocks()
    counter += 1
    if counter > 100000:
        counter = 0

    if counter % (fps // game.level // 2) == 0 or pressing_down:
        if game.state == "start":
            game.move_down()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate_block()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                game.move_to_side(-1)
            if event.key == pygame.K_RIGHT:
                game.move_to_side(1)
            if event.key == pygame.K_SPACE:
                game.move_space()
            if event.key == pygame.K_ESCAPE:
                game.__init__(20, 10)

    if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressing_down = False

    screen.fill(white)

    for h in range(game.height):
        for w in range(game.width):
            pygame.draw.rect(screen, grey, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[h][w] > 0:
                pygame.draw.rect(screen, colours[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

    if game.block is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.block.display_blocks():
                    pygame.draw.rect(screen, colours[game.block.colour],
                                     [game.x + game.zoom * (j + game.block.x) + 1,
                                      game.y + game.zoom * (i + game.block.y) + 1,
                                      game.zoom - 2, game.zoom - 2])


    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 65, True, False)
    text = font.render("Score: " + str(game.score), True, black)
    text_game_over = font1.render("Game Over", True, (255, 0, 0))
    text_esc = font1.render("Press ESC", True, (128, 128, 128, 255))

    screen.blit(text, [0, 0])
    if game.state == "gameover":
        screen.blit(text_game_over, [20, 200])
        screen.blit(text_esc, [25, 265])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()








