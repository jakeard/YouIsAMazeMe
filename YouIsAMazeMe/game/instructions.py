import arcade
from game import constants
import game.start_view

class Instructions(arcade.View):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color((131, 177, 91))
        arcade.draw_text("How to Play", int(constants.SCREEN_WIDTH / 2 + 1 * constants.WIDTH_RATIO), int(550 * constants.HEIGHT_RATIO), arcade.color.WHITE, font_size=35, anchor_x='center')
        arcade.draw_text('Your job is to escape each level. Use WASD to move. You are the (YOU HERE) character, and must push blocks like (EXAMPLE BLOCK HERE) to form code that will allow you to escape the room. Put the code after the (RUN BLOCK HERE) block. Look out for bugs in your code! The (EASY BUG) bug can get in your way and slow you down, the (MEDIUM BUG) bug can mess up your code, and the (HARD BUG) bug will kill your program. Good luck!', 600, int(450 * constants.HEIGHT_RATIO), arcade.color.WHITE, font_size=30, anchor_x='center', multiline=True, width=1000)
        arcade.draw_text('Back', int(60 * constants.WIDTH_RATIO), int(25 * constants.HEIGHT_RATIO), arcade.color.WHITE, font_size=25, anchor_x='center')
        # arcade.draw_text('Select Level', constants.SCREEN_WIDTH / 2 + 3 * constants.WIDTH_RATIO, constants.SCREEN_HEIGHT / 2 - 160 * constants.HEIGHT_RATIO, arcade.color.WHITE, font_size = 35, anchor_x='center')

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if _x in range(int(20 * constants.WIDTH_RATIO), int(100 * constants.WIDTH_RATIO)) and _y in range(int(20 * constants.HEIGHT_RATIO), int(55 * constants.HEIGHT_RATIO)):
            view = game.start_view.Start_View()
            view.on_show()
            self.window.show_view(view)
        # if _x in range(int(354 * constants.WIDTH_RATIO), int(451 * constants.WIDTH_RATIO)) and _y in range(int(190 * constants.HEIGHT_RATIO), int(241 * constants.HEIGHT_RATIO)):
        #     view = MainWindow()
        #     view.setup()
        #     self.window.show_view(view)
        # elif _x in range(int(276 * constants.WIDTH_RATIO), int(532 * constants.WIDTH_RATIO)) and _y in range(int(137 * constants.HEIGHT_RATIO), int(177 * constants.HEIGHT_RATIO)):
        #     view = LevelSelector()
        #     view.on_draw()
        #     self.window.show_view(view)