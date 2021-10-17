import arcade
from game.start_view import Start_View
from game import constants


if __name__ == "__main__":
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    start_view = Start_View()
    window.show_view(start_view)
    arcade.run()