import arcade
from game.director import MainWindow
from game.level_selector import LevelSelector
from game import constants

class Start_View(arcade.View):
    def __init__(self):
        super().__init__()
    
    def on_show(self):
        constants.autumn_sound.play(volume=.75, pan=1)
        self.texture = arcade.load_texture(constants.START_SCREEN)

    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_text("You Is AMaze Me", constants.SCREEN_WIDTH / 2 + 25 * constants.WIDTH_RATIO, constants.SCREEN_HEIGHT / 2 + 45 * constants.HEIGHT_RATIO, arcade.color.WHITE, font_size=35, anchor_x='center')
        arcade.draw_text('Play', constants.SCREEN_WIDTH / 2  + 1 * constants.WIDTH_RATIO, constants.SCREEN_HEIGHT / 2 - 100 * constants.HEIGHT_RATIO, arcade.color.WHITE, font_size=35, anchor_x='center')
        arcade.draw_text('Select Level', constants.SCREEN_WIDTH / 2 + 3 * constants.WIDTH_RATIO, constants.SCREEN_HEIGHT / 2 - 160 * constants.HEIGHT_RATIO, arcade.color.WHITE, font_size = 35, anchor_x='center')

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if _x in range(int(354 * constants.WIDTH_RATIO), int(451 * constants.WIDTH_RATIO)) and _y in range(int(190 * constants.HEIGHT_RATIO), int(241 * constants.HEIGHT_RATIO)):
            view = MainWindow()
            view.setup()
            self.window.show_view(view)
        elif _x in range(int(276 * constants.WIDTH_RATIO), int(532 * constants.WIDTH_RATIO)) and _y in range(int(137 * constants.HEIGHT_RATIO), int(177 * constants.HEIGHT_RATIO)):
            view = LevelSelector()
            view.on_draw()
            self.window.show_view(view)
        



