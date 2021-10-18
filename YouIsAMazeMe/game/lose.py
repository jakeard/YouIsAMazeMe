import arcade
from game import constants
import game.director

class Lose(arcade.View):
    def __init__(self):
        super().__init__()
    
    def on_show(self):
        arcade.set_viewport(0, constants.SCREEN_WIDTH, 0, constants.SCREEN_HEIGHT)
        self.texture = arcade.load_texture(constants.LOSE_SCREEN)
    
    def on_draw(self):
        arcade.start_render
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_text('Retry', constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 200, arcade.color.CAMEL, font_size = 40, anchor_x='center')
        arcade.draw_text('Quit', constants.SCREEN_WIDTH / 2 - 10, constants.SCREEN_HEIGHT / 2 - 270, arcade.color.CAMEL, font_size = 40, anchor_x='center')
        # arcade.draw_rectangle_outline(constants.SCREEN_WIDTH / 2 - 8, constants.SCREEN_HEIGHT / 2 - 251, 107, 49, arcade.color.WHITE)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if _x in range(266, 537) and _y in range(58, 173):
            view = game.director.MainWindow()
            view.setup()
            self.window.show_view(view)
        elif _x in range(285, 500) and _y in range(49, 148):
            arcade.exit()