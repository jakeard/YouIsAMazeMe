import arcade
import game.constants as constants
from game.movingSprite import MovingSprite 
import random

def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True)
    ]

class EnemyBasic(MovingSprite):

    def __init__(self, x, y):
        super().__init__(x, y)
        # How does this interract with the character?
        self.can_damage = False
        self.can_push = False
        self.can_block = False
        
        self.fixing = False

        self.idle_counter = 0
        self.update_frames = 300 # runs approx. 60 frames per second, so this is about 5 seconds.

        self.center_x = x
        self.center_y = y
        self.past_x = None
        self.past_y = None
        self.past_direction = None
        self.direction = (0, 0)
        self.character_face_direction = constants.RIGHT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0

        self.scale = constants.CHARACTER_SCALING

        # Adjust the collision box. Default includes too much empty space
        # side-to-side. Box is centered at sprite center, (0, 0)
        self.points = [[-22, -64], [22, -64], [22, 28], [-22, 28]]

        # --- Load Textures ---

        # Images from Kenney.nl's Asset Pack 3
        main_path = constants.PLAYER_SPRITE

        # Load textures for idle standing
        #self.idle_texture_pair = load_texture_pair(f"{main_path}_idle.png")
        # Player Select
        x = 4

        self.idle_texture_pair = load_texture_pair(f"{main_path}{x}.png")

        # Load textures for walking
        self.walk_textures = []
        for i in range((0+x),(2+x)):
            texture = load_texture_pair(f"{main_path}{i}.png")
            self.walk_textures.append(texture)

    def update_animation(self, delta_time: float = 1/60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == constants.RIGHT_FACING:
            self.character_face_direction = constants.LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == constants.LEFT_FACING:
            self.character_face_direction = constants.RIGHT_FACING

        # Idle animation
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 1 * constants.UPDATES_PER_FRAME:
            self.cur_texture = 0
        frame = self.cur_texture // constants.UPDATES_PER_FRAME
        direction = self.character_face_direction
        self.texture = self.walk_textures[frame][direction]
    
    def set_past_coords(self, past_x, past_y):
        self.past_x = past_x
        self.past_y = past_y
    
    def set_past_direction(self, direction):
        self.past_direction = direction

    def update(self):
        """The player's update class. Is run every game tick."""
        super().update()
        self.idle_counter+=1
        self.determine_move()
        if self.fixing:
            if not self.is_moving:
                self.fixing = False

    def determine_move(self, target=None):
        if not self.is_moving:
            if self.idle_counter >= self.update_frames: # if it's an interval of the update time...
                #self.fixing = True # Make it so that enemies can't be pushed.
                direction = random.choice([(-1,0), (1,0), (0,-1), (0,1), (0,0)])
                self.set_past_coords = self.current_pos
                self.past_direction = direction
                self.set_move(direction)
                self.idle_counter = 0
        


    

class EnemyMover(EnemyBasic):

    def __init__(self,x,y):
        super().__init__(x,y)

        self.can_push = True
        self.update_frames = 175

        main_path = constants.PLAYER_SPRITE

        # Load textures for idle standing
        #self.idle_texture_pair = load_texture_pair(f"{main_path}_idle.png")
        # Player Select
        x = 2

        self.idle_texture_pair = load_texture_pair(f"{main_path}{x}.png")

        # Load textures for walking
        self.walk_textures = []
        for i in range((0+x),(2+x)):
            texture = load_texture_pair(f"{main_path}{i}.png")
            self.walk_textures.append(texture)
    

class EnemyAttacker(EnemyBasic):
    def __init__(self,x,y):
        super().__init__(x,y)

        self.can_push = True

        main_path = constants.PLAYER_SPRITE

        # Load textures for idle standing
        #self.idle_texture_pair = load_texture_pair(f"{main_path}_idle.png")
        # Player Select
        x = 4

        self.idle_texture_pair = load_texture_pair(f"{main_path}{x}.png")

        # Load textures for walking
        self.walk_textures = []
        for i in range((0+x),(2+x)):
            texture = load_texture_pair(f"{main_path}{i}.png")
            self.walk_textures.append(texture)