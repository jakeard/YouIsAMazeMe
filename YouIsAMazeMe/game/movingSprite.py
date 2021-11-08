# A subclass of arcade.sprite, and a superclass of every moving sprite.

import arcade
import game.constants as constants

class MovingSprite(arcade.Sprite):

    def __init__(self, x, y):
        super().__init__()

        # Movement constants
        self.center_x = x
        self.center_y = y
        self.is_moving = False
        self.direction = (0,0)
        self.current_pos = (self.center_x, self.center_y)
        self.target_pos = self.current_pos
        self.initial_pos = self.current_pos

    def set_move(self, direction):
        self.initial_pos = self.current_pos
        self.direction = direction
        self.is_moving = True
        self.target_pos = ((self.center_x+(direction[0]*constants.TILE_SIZE)), (self.center_y+(direction[1]*constants.TILE_SIZE)))
        print(f"Current pos: {self.current_pos}, target pos: {self.target_pos}")
    
    # def set_move_collision(self, target_x, target_y, direction: tuple = (0,0)):
    #     self.direction = direction
    #     self.is_moving = True
    #     self.target_pos = (target_x, target_y)
    
    def move(self):
        """Method that gets called during update, used to move."""
        # Am I at my target location?
        # print(f"Current pos: {self.current_pos}, target pos: {self.target_pos}")
        if self.target_pos != (self.center_x, self.center_y):
            self.change_x = self.direction[0]*constants.MOVEMENT_SPEED
            self.change_y = self.direction[1]*constants.MOVEMENT_SPEED

        else:
            #print("Reached destination")
            self.direction = (0,0)
            self.change_x = 0
            self.change_y = 0
            self.is_moving = False
            

    def update(self):
        """The player's update class. Is run every game tick."""
        super().update()
        # Make sure that the current position is up to date
        self.current_pos = (self.center_x, self.center_y)

        # Only run the move function if set_move has activated movement
        if self.is_moving:
            self.move()
        