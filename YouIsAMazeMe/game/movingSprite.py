# A subclass of arcade.sprite, and a superclass of every moving sprite.

import arcade
import game.constants as constants

class MovingSprite(arcade.Sprite):
    """
    A super class that keeps track of all moving sprites 
    locations, directions, face, movement, state, etc.
    """
    def __init__(self, x, y):
        super().__init__()

        # Movement constants
        self.fixing = False
        self.is_disabled = False
        self.center_x = x
        self.center_y = y
        self.is_moving = False
        self.direction = (0,0)
        self.current_pos = (self.center_x, self.center_y)
        self.target_pos = self.current_pos
        self.initial_pos = self.current_pos
        self.disabled_pos = None

    def set_move(self, direction):

        if not self.is_disabled:
            self.initial_pos = self.current_pos
            self.direction = direction
            self.is_moving = True
            self.target_pos = ((self.center_x+(direction[0]*constants.TILE_SIZE)), (self.center_y+(direction[1]*constants.TILE_SIZE)))
    
    def move(self):
        """Method that gets called during update, used to move."""
        # Am I at my target location?
        if self.target_pos != (self.center_x, self.center_y):
            self.change_x = self.direction[0]*constants.MOVEMENT_SPEED
            self.change_y = self.direction[1]*constants.MOVEMENT_SPEED

        else:
            self.direction = (0,0)
            self.change_x = 0
            self.change_y = 0
            self.is_moving = False
            if self.fixing:
                self.fixing = False
            

    def update(self):
        """The player's update class. Is run every game tick."""

        if not self.is_disabled:
            super().update()

            # Make sure that the current position is up to date
            self.current_pos = (self.center_x, self.center_y)

            # Only run the move function if set_move has activated movement
            if self.is_moving:
                self.move()
            else: # enter this block if I'm not moving!
                if not self.is_moving and self.fixing:
                    self.fixing = False
                    #self._round_pos() # disabled, slows down program speed and still doesn't fix every error.

        
    def bounce(self, direction=None):
        """Causes the sprite to reverse direction. Reverses current direction by default."""
        self.fixing = True
        if direction is None:
            direction = self.direction
        
        self.direction = (direction[0]*-1, direction[1]*-1)
        self.target_pos = self.initial_pos
        
    def hide(self):
        """Teleport them off screen, and disable their movement."""
        if not self.is_disabled:
            self.center_x,self.center_y = self.target_pos
            self.disabled_pos = self.target_pos
            self.change_x = 0
            self.change_y = 0
            self.is_disabled = True
            self.is_moving = False
            self.direction = (0,0)
            self.center_x,self.center_y = (-64,-64)
    
    def unhide(self):
        self.center_x = 275
        self.center_y = 389
        if self.is_disabled:
            self.is_disabled = False
            self.center_x,self.center_y = self.disabled_pos
            self.disabled_pos = None

    def _round_pos(self):
        """Helper function, sets the sprite's location to the closest tile center."""
        if not self.center_x%64==0:
            x_offset = round(self.center_x/64)
            self.center_x = x_offset*64
        if not self.center_y%64==0:
            y_offset = round(self.center_y/64)
            self.center_y = y_offset*64

    def collides_with_sprite(self, other) -> bool:
        if not self.is_disabled:
            return super().collides_with_sprite(other)
        else:
            return False
