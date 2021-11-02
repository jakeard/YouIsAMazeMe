import arcade
from game import constants
# import game.director

class Commands():
    def __init__(self, sprites):
        self.file = 'YouIsAMazeMe/game/run.py'
        self.sprites = sprites
        self.door = sprites['door'][0]
        # self.door = sprites['door'][0]
        # self.positions = []
        # self.boxes = sprites['boxes']
        # self.box_order()

    def execute(self, sprites):
        # self.positions = []
        print("Executing commands!")
        self.sprites = sprites
        self.boxes = sprites['boxes']
        self.box_order()
        
           
    def box_order(self):
        # for box in self.boxes:
        #     self.positions.append((box.center_x, box.center_y, box.get_type()))
        boxes = self.boxes
        search = None
        # response = None
        cmds = []
        for box in boxes:
            if box == boxes[0]:
                original_x = box.center_x
                original_y = box.center_y
                search = original_x + constants.TILE_SIZE
            if box.center_x == search and box.center_y == original_y:
                cmds.append(box.get_type())
                print(box.get_type())
                search = box.center_x + constants.TILE_SIZE
        if cmds == ['print(', 'door', ")"]:
            print("A door.")
            door = self.door
            door.center_x = 704
            door.center_y = constants.TILE_SIZE * 1
        if cmds == ['del(', 'door', ")"]:
            print("Delete a door.")
            door = self.door
            door.center_x = constants.TILE_SIZE + constants.SCREEN_WIDTH
            door.center_y = constants.TILE_SIZE + constants.SCREEN_HEIGHT
            # game.director.MainWindow.change_win_status(True)




        # with open(self.file, 'w') as f:
        #     # print(cmds)
        #     for i in cmds:
        #         f.write(i)
        # with open(self.file, 'r') as f:
        #     try:
        #         exec(f.read())
        #     except:
        #         print("Error")
        #         # response = 'Error'
        # # arcade.draw_text(response, constants.SCREEN_WIDTH / 2 + 25, constants.SCREEN_HEIGHT / 2 + 45, arcade.color.RUST, font_size=35, anchor_x='center')
        # # with open(self.file, 'r') as f:
        # #     try:
                
            