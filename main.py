import pygame
from pygame import mixer
import sys  # needed so the system can exit the window when the 'x' is pressed
from Scene_files.SceneManager import SceneManager, Scene
from Scene_files.Scenes import SceneStart
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, MUSIC_PATH, MUSIC_VOLUME


########################################################################################################################


pygame.init()
mixer.init()


# Create screen and clock, clock will be needed to help make animations and waits https://www.pygame.org/docs/ref/time.html
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # set the screen size
# screen = screen.convert_alpha()  # Convert the screen to support transparency on pixels
pygame.display.set_caption('Stratobus Mission')  # set the window title
clock = pygame.time.Clock()  # make a clock object, so we can use its method 'clock.tick(30) later, this will slow the frame rate (or refresh rate) to 30 frames per second during while loops instead of doing the while loop nearly instantaneously


########################################################################################################################


def main():
    scene_manager = SceneManager()  # object instantiation for the SceneManager
    scene_manager.switch_scene(SceneStart(scene_manager, clock))  # start scene 1

    # start running the game but always listen for the event of the user clicking exit or any other events to handle
    while True:
        if mixer.music.get_busy():
            pass  # As the code might loop back to here, didn't want to load it again if already playing (ie busy == True)
        else:
            mixer.music.load(MUSIC_PATH)
            mixer.music.set_volume(MUSIC_VOLUME) # Set volume to 30%
            mixer.music.play(-1, 0, 200) # loop infinitely

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # exit event
                pygame.quit()
                sys.exit()
            scene_manager.handle_event(event)  # any other events are passed to whatever scene is active for processing by that specific scene (a button click on a part of a screen could overlap with button clicks on any scene otherwise)

        # continuously (because we are in a while true loop) update the scene, draw the scene, and re-render the display at 30fps
        scene_manager.update()
        scene_manager.draw(screen)
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
