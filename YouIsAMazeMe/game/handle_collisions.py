import arcade
from game import constants
from game.commands import Commands
from game.boxes import Box
# from game.action import Action
# from game.player.player import PlayerCharacter

class HandleCollisions():
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self):
        self.fixing = False
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
        # self.door = sprites['door']
        # self.button = sprites['button'][0]
        self.commands = Commands(sprites)
        self.button = sprites["button"]

        self._handle_walls_collision()
        self._handle_box_collision()
        self._handle_box_environment_collision()
        self._handle_button_press()
        self._handle_enemy_collision()
    
    def _handle_walls_collision(self):
        player = self.player
        for wall in self.walls:
            if not self.fixing:
                if player.collides_with_sprite(wall):
                    self.fixing = True
                    direction = (player.direction[0] * -1, player.direction[1] * -1)
                    player.direction = direction
                    player.target_pos = player.initial_pos
    
    # def _handle_button_collision(self):
    #     player = self.player
    #     for button in self.button:
    #         if not self.fixing:
    #             if player.collides_with_sprite(wall):
    #                 self.fixing = True
    #                 direction = (player.direction[0] * -1, player.direction[1] * -1)
    #                 player.direction = direction
    #                 player.target_pos = player.initial_pos

    def _handle_box_collision(self):
        player = self.player
        for box in self.boxes:
            if not self.fixing:
                if player.collides_with_sprite(box):
                    # Check if the box is currently being fixed before it tries to be moved!
                    if not box.fixing:
                        # Tell the box to move!
                        box.set_move(player.direction)
                    self.fixing = True
                    direction = (player.direction[0] * -1, player.direction[1] * -1)
                    player.direction = direction
                    player.target_pos = player.initial_pos

        # if player.collides_with_sprite(box):
        #     # velocity of player
        #     box.center_x = int(constants.MAX_X / 2)
        #     box.center_y += int(constants.player_Y)

    def _handle_box_environment_collision(self):
        for box in self.boxes:
            if not box.fixing:
                hitlist = arcade.check_for_collision_with_lists(box, [self.walls, self.boxes])
                if len(hitlist) != 0:
                    box.fixing = True
                    new_direction = (box.direction[0]*-1, box.direction[1]*-1)
                    box.direction = new_direction
                    box.target_pos = box.initial_pos
                    for hit in hitlist:
                        #print("hit")
                        # What will this box do to whatever it collides with?
                        pass
    
    def _handle_button_press(self):
        player = self.player
        for button in self.button:
            if player.collides_with_sprite(button):
                if button.pressed == False:
                    button.pressed = True
                    button.is_pressed(button.pressed)
                    self.commands.execute(self.sprites)
            else:
                button.pressed = False
                button.is_pressed(self.pressed)

    def _handle_enemy_collision(self):
        for enemy in self.enemies:
            # enemy.can_push
            # enemy.can_block
            # enemy.can_damage
            # enemy.can_be_pushed
            player = self.player

            # For when the player runs into the enemy
            if player.collides_with_sprite(enemy) and not self.fixing:

                # Is the enemy standing still, and can it be pushed?
                if not enemy.fixing and not enemy.can_block:
                    # Send the enemy away!
                    enemy.set_move(player.direction)
                    if enemy.can_damage:
                        # TODO: Add code here, telling the player/director/whoever that the player took damage
                        pass
                
                self.fixing = True
                direction = (player.direction[0] * -1, player.direction[1] * -1)
                player.direction = direction
                player.target_pos = player.initial_pos
                

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
                                    collision.direction = (enemy.direction)
                            else:
                                # If the enemy didn't move into it, make it reverse direction instead.
                                collision.direction = ((collision.direction[0]*-1, collision.direction[1]*-1))
                            collision.fixing = True
                    enemy.fixing = True
                    direction = (enemy.direction[0] * -1, enemy.direction[1] * -1)
                    enemy.direction = direction
                    enemy.target_pos = enemy.initial_pos
                    