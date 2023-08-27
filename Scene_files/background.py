import pygame
import os

# Get the directory where the current settings.py script resides
root_dir = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# now anything pointing to a directory is redefined by applying the hosts absolute path

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


BackGround_home = Background(os.path.join(root_dir, 'Scene_files/Images/home_bg.png'), [0, 0])
BackGround_asteroid = Background(os.path.join(root_dir, 'Scene_files/Images/asteroid_bg.png'), [0, 0])
BackGround_satellite = Background(os.path.join(root_dir, 'Scene_files/Images/sentinel_bg.png'), [0, 0])
BackGround_mars = Background(os.path.join(root_dir, 'Scene_files/Images/mars_bg.png'), [0, 0])
BackGround_payload = Background(os.path.join(root_dir, 'Scene_files/Images/payload_bg.png'), [0, 0])
BackGround_payload_new = Background(os.path.join(root_dir, 'Scene_files/Images/payload_bg1.png'), [0, 0])
BackGround_iss = Background(os.path.join(root_dir, 'Scene_files/Images/iss_bg.png'), [0, 0])
BackGround_final = Background(os.path.join(root_dir, 'Scene_files/Images/final_bg.png'), [0, 0])
BackGround_end = Background(os.path.join(root_dir, 'Scene_files/Images/end_bg.png'), [0, 0])
