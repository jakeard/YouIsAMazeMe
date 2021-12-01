import arcade
import os
import game.start_view
import game.director
from game import constants

class LevelSelector(arcade.View):
    def __init__(self):
        super().__init__()
        self.press_ranges = []
        self.num_files = len([f for f in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../', 'levels')) if f not in {'todo.txt', 'level_00.csv', 'curr_data.json'}])

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color((131, 177, 91))
        arcade.draw_text('Levels', int(constants.SCREEN_WIDTH / 2 + 1 * constants.WIDTH_RATIO), int(550 * constants.HEIGHT_RATIO), arcade.color.WHITE, font_size=35, anchor_x='center')
        arcade.draw_text('Back', int(60 * constants.WIDTH_RATIO), int(25 * constants.HEIGHT_RATIO), arcade.color.WHITE, font_size=25, anchor_x='center')
        level = 0
        y = 400 * constants.HEIGHT_RATIO
        while level != self.num_files:
            for i in range(int(200 * constants.WIDTH_RATIO), int(600 * constants.WIDTH_RATIO) + 1, int(200 * constants.WIDTH_RATIO)):
                level += 1
                if level % 4 == 0:
                    y -= 150 * constants.HEIGHT_RATIO
                if level < 10:
                    arcade.draw_text(f'0{level}', i, int(y), arcade.color.WHITE, font_size=35, anchor_x='center')
                else:
                    arcade.draw_text(f'{level}', i, int(y), arcade.color.WHITE, font_size=35, anchor_x='center')
                self.press_ranges.append((int(i - 25 * constants.WIDTH_RATIO), int(i + 25 * constants.WIDTH_RATIO), int(y + 35 * constants.HEIGHT_RATIO), int(y - 1 * constants.HEIGHT_RATIO), level + 1))
                if level == self.num_files:
                    break
        # arcade.draw_lrtb_rectangle_outline(int(20 * constants.WIDTH_RATIO), int(100 * constants.WIDTH_RATIO), int(55 * constants.HEIGHT_RATIO), int(20 * constants.HEIGHT_RATIO), arcade.color.BLACK)
    
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if _x in range(int(20 * constants.WIDTH_RATIO), int(100 * constants.WIDTH_RATIO)) and _y in range(int(20 * constants.HEIGHT_RATIO), int(55 * constants.HEIGHT_RATIO)):
            view = game.start_view.Start_View()
            view.on_show()
            self.window.show_view(view)
        else:
            for i in self.press_ranges:
                if _x in range(i[0], i[1]) and _y in range(i[3], i[2]):
                    view = game.director.MainWindow(i[4] - 1)
                    view.setup()
                    self.window.show_view(view)
                    break