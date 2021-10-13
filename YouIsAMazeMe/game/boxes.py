from os import X_OK
import arcade
from game.movingSprite import MovingSprite
from game import constants

class Box(MovingSprite):
    def __init__(self, x, y):
        super().__init__()

        self.texture = arcade.load_texture(constants.WALL_SPRITE)
        self.scale = 2.2
        self.center_x = x
        self.center_y = y

        self.fixing = False

    def update(self):
        super().update()

        if self.fixing:
            if not self.is_moving:
                self.fixing = False