import arcade
from game.director import MainWindow
from game.level_selector import LevelSelector
from game import constants
from game.instructions import Instructions

class Start_View(arcade.View):
    def __init__(self):
        super().__init__()
    
    def on_show(self):
        self.texture = arcade.load_texture(constants.START_SCREEN)

    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_text("You Is AMaze Me", constants.SCREEN_WIDTH / 2 + 1 * constants.WIDTH_RATIO, constants.SCREEN_HEIGHT / 2 + 125 * constants.HEIGHT_RATIO, arcade.color.WHITE, font_size=35, anchor_x='center')
        arcade.draw_text('Play', constants.SCREEN_WIDTH / 2  + 1 * constants.WIDTH_RATIO, constants.SCREEN_HEIGHT / 2 - 20 * constants.HEIGHT_RATIO, arcade.color.WHITE, font_size=35, anchor_x='center')
        arcade.draw_text('Select Level', constants.SCREEN_WIDTH / 2 + 3 * constants.WIDTH_RATIO, constants.SCREEN_HEIGHT / 2 - 80 * constants.HEIGHT_RATIO, arcade.color.WHITE, font_size = 35, anchor_x='center')
        arcade.draw_text('Instructions', constants.SCREEN_WIDTH / 2 + 3 * constants.WIDTH_RATIO, constants.SCREEN_HEIGHT / 2 - 140 * constants.HEIGHT_RATIO, arcade.color.WHITE, font_size = 35, anchor_x='center')

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if _x in range(int(365 * constants.WIDTH_RATIO), int(440 * constants.WIDTH_RATIO)) and _y in range(int(270 * constants.HEIGHT_RATIO), int(315 * constants.HEIGHT_RATIO)):
            view = MainWindow()
            view.setup()
            self.window.show_view(view)
        elif _x in range(int(310 * constants.WIDTH_RATIO), int(495 * constants.WIDTH_RATIO)) and _y in range(int(212 * constants.HEIGHT_RATIO), int(250 * constants.HEIGHT_RATIO)):
            view = LevelSelector()
            view.on_draw()
            self.window.show_view(view)
        elif _x in range(int(305 * constants.WIDTH_RATIO), int(495 * constants.WIDTH_RATIO)) and _y in range(int(150 * constants.HEIGHT_RATIO), int(190 * constants.HEIGHT_RATIO)):
            view = Instructions()
            view.on_draw()
            self.window.show_view(view)
        



