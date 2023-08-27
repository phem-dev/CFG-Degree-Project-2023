from Scene_files.settings import *
from Utils.button import Button



class SceneManager:
    """
        Manages a scene/page displayed, including switching to a new scene

        Attributes:
            current_scene (object): The current active scene. Expected to have `handle_event`, `update`, and `draw` methods.
    """

    def __init__(self):
        """Initialises the SceneManager having no active scene."""
        self.current_scene = None

    def switch_scene(self, scene):
        """Updates the current scene with a new one."""
        self.current_scene = scene

    def handle_event(self, event):
        """If the current screen is active it takes in an event ready to be handled."""
        if self.current_scene:
            self.current_scene.handle_event(event)

    # the update and draw functions will be used in while loops to update/refresh what is ready to show and then show/draw it
    def update(self):
        """If the current screen is active it can be called to be updated before its drawn( below)"""
        if self.current_scene:
            self.current_scene.update()

    def draw(self, screen):
        """Calls the current scene's draw method with the given screen."""
        if self.current_scene:
            self.current_scene.draw(screen)


########################################################################################################################
# Scene superclass, is an abstract class to be used as a template, it includes the essential (but empty so far) methods for a scene
class Scene:
    def __init__(self):
        """
    Represents a scene within a game or application, including mute/unmute functionality.

        Attributes:
        mute_image (pygame.Surface):
            Loaded image of the mute speaker icon.
        unmute_image (pygame.Surface):
            Loaded image of the unmute speaker icon.
        mute_button_rect (pygame.Rect)
        The rectangle representing the mute/unmute button's position and size on the screen.
        """
        # Load the mute and unmute images
        self.mute_image = pygame.image.load('Scene_files/Images/speaker_mute_30px.png')
        self.unmute_image = pygame.image.load('Scene_files/Images/speaker_30px.png')
        # Define the mute/unmute button's rect (assuming top-right corner and 50x50 size for now)
        self.mute_button_rect = pygame.Rect(SCREEN_WIDTH - 40, 10, 30, 30)

    def toggle_mute(self):
        """
        Toggles the mute state of the music and buttons in the scene.
        Mutes or unmutes based on the current global `IS_MUTED` variable.
        """
        global MUSIC_VOLUME, IS_MUTED, BUTTON_VOLUME
        if not IS_MUTED:
            IS_MUTED = True
            # Here, you should also update the volume in actual pygame mixer
            pygame.mixer.music.set_volume(0)
            # mute all buttons
            Button.button_volume = 0
            for button in Button.active_buttons:
                button.set_volume(0)


        else:
            IS_MUTED = False
            pygame.mixer.music.set_volume(MUSIC_VOLUME)
            # unmute all buttons
            Button.button_volume = BUTTON_VOLUME
            for button in Button.active_buttons:
                button.set_volume(BUTTON_VOLUME)



    def handle_event(self, event):
        """
        Check if the user clicked on the mute/unmute button and triggers the toggle_mute function if so.

        Parameters:
        event (pygame.event.Event):
            The user input event to be processed.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.mute_button_rect.collidepoint(event.pos):
                self.toggle_mute()

    def update(self):
        """
         (Intended for future updates)
         Process any changes or logic that need to be updated before drawing to the screen.
         Currently, this method is a placeholder.
         """
        pass

    def draw(self, screen):
        """
        Render the mute/unmute button on the screen based on the current mute state.

        Parameters:
        screen (pygame.Surface):
            The surface onto which the mute/unmute button should be drawn.
        """
        # Depending on the state, draw either the mute or unmute button
        if IS_MUTED:
            screen.blit(self.mute_image, self.mute_button_rect.topleft)
        else:
            screen.blit(self.unmute_image, self.mute_button_rect.topleft)


