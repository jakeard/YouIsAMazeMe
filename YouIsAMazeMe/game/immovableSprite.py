import arcade

class ImmovableSprite(arcade.Sprite):
    def __init__(self, coordinates):
        super().__init__(self)
        self.center_x = coordinates[0]
        self.center_y = coordinates[1]
    
    