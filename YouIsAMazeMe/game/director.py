"""
Move with a Sprite Animation

Simple program to show basic sprite usage.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_animation
"""
import random, arcade 
import game.constants as constants
from game.player.player import PlayerCharacter
from game.handle_collisions import HandleCollisions
from game.immovableSprite import ImmovableSprite
from game.commands import Commands
from game.walls import Walls
from game.button import Buttons
from game.boxes import Box
from game.win import Win
from game.lose import Lose


class MainWindow(arcade.View):
    """ Main application class. """

    def __init__(self):
        """ Set up the game and initialize the variables. """
        super().__init__()

        # The sprites in this game window can be stored in a dictionary. That makes it easier to iterate through each rendered item.
        self.sprites = {}
        self.sprites["button"] = None
        self.sprites["player"] = None
        self.sprites["boxes"] = None
        self.sprites["wall_list"] = None
        self.sprites["door"] = None
        # Set up the player
        self.score = 0
        self.player = None
        self.won = None

    def setup(self):
        # Automatically sets up a SpriteList for every key.
        for key in self.sprites:
            self.sprites[key] = arcade.SpriteList()
        
        self.handle_collisions = HandleCollisions()
        
        # self.commands = Commands()
        # Set up the player
        self.score = 0
        self.player = PlayerCharacter()

        self.player.center_x = constants.SCREEN_WIDTH // 2
        self.player.center_y = constants.SCREEN_HEIGHT // 2
        self.player.scale = constants.CHARACTER_SCALING

        self.sprites["player"].append(self.player)

        for i in range(1, constants.SCREEN_HEIGHT + 15, 17):
            wall = Walls(8, i)
            self.sprites["wall_list"].append(wall)
            wall = Walls(constants.SCREEN_WIDTH - 8, i)
            self.sprites["wall_list"].append(wall)
        for i in range(1, constants.SCREEN_WIDTH, 17):
            try:
                wall = Walls(i, constants.SCREEN_HEIGHT - 8)
                self.sprites["wall_list"].append(wall)
            except ValueError:
                pass
            try:
                wall = Walls(i, 8)
                self.sprites["wall_list"].append(wall)
            except ValueError:
                pass
        
        # 80, 108
        button = Buttons(80, 108)
        # button.center_x = 80
        # button.center_y = 108
        self.sprites["button"].append(button)
    
        door = ImmovableSprite(constants.SCREEN_WIDTH + constants.TILE_SIZE, constants.SCREEN_HEIGHT + constants.TILE_SIZE, constants.DOOR_SPRITE)
        self.sprites["door"].append(door)
        # 592 236
        box = Box(464, 300, 'start')
        self.sprites['boxes'].append(box) # BLOCKS NEED TO GO IN ORDER THAT THEY WOULD BE IN NORMALLY FOR A COMMAND (ex: print, then object, then closing bracket)
        box = Box(272, 364, "del(")       # BLOCKS NEED TO GO IN ORDER THAT THEY WOULD BE IN NORMALLY FOR A COMMAND
        self.sprites["boxes"].append(box) # BLOCKS NEED TO GO IN ORDER THAT THEY WOULD BE IN NORMALLY FOR A COMMAND
        box = Box(528, 300, "print(")     # BLOCKS NEED TO GO IN ORDER THAT THEY WOULD BE IN NORMALLY FOR A COMMAND
        self.sprites["boxes"].append(box) # BLOCKS NEED TO GO IN ORDER THAT THEY WOULD BE IN NORMALLY FOR A COMMAND
        box = Box(592, 300, "door")       # BLOCKS NEED TO GO IN ORDER THAT THEY WOULD BE IN NORMALLY FOR A COMMAND
        self.sprites["boxes"].append(box) # BLOCKS NEED TO GO IN ORDER THAT THEY WOULD BE IN NORMALLY FOR A COMMAND
        box = Box(656, 300, "')")         # BLOCKS NEED TO GO IN ORDER THAT THEY WOULD BE IN NORMALLY FOR A COMMAND
        self.sprites["boxes"].append(box) # BLOCKS NEED TO GO IN ORDER THAT THEY WOULD BE IN NORMALLY FOR A COMMAND
        # box = Box(720, 300, "World'")
        # self.sprites["boxes"].append(box)

        self.commands = Commands(self.sprites)
        # Set the background color
        arcade.set_background_color(arcade.color.KHAKI)

    def on_draw(self):
        """
        Render the screen. This function is called every frame.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Iterates through every key in the sprite dict, and draws them.
        for key in self.sprites:
            self.sprites[key].draw()

        # Put the text on the screen.
        # output = f"Score: {self.score}"
        arcade.draw_text("R - Restart", 20, 20, arcade.color.RUST, 14)

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        player = self.sprites['player'][0] 
        # Only accept these inputs if the player is not moving
        if not player.is_moving:  # I'm moving! I don't want to be able to move again.
            player.set_past_coords(player.center_x, player.center_y)
            if key == arcade.key.UP or key == arcade.key.W:
                direction = (0,1)
            elif key == arcade.key.DOWN or key == arcade.key.S:
                direction = (0,-1)
            elif key == arcade.key.RIGHT or key == arcade.key.D:
                direction = (1,0)
            elif key == arcade.key.LEFT or key == arcade.key.A:
                direction = (-1,0)
            else:
                direction = (0,0)
            player.set_past_direction(direction)
            self.handle_collisions.fixing = False

            player.set_move(direction)
        # All other key presses go after this statement
        if key == arcade.key.R:
            self.setup()
       
    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """
        pass

    def on_update(self, delta_time):
        """ Movement and game logic """
        for key in self.sprites:
            # Runs each sprite's update() method.
            self.sprites[key].update()
            # Runs each sprite's update_animation() method.
            self.sprites[key].update_animation()
        self._cue_action("update")
        # self.won = True
        if not self.won is None:
            if self.won:
                view = Win()
            elif not self.won:
                view = Lose()
            self.window.show_view(view)

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        self.handle_collisions.execute(self.sprites)
        # self.commands.execute(self.sprites)
        # Generate a list of all sprites that collided with the player.
    
    def change_win_status(self, status):
        self.won = status
