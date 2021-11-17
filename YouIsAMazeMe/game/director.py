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
from game.level_loader import LevelLoader


class MainWindow(arcade.View):
    """ Main application class. """

    def __init__(self, level=None):
        """ Set up the game and initialize the variables. """
        super().__init__()
        if level is not None:
            self.level = level
        else:
            self.level = 1

        # The sprites in this game window can be stored in a dictionary. That makes it easier to iterate through each rendered item.
        self.sprites = {}
        self.sprites["grass"] = None
        self.sprites["button"] = None
        self.sprites["boxes"] = None
        self.sprites["wall_list"] = None
        self.sprites["door"] = None
        self.sprites["player"] = None
        self.sprites["enemies"] = None

        # Set up the player
        self.score = 0
        self.player = None
        self.won = None

    def setup(self):
        # Automatically sets up a SpriteList for every key.
        for key in self.sprites:
            self.sprites[key] = arcade.SpriteList()
        
        self.handle_collisions = HandleCollisions()
        
        # Set up the player
        for x in range(0, constants.SCREEN_WIDTH + constants.TILE_SIZE, constants.TILE_SIZE):
            for y in range(0, constants.SCREEN_HEIGHT + constants.TILE_SIZE, constants.TILE_SIZE):
                grass = ImmovableSprite(x, y, constants.GRASS_SPRITE)
                self.sprites["grass"].append(grass)
        loader = LevelLoader(self.sprites, self.level)
        loader.load_level()
        

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
        arcade.draw_text("R - Restart", constants.TILE_SIZE/2, constants.SCREEN_HEIGHT - constants.TILE_SIZE/3, arcade.color.WHITE, 16)

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
        delta_time += 1
        for key in self.sprites:
            # Runs each sprite's update() method.
            self.sprites[key].update()
            # Runs each sprite's update_animation() method.
            self.sprites[key].update_animation()
        self._cue_action("update")
        if not self.won is None:
            if self.won:
                view = Win(self.level)
            elif not self.won:
                view = Lose()
            self.window.show_view(view)

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        self.handle_collisions.execute(self.sprites)
        self.won = self.handle_collisions.handle_door_collision(self.sprites)
    
    def change_win_status(self, status):
        self.won = status
