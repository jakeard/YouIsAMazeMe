import arcade
from arcade.sprite_list.spatial_hash import check_for_collision, check_for_collision_with_lists
from pyglet.media.player import Player
from game import constants
from game.commands import Commands
from game.boxes import Box
import random
# from game.action import Action
from game.player.player import PlayerCharacter

class HandleCollisions():
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self):
        self.pressed = False
    
    def execute(self, sprites):
        """Executes the action using the given actors.

        Args:
            sprites (dict): The game actors {key: tag, value: list}.
        """
        self.sprites = sprites
        self.player = sprites['player'][0]
        self.walls = sprites['wall_list']
        self.boxes = sprites['boxes']
        self.enemies = sprites['enemies']
        self.commands = Commands(sprites)
        self.button = sprites["button"]
        self.slimes = sprites["slimes"]
  
        self._handle_walls_collision()
        self._handle_box_collision()
        self._handle_box_environment_collision()
        self._handle_button_press()
        self._handle_enemy_collision()
        self._handle_slimes_collision()

    def _handle_slimes_collision(self):
        for slime in self.slimes:
            hit_list = arcade.check_for_collision_with_lists(slime, [self.sprites['player'], self.enemies, self.boxes])
            for collision in hit_list:
                if not collision.fixing:
                    constants.ew_sound.play(volume=1, pan=1, loop = False)
                    collision.bounce()
    
    def _handle_walls_collision(self):
        player = self.player
        if not player.fixing:
            for wall in self.walls:
                    if player.collides_with_sprite(wall):
                        num = random.randint(1,2)
                        if num == 1:
                            constants.boing_sound.play(volume=1, pan=1, loop = False)
                        elif num == 2:
                            constants.bonk_sound.play(volume=1, pan=1, loop = False)
                        player.bounce()

    def _handle_box_collision(self):
        player = self.player
        if not player.fixing:
            for box in self.boxes:
                    if player.collides_with_sprite(box):
                        # Check if the box is currently being fixed before it tries to be moved!
                        if not box.fixing:
                            num = random.randint(1,2)
                            if num == 1:
                                constants.grunt_sound.play(volume=1, pan=1, loop = False)
                            elif num == 2:
                                constants.ahh_sound.play(volume=1, pan=1, loop = False)
                            # Tell the box to move!
                            box.set_move(player.direction)
                        player.bounce()


    def _handle_box_environment_collision(self):
        for box in self.boxes:
            if not box.fixing:
                hitlist = arcade.check_for_collision_with_lists(box, [self.walls, self.boxes, self.slimes])
                if len(hitlist) != 0:
                    box.bounce()
                    for hit in hitlist:
                        #print("hit")
                        # What will this box do to whatever it collides with?
                        pass
    
    def _handle_button_press(self):
        player = self.player
        for button in self.button:
            if player.collides_with_sprite(button):
                if button.pressed == False:
                    constants.button_sound.play(volume=1, pan=1, loop = False)
                    button.pressed = True
                    button.is_pressed(button.pressed)
                    self.commands.execute(self.sprites)
            else:
                button.pressed = False
                button.is_pressed(self.pressed)

    def _handle_enemy_collision(self):
        player = self.player
        for enemy in self.enemies:
            # enemy.can_push
            # enemy.can_block
            # enemy.can_damage
            # enemy.can_be_pushed

            if enemy.can_damage:
              # This is where the player dies
                if player.collides_with_sprite(enemy):
                    constants.died_sound.play(volume=1, pan=1, loop = False)
                    self.player.hide()
            # For when the player runs into the enemy

            if not player.fixing and player.collides_with_sprite(enemy):
    
                num = random.randint(1,3)
                if num == 1:
                    constants.owie_sound.play(volume=1, pan=1, loop = False)
                elif num == 2:
                    constants.ohno_sound.play(volume=1, pan=1, loop = False)
                elif num == 3:
                    constants.ouch_sound.play(volume=1, pan=1, loop = False)
                    
                if player.is_moving:
                    #print("bouncing")
                    # Is the enemy standing still, and can it be pushed?
                    if not enemy.is_moving and not enemy.fixing and not enemy.can_block:
                        # Send the enemy away!
                        enemy.set_move(player.direction)
                    
                    player.bounce()
                else:
                    #print("shoving")
                    # For when the enemy runs into the player
                    player.fixing = True
                    player.set_move(enemy.direction)
                    enemy.bounce()
                

            if not enemy.fixing:
                # Test to see if it collides with boxes, or the wall.
                hitlist = arcade.check_for_collision_with_lists(enemy, [self.walls, self.boxes])
                if len(hitlist) != 0:
                    # Special code if the enemy runs into a box
                    for collision in hitlist:
                        if isinstance(collision, Box) and not collision.fixing: # is the object a box, and is it stationary?
                            # did the player push the box, or did the enemy run into the box?
                            collision.target_pos = collision.initial_pos
                            # If the enemy is moving, and they can legally push the block:
                            if enemy.is_moving and enemy.can_push:
                                # If the box wasn't moving beforehand...
                                if not collision.is_moving:
                                    collision.set_move(enemy.direction)
                                else:
                                    # Otherwise, just change the direction only.
                                    collision.bounce()
                            else:
                                # num = random.randint(1,2)
                                # if num == 1:
                                #     constants.boing_sound.play(volume=1, pan=1, loop = False)
                                # elif num == 2:
                                #     constants.bonk_sound.play(volume=1, pan=1, loop = False)
                                # If the enemy didn't move into it, make it reverse direction instead.
                                collision.bounce()
                    enemy.bounce()
                    
    def handle_door_collision(self, sprites):
        door = sprites['door'][0]
        player = self.player
        if player.collides_with_sprite(door):
            num = random.randint(1,3)
            if num == 1:
                constants.win_sound.play(volume=1, pan=1, loop = False)
            elif num == 2:
                constants.yay_sound.play(volume=1, pan=1, loop = False)
            elif num == 3:
                constants.hooray_sound.play(volume=1, pan=1, loop = False)
            return True
