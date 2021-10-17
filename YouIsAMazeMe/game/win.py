import arcade
import time
from game import constants
import game.director

class Win(arcade.View):
    def __init__(self):
        super().__init__()
    
    def on_show(self):
        arcade.set_viewport(0, constants.SCREEN_WIDTH, 0, constants.SCREEN_HEIGHT)
        self.texture = arcade.load_texture(constants.WIN_SCREEN)
    
    def on_draw(self):
        arcade.start_render
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_text('Next Level', constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 200, arcade.color.GO_GREEN, font_size = 40, anchor_x='center')
        # arcade.draw_rectangle_outline(constants.SCREEN_WIDTH / 2 + 1, constants.SCREEN_HEIGHT / 2 - 181, 258, 50, arcade.color.WHITE)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if _x in range(143, 660) and _y in range(69, 170):
            view = game.director.MainWindow()
            view.setup()
            self.window.show_view(view)
        