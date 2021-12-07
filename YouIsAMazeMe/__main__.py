import arcade
from game.start_view import Start_View
from game import constants


if __name__ == "__main__":
    """
    The file that starts the whole program. All attempts 
    to start the game begin here.
    """
    constants.pixel_sound.play(volume=.28, pan=1, loop = True)
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    start_view = Start_View()
    window.show_view(start_view)
    arcade.run()