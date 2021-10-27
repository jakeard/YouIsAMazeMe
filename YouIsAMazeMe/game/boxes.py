from os import X_OK
import arcade
from game.movingSprite import MovingSprite
from game import constants

class Box(MovingSprite):
    def __init__(self, x, y, type):
        super().__init__()


        main_path = constants.CODE_BLOCKS
        self.texture = arcade.load_texture(f"{main_path}\{type}.png")
        self.scale = 1
        self.set_size()

        self.type = type
        self.center_x = x
        self.center_y = y


        self.fixing = False

    def update(self):
        super().update()

        if self.fixing:
            if not self.is_moving:
                self.fixing = False

    def set_size(self, size=(constants.TILE_SIZE-16)):
        self.height = size
        self.width = size
        # This part doesn't seem to be changing the size of the hitbox...
        point = size
        self.points = [[-point, -point], [point, -point], [point, point], [-point, point]]
    
    def get_type(self):
        return self.type