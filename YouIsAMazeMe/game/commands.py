import arcade
from game import constants
import game.enemy.enemies as enemies

class Commands():
    """
    The Commands class is called when the player presses the button, 
    and checks for the order of the boxes after the starting block in 
    order to know what to do.
    """
    def __init__(self, sprites):
        self.file = 'YouIsAMazeMe/game/run.py'
        self.sprites = sprites
        self.door = sprites['door'][0]
        self.enemies = sprites['enemies']
        self.slimes = sprites['slimes']
        self.button = sprites["button"]

    def execute(self, sprites):
        print("Executing commands!")
        self.sprites = sprites
        self.boxes = sprites['boxes']
        self.box_order()
        
           
    def box_order(self):
        boxes = self.boxes
        search = None
        cmds = []
        searching = True
        for box in boxes:
            if box.get_type() == "start":
                original_x = box.center_x
                original_y = box.center_y
                search = original_x + constants.TILE_SIZE
                count = 0
                while searching:
                    count += 1
                    for box in boxes: 
                        end = "Nope!"                      
                        if box.center_x == search and box.center_y == original_y:
                            cmds.append(box.get_type())
                            end = box.get_type()
                            print(box.get_type())
                            search = box.center_x + constants.TILE_SIZE
                        if end == ")" or count == len(boxes):
                            searching = False
                if cmds == ['print(', 'door', ")"]:
                    print("A door.")
                    door = self.door
                    door.center_x = 704
                    door.center_y = 704
                if cmds == ['print(', 'slimes', ")"]:
                    print("Print a slimes.")
                    button = self.button[0]
                    x = button.center_x
                    y = button.center_y
                    self.sprites['slimes'][0].center_x = x
                    self.sprites['slimes'][0].center_y = y
                if cmds == ['del(', 'slimes', ")"]:
                    print("Delete the slimes.")
                    slimes = self.slimes
                    for slime in slimes:
                        slime.center_x = constants.TILE_SIZE * 2 + constants.SCREEN_WIDTH
                        slime.center_y = constants.TILE_SIZE * 2 + constants.SCREEN_HEIGHT
                if cmds == ['del(', 'door', ")"]:
                    print("Delete a door.")
                    door = self.door
                    door.center_x = constants.TILE_SIZE + constants.SCREEN_WIDTH
                    door.center_y = constants.TILE_SIZE + constants.SCREEN_HEIGHT
                if cmds == ['del(', 'bugs', ")"]:
                    print("Delete all bugs.")
                    for enemy in self.enemies:
                        enemy.center_x = constants.TILE_SIZE + constants.SCREEN_WIDTH
                        enemy.center_y = constants.TILE_SIZE + constants.SCREEN_HEIGHT
                if cmds == ['print(', 'bugs', ")"]:
                    print("Print a bugs.")
                    button = self.button[0]
                    x = button.center_x
                    y = button.center_y
                    self.sprites['enemies'][0].center_x = x
                    self.sprites['enemies'][0].center_y = y