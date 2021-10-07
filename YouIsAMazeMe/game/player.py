import arcade
import game.constants as constants


def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True)
    ]

class PlayerCharacter(arcade.Sprite):
    def __init__(self):

        # Set up parent class
        super().__init__()

        # Default to face-right
        self.character_face_direction = constants.RIGHT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0

        self.scale = constants.CHARACTER_SCALING

        # Adjust the collision box. Default includes too much empty space
        # side-to-side. Box is centered at sprite center, (0, 0)
        self.points = [[-22, -64], [22, -64], [22, 28], [-22, 28]]

        # --- Load Textures ---

        # Images from Kenney.nl's Asset Pack 3
        main_path = ":resources:images/animated_characters/female_adventurer/femaleAdventurer"
        # main_path = ":resources:images/animated_characters/female_person/femalePerson"
        # main_path = ":resources:images/animated_characters/male_person/malePerson"
        # main_path = ":resources:images/animated_characters/male_adventurer/maleAdventurer"
        # main_path = ":resources:images/animated_characters/zombie/zombie"
        # main_path = ":resources:images/animated_characters/robot/robot"

        # Load textures for idle standing
        self.idle_texture_pair = load_texture_pair(f"{main_path}_idle.png")

        # Load textures for walking
        self.walk_textures = []
        for i in range(8):
            texture = load_texture_pair(f"{main_path}_walk{i}.png")
            self.walk_textures.append(texture)

        # Movement constants
        self.is_moving = False
        self.direction = (0,0)
        self.current_pos = (self.center_x, self.center_y)
        self.target_pos = self.current_pos

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
        if self.cur_texture > 7 * constants.UPDATES_PER_FRAME:
            self.cur_texture = 0
        frame = self.cur_texture // constants.UPDATES_PER_FRAME
        direction = self.character_face_direction
        self.texture = self.walk_textures[frame][direction]

    def set_move(self, direction: tuple = (0,0)):
        self.direction = direction
        self.is_moving = True
        self.target_pos = ((self.center_x+(direction[0]*constants.TILE_SIZE)), (self.center_y+(direction[1]*constants.TILE_SIZE)))
        #print(f"Current pos: {self.current_pos}, target pos: {self.target_pos}")
    
    def move(self):
        """Method that gets called during update, used to move."""
        # Am I at my target location?
        #print(f"Current pos: {self.current_pos}, target pos: {self.target_pos}")
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