import arcade

class ImmovableSprite(arcade.Sprite):
    def __init__(self, x, y, img):
        super().__init__(img)
        self.center_x = x
        self.center_y = y
    