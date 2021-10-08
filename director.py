"""
Move with a Sprite Animation

Simple program to show basic sprite usage.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_animation
"""
import random
import arcade
import game.constants as constants
from game.player import PlayerCharacter
from game.handle_collisions import HandleCollisions


class MainWindow(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """ Set up the game and initialize the variables. """
        super().__init__(width, height, title)

        # The sprites in this game window can be stored in a dictionary. That makes it easier to iterate through each rendered item.
        self.sprites = {}
        self.sprites["player"] = None
        # self.sprites["coins"] = None
        self.sprites["wall_list"] = None

        # Set up the player
        self.score = 0
        self.player = None

    def setup(self):
        # Automatically sets up a SpriteList for every key.
        for key in self.sprites:
            self.sprites[key] = arcade.SpriteList()

        self.camera = arcade, camera(self.width, self)

        self.handle_collisions = HandleCollisions()
        # Set up the player
        self.score = 0
        self.player = PlayerCharacter()

        self.player.center_x = constants.SCREEN_WIDTH // 2
        self.player.center_y = constants.SCREEN_HEIGHT // 2
        self.player.scale = 0.8

        self.sprites["player"].append(self.player)

        wall = arcade.Sprite(
            ":resources:images/tiles/boxCrate_double.png", constants.SPRITE_SCALING)
        wall.center_x = 350
        wall.center_y = 350
        self.sprites["wall_list"].append(wall)

        # for i in range(constants.COIN_COUNT):
        #     coin = arcade.Sprite(":resources:images/items/gold_1.png",
        #                          scale=0.5)
        #     coin.center_x = random.randrange(constants.SCREEN_WIDTH)
        #     coin.center_y = random.randrange(constants.SCREEN_HEIGHT)

        #     self.sprites["coins"].append(coin)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen. This function is called every frame.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        self.camera.use()

        # Iterates through every key in the sprite dict, and draws them.
        for key in self.sprites:
            self.sprites[key].draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        # Only accept these inputs if the player is not moving
        # I'm moving! I don't want to be able to move again.
        if not self.sprites["player"][0].is_moving:
            if key == arcade.key.UP or key == arcade.key.W:
                direction = (0, 1)
            elif key == arcade.key.DOWN or key == arcade.key.S:
                direction = (0, -1)
            elif key == arcade.key.RIGHT or key == arcade.key.D:
                direction = (1, 0)
            elif key == arcade.key.LEFT or key == arcade.key.A:
                direction = (-1, 0)
            else:
                direction = (0, 0)

            self.sprites["player"][0].set_move(direction)
        # All other key presses go after this statement

    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """
        pass

        def center_camera_to_player(self):
            screen_center_x = (self.player.center_x -
                               (self.camera.viewport_height / 2))
            screen_center_y = (self.player.center_y -
                               (self.camera.viewport_height / 2))

        # Don't let camera travel past 0
            if screen_center_x < 0:
                screen_center_x = 0
            if screen_center_y < 0:
                screen_center_y = 0
            player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)

    def _cue_action(self, tag):
        """Executes the actions with the given tag.

        Args:
            tag (string): The given tag.
        """
        self.handle_collisions.execute(self.sprites)
        # Generate a list of all sprites that collided with the player.
        # hit_list = arcade.check_for_collision_with_list(self.player, self.sprites["coins"])

        # Loop through each colliding sprite, remove it, and add to the score.
        # for coin in hit_list:
        #     coin.remove_from_sprite_lists()
        #     self.score += 1

    def on_update(self, delta_time):
        """ Movement and game logic """

        for key in self.sprites:
            # Runs each sprite's update() method.
            self.sprites[key].update()
            # Runs each sprite's update_animation() method.
            self.sprites[key].update_animation()
        self._cue_action("update")
        self.center_camera_to_player()
