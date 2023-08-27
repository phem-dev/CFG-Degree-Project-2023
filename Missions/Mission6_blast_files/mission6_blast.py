import os
import pygame
import random
import math
from pygame import mixer

# Get the root directory by going up a few times (nested)
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# now anything pointing to a directory is redefined by applying the hosts absolute path

# initialize pygame
pygame.init()
# create screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# title and icon
pygame.display.set_caption("Asteroid Blast")
icon = pygame.image.load(os.path.join(root_dir, "Missions/Mission6_blast_files/Mission6_asteroid_blast_assets/asteroid.png"))
pygame.display.set_icon(icon)

# ship
ship_img = pygame.image.load(os.path.join(root_dir, "Missions/Mission6_blast_files/Mission6_asteroid_blast_assets/zeppelin.png"))
ship_img = pygame.transform.rotate(ship_img, 270)
ship_width = 64
shipx = screen_width // 2 - ship_width // 2
shipy = 480
shipx_change = 0

# asteroid
asteroid_img = pygame.image.load(os.path.join(root_dir, "Missions/Mission6_blast_files/Mission6_asteroid_blast_assets/asteroid1.png"))
# create empty lists to add the different asteroid variables to
asteroid_images = []
asteroidx = []
asteroidy = []
asteroidy_change = []
num_asteroids = 3
speed = 0.3

stagger_amount = 200  # stagger the start of the asteroids so they don't all fall together

# loop to create three asteroids and add their attributes to the above list
for i in range(num_asteroids):
    asteroid_images.append(asteroid_img)
    asteroidx.append(random.randint(0, 736))
    asteroidy.append(0 - stagger_amount * i)  # Start above the screen and stagger start
    asteroidy_change.append(speed)  # Set the speed for each asteroid

# bullet
bullet_img = pygame.image.load(os.path.join(root_dir, "Missions/Mission6_blast_files/Mission6_asteroid_blast_assets/bullet.png"))
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 5
# ready - you can't see the bullet on the screen
# fire - you can see the bullet on the screen
bullet_state = "ready"

#  score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 25)
textX = 10
textY = 10

# game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    """ Displays the player's score in the top left corner of the screen"""
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    """ Displays the GAME OVER text in the middle of the screen"""
    over_text = over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (200, 250))


def ship(x, y):
    """Draws the ship on the screen"""
    screen.blit(ship_img, (x, y))


def asteroid(index, x, y):
    """Draws an asteroid on the screen"""
    screen.blit(asteroid_images[index], (x, y))


def fire_bullet(x, y):
    """ Draw bullet on the screen"""
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


# index of asteroid hit by the bullet
asteroid_hit_index = -1


def is_collision(bulletx, bullety):
    """check if a collision happened between a bullet and an asteroid"""
    global asteroid_hit_index
    for i in range(num_asteroids):
        distance = math.sqrt((math.pow(asteroidx[i] - bulletx, 2)) + (math.pow(asteroidy[i] - bullety, 2)))
        if distance < 27:
            asteroid_hit_index = i
            return True


def is_game_over(shipx, shipy):
    """check if the ship collided with an asteroid"""
    for i in range(num_asteroids):
        distance = math.sqrt((math.pow(asteroidx[i] - shipx, 2)) + (math.pow(asteroidy[i] - shipy, 2)))
        if distance < 40:
            return True


class Background(pygame.sprite.Sprite):
    """Class for the game background"""

    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


# create instance of background
BackGround = Background(os.path.join(root_dir, 'Missions/Mission6_blast_files/Mission6_asteroid_blast_assets/asteroid_bg.png'), [0, 0])

# game loop
running = True
while running:

    screen.fill((255, 255, 255))  # Fill the screen with a white background
    screen.blit(BackGround.image, BackGround.rect)  # draw the background

    # animate each asteroid using loop
    for i in range(num_asteroids):
        asteroidy[i] += asteroidy_change[i]  # move asteroid down the screen
        # if asteroid goes off the screen, respawn at random position on x-axis at the top of the screen
        if asteroidy[i] > screen_height:
            asteroidx[i] = random.randint(0, 736)
            asteroidy[i] = 0

    # loop to handle input
    for event in pygame.event.get():
        # exit game by closing window or pressing escape
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        # if key is pressed, check whether it is the left or the right and move the ship in that direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                shipx_change = -0.5
            if event.key == pygame.K_RIGHT:
                shipx_change = 0.5
            #     if space bar is pressed fire bullet and make bullet sound
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound(os.path.join(root_dir, 'Missions/Mission6_blast_files/Mission6_asteroid_blast_assets/laser.wav'))
                    bullet_sound.play()
                    bulletx = shipx
                    fire_bullet(bulletx, bullety)  # draw bullet at start position

        # stop  moving ship when arrow keys released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                shipx_change = 0

    # ship movement
    shipx += shipx_change
    # makesure ship doesn't go out of bounds
    if shipx <= 0:
        shipx = 0
    elif shipx > 736:
        shipx = 736

    # bullet movement
    # reset bullet start position and state when it leaves top of screen
    if bullety <= 0:
        bullety = 480
        bullet_state = "ready"

    # when bullet is fired move it up the screen
    if bullet_state == "fire":
        fire_bullet(bulletx, bullety)
        bullety -= bullety_change

        # check for a collison after a bullet is fired
        collison = is_collision(bulletx, bullety)
        # if there is a collision make an explosion sound, reset the bullet position and state, increase score by 1, reset asterpod position at top of screen
        if collison:
            explosion_sound = mixer.Sound(os.path.join(root_dir, 'Missions/Mission6_blast_files/Mission6_asteroid_blast_assets/explosion.wav'))
            explosion_sound.play()
            bullety = 480
            bullet_state = "ready"
            score_value += 1
            asteroidx[asteroid_hit_index] = random.randint(0, 736)
            asteroidy[asteroid_hit_index] = 0
            asteroid_hit_index = -1

    # Check if game is over
    game_over = is_game_over(shipx, shipy)
    # If game over: play explosion sound, display game over text, show final score in centre of screen, update display, wait 3 seconds before exiting
    if game_over:
        explosion_sound = mixer.Sound(os.path.join(root_dir, 'Missions/Mission6_blast_files/Mission6_asteroid_blast_assets/explosion.wav'))
        explosion_sound.play()
        game_over_text()
        show_score(350, 320)
        pygame.display.flip()
        pygame.time.wait(3000)
        break

    # draw the ship, asteroids and score on the screen and update the display for each loop of the game loop
    ship(shipx, shipy)
    for i in range(num_asteroids):
        asteroid(i, asteroidx[i], asteroidy[i])
    show_score(textX, textY)
    pygame.display.update()

# Quit pygame
pygame.quit()
