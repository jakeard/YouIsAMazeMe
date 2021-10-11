import arcade
from game.immovableSprite import ImmovableSprite
from game import constants

class Walls(ImmovableSprite):
    def __init__(self, x, y):
        super().__init__(x, y, constants.WALL_SPRITE)

        