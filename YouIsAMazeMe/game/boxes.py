from os import X_OK
import arcade
from game.movingSprite import MovingSprite
from game import constants

class Box(MovingSprite):
    def __init__(self, x, y):
        super().__init__()

        self.texture = arcade.load_texture(constants.PRINT)
        self.scale = .65
        self.set_size()
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