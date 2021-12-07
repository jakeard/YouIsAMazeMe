import arcade
from game.movingSprite import MovingSprite
from game import constants

class Box(MovingSprite):
    """
    The class that sets, keeps track of, and updates the moving boxes with 
    the commands on them. Is a subclass of the MovingSprite class. 
    """
    def __init__(self, x, y, box_type=None):
        super().__init__(x, y)


        main_path = constants.CODE_BLOCKS
        if box_type is not None:
            self.texture = arcade.load_texture(f"{main_path}/{box_type}.png")
        else:
            self.texture = arcade.load_texture(f"{main_path}/base.png")
        self.scale = 1
        self.set_size()
        self.type = box_type
        self.center_x = x
        self.center_y = y

    def update(self):
        super().update()

    def set_size(self, size=(constants.TILE_SIZE-16)):
        self.height = size
        self.width = size
        # This part doesn't seem to be changing the size of the hitbox...
        point = size
        self.points = [[-point, -point], [point, -point], [point, point], [-point, point]]
    
    def get_type(self):
        return self.type

    def set_move(self, direction):
        super().set_move(direction)