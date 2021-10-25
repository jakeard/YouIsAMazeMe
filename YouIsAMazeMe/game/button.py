import arcade
from game.immovableSprite import ImmovableSprite
from game import constants

class Buttons(ImmovableSprite):
    def __init__(self, x, y):
        super().__init__(x, y, constants.BUTTON_SPRITE)
    
    def is_pressed(self, pressed):
        if pressed == True:
           self.append_texture(constants.BUTTON_PRESSED_SPRITE)
           self.set_texture(1)
           self.width = 64
           self.height = 64
        else:
            self.set_texture(0)
        