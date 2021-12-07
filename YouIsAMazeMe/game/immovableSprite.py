import arcade

class ImmovableSprite(arcade.Sprite):
    """
    The super class for immovable objects, passes the image 
    to arcade.Sprite and holds x and y coordinate of object.
    """
    def __init__(self, x, y, img):
        super().__init__(img)
        self.center_x = x
        self.center_y = y
    