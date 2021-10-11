import arcade
from game import constants
# from game.action import Action
# from game.player.player import PlayerCharacter

class HandleCollisions():
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self):
        self.fixing = False
    
    def execute(self, sprites):
        """Executes the action using the given actors.

        Args:
            sprites (dict): The game actors {key: tag, value: list}.
        """
        self.player = sprites['player'][0]
        self.walls = sprites['wall_list']
        # self.boxes = sprites['boxes']

        self._handle_walls_collision()
        # self._handle_box_collision()
    
    def _handle_walls_collision(self):
        player = self.player
        for wall in self.walls:
            if not self.fixing:
                if player.collides_with_sprite(wall):
                    self.fixing = True
                    direction = (player.direction[0] * -1, player.direction[1] * -1)
                    player.direction = direction
                    player.target_pos = player.initial_pos

    # def _handle_box_collision(self, player, boxes):
    #     for box in boxes:
    #         if player.collides_with_sprite(box):
    #             pass
        
        # if player.collides_with_sprite(box):
        #     # velocity of player
        #     box.center_x = int(constants.MAX_X / 2)
        #     box.center_y += int(constants.player_Y)