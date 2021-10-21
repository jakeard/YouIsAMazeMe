import arcade
from game.immovableSprite import ImmovableSprite
from game import constants

class Walls(ImmovableSprite):
    def __init__(self, x, y):
        super().__init__(x, y, constants.WALL_SPRITE)
        self.set_size()

    def set_size(self, size=(constants.TILE_SIZE)):
        self.height = size
        self.width = size
        # This part doesn't seem to be changing the size of the hitbox...
        point = size
        self.points = [[-point, -point], [point, -point], [point, point], [-point, point]]