import arcade
from game import constants

class Commands():
    def __init__(self, sprites):
        self.positions = []
        self.boxes = sprites['boxes']
        self.box_order()
        

    # def execute(self, sprites):
    #     self.positions = []
    #     self.boxes = sprites['boxes']
    #     self.box_order()
    
    def box_order(self):
        for box in self.boxes:
            self.positions.append((box.center_x, box.center_y, box.get_type()))
            if box.get_type() == "print":
                search = box.center_x + constants.TILE_SIZE
                for box in self.boxes:
                    if box.center_x == search:
                        print(box.get_type())
            if box.get_type() == "delete":
                pass
            if box.get_type() == "spawn":
                pass
            
        # for box in self.boxes:
        #     if box.get_type() == "print":
        #         
        #     if box.get_type() == "delete":
        #         pass
        #     if box.get_type() == "spawn":
