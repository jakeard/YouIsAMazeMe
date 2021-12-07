import arcade
from game import constants
import game.director

class Lose(arcade.View):
    """
    An arcade.View class, shows the lose screen when loaded.
    """
    def __init__(self):
        super().__init__()
    
    def on_show(self):
        arcade.set_viewport(0, constants.SCREEN_WIDTH, 0, constants.SCREEN_HEIGHT)
        self.texture = arcade.load_texture(constants.LOSE_SCREEN)
    
    def on_draw(self):
        arcade.start_render
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_text('Retry', constants.SCREEN_WIDTH / 2 + 1 * constants.WIDTH_RATIO, constants.SCREEN_HEIGHT / 2 - 200 * constants.HEIGHT_RATIO, arcade.color.CAMEL, font_size = 40, anchor_x='center')
        arcade.draw_text('Quit', constants.SCREEN_WIDTH / 2 - 10 * constants.WIDTH_RATIO, constants.SCREEN_HEIGHT / 2 - 270 * constants.HEIGHT_RATIO, arcade.color.CAMEL, font_size = 40, anchor_x='center')

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if _x in range(int(320 * constants.WIDTH_RATIO), int(483 * constants.WIDTH_RATIO)) and _y in range(int(83 * constants.HEIGHT_RATIO), int(148 * constants.HEIGHT_RATIO)):
            print('r')
            view = game.director.MainWindow()
            view.setup()
            self.window.show_view(view)
        elif _x in range(int(338 * constants.WIDTH_RATIO), int(446 * constants.WIDTH_RATIO)) and _y in range(int(24 * constants.HEIGHT_RATIO), int(74 * constants.HEIGHT_RATIO)):
            arcade.exit()