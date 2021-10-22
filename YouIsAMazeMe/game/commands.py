import arcade

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
        # for i in self.boxes:
        #     for j in self.boxes:
        for i in self.positions:
            for j in self.positions:

                # if i[1] == j[1] and i[1] += 




        # print(self.positions)

