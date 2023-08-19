import pygame
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


BackGround_home = Background('Scene_files/Images/home_bg.png', [0, 0])
BackGround_asteroid = Background('Scene_files/Images/asteroid_bg.png', [0, 0])
BackGround_sentinel = Background('Scene_files/Images/sentinel_bg.png', [0, 0])
BackGround_mars = Background('Scene_files/Images/mars_bg.png', [0, 0])
BackGround_payload = Background('Scene_files/Images/payload_bg.png', [0, 0])
