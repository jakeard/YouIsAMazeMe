import arcade
from game.director import MainWindow
from game import constants


if __name__ == "__main__":
    window = MainWindow(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    window.setup()
    arcade.run()