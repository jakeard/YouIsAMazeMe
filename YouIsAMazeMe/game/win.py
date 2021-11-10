import arcade
import time
from game import constants
import game.director

class Win(arcade.View):
    def __init__(self, level):
        super().__init__()
        self.level = level
    
    def on_show(self):
        arcade.set_viewport(0, constants.SCREEN_WIDTH, 0, constants.SCREEN_HEIGHT)
        self.texture = arcade.load_texture(constants.WIN_SCREEN)
    
    def on_draw(self):
        arcade.start_render
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_text('Next Level', constants.SCREEN_WIDTH / 2 + 1 * constants.WIDTH_RATIO, constants.SCREEN_HEIGHT / 2 - 200 * constants.HEIGHT_RATIO, arcade.color.GO_GREEN, font_size = 40, anchor_x='center')
        
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if _x in range(int(272 * constants.WIDTH_RATIO), int(531 * constants.WIDTH_RATIO)) and _y in range(int(94 * constants.HEIGHT_RATIO), int(145 * constants.HEIGHT_RATIO)):
            view = game.director.MainWindow(self.level + 1)
            view.setup()
            self.window.show_view(view)
        