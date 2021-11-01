import arcade
from game.director import MainWindow
from game import constants

class Start_View(arcade.View):
    def __init__(self):
        super().__init__()
    
    def on_show(self):
        self.texture = arcade.load_texture(constants.START_SCREEN)

    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_text("You Is AMaze Me", constants.SCREEN_WIDTH / 2 + 25 * constants.WIDTH_RATIO, constants.SCREEN_HEIGHT / 2 + 45 * constants.HEIGHT_RATIO, arcade.color.RUST, font_size=35, anchor_x='center')
        arcade.draw_text('Play', constants.SCREEN_WIDTH / 2  + 1 * constants.WIDTH_RATIO, constants.SCREEN_HEIGHT / 2 - 100 * constants.HEIGHT_RATIO, arcade.color.RUST, font_size = 35, anchor_x='center')
        # arcade.draw_rectangle_outline(constants.SCREEN_WIDTH / 2 + 2, constants.SCREEN_HEIGHT / 2 - 85, 95, 50, arcade.color.BLACK)
        # arcade.draw_lrtb_rectangle_outline(int(354 * constants.WIDTH_RATIO), int(451 * constants.WIDTH_RATIO), int(241 * constants.HEIGHT_RATIO), int(190 * constants.HEIGHT_RATIO), arcade.color.BLACK)
        
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if _x in range(int(354 * constants.WIDTH_RATIO), int(451 * constants.WIDTH_RATIO)) and _y in range(int(190 * constants.HEIGHT_RATIO), int(241 * constants.HEIGHT_RATIO)):
            view = MainWindow()
            view.setup()
            self.window.show_view(view)
        



