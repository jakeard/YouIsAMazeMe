import arcade
import time
from game import constants
import game.director
import game.level_selector

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
        arcade.draw_text('Select Level', constants.SCREEN_WIDTH / 2 + 1 * constants.WIDTH_RATIO, constants.SCREEN_HEIGHT / 2 - 260 * constants.HEIGHT_RATIO, arcade.color.GO_GREEN, font_size = 40, anchor_x='center')
        arcade.draw_text('Main Menu', int(60 * constants.WIDTH_RATIO), int(25 * constants.HEIGHT_RATIO), arcade.color.RUBY_RED, font_size=25, anchor_x='center')

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if _x in range(int(272 * constants.WIDTH_RATIO), int(531 * constants.WIDTH_RATIO)) and _y in range(int(94 * constants.HEIGHT_RATIO), int(145 * constants.HEIGHT_RATIO)):
            view = game.director.MainWindow(self.level + 1)
            view.setup()
            self.window.show_view(view)
        elif _x in range(int(272 * constants.WIDTH_RATIO), int(531 * constants.WIDTH_RATIO)) and _y in range(int(30 * constants.HEIGHT_RATIO), int(80 * constants.HEIGHT_RATIO)):
            view = game.level_selector.LevelSelector()
            view.on_draw()
            self.window.show_view(view)
        elif _x in range(int(2 * constants.WIDTH_RATIO), int(118 * constants.WIDTH_RATIO)) and _y in range(int(20 * constants.HEIGHT_RATIO), int(55 * constants.HEIGHT_RATIO)):
            view = game.start_view.Start_View()
            view.on_show()
            self.window.show_view(view)
        