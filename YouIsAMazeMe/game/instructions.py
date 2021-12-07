import arcade
from game import constants
import game.start_view

class Instructions(arcade.View):
    """
    An arcade.View class, shows the screen that has the game instructions when loaded.
    """
    def __init__(self):
        super().__init__()
        self.texture= arcade.load_texture(constants.INSTRUCT)

    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_lrtb_rectangle_filled(int(7 * constants.WIDTH_RATIO), int(75 * constants.WIDTH_RATIO), int(45 * constants.HEIGHT_RATIO), int(15 * constants.HEIGHT_RATIO), (179, 116, 93))
        arcade.draw_text("How to Play", int(constants.SCREEN_WIDTH / 2 + 1 * constants.WIDTH_RATIO), int(550 * constants.HEIGHT_RATIO), arcade.color.WHITE, font_size=35, anchor_x='center')
        arcade.draw_text('Your job is to escape each level. Use WASD to move. You are the     character, and must push blocks like     to form code that will allow you to escape the room. Put the code after the      block. Look out for bugs in your code! The     bug can get in your way and slow you down, the       bug can mess up your code, and the        bug will kill you and your program. The slime blocks look like this     and block your path. You must remove them using your code in order to get through. If you get stuck, or the bugs mess you up, press "R" to restart the level, or press "Q" to return to the start menu. Good luck!', 600, int(450 * constants.HEIGHT_RATIO), arcade.color.WHITE, font_size=30, anchor_x='center', multiline=True, width=1000)
        arcade.draw_text('Back', int(40 * constants.WIDTH_RATIO), int(20 * constants.HEIGHT_RATIO), arcade.color.WHITE, font_size=25, anchor_x='center')

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if _x in range(int(7 * constants.WIDTH_RATIO), int(75 * constants.WIDTH_RATIO)) and _y in range(int(15 * constants.HEIGHT_RATIO), int(45 * constants.HEIGHT_RATIO)):
            view = game.start_view.Start_View()
            view.on_show()
            self.window.show_view(view)