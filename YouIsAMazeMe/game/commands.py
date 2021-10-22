import arcade
from game import constants

class Commands():
    def __init__(self):
        pass

    def execute(self, sprites):
        self.positions = []
        self.boxes = sprites['boxes']
        self.box_order()
    
    def box_order(self):
        for box in self.boxes:
            self.positions.append((box.center_x, box.center_y, box.get_type()))
        for i in range(0, constants.SCREEN_WIDTH, 64):
            pass