import arcade
from game.immovableSprite import ImmovableSprite
from game import constants

class Buttons(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.textures = [arcade.load_texture(constants.BUTTON_SPRITE), 
                         arcade.load_texture(constants.BUTTON_PRESSED_SPRITE)]
        self.center_x = x
        self.center_y = y
        self.is_pressed(False)
        
    def is_pressed(self, pressed):
        if pressed:
            self.texture = self.textures[1]
        else:
            self.texture = self.textures[0]
        