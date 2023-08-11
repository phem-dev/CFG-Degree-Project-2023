
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
    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass

