import arcade
from game.action import Action
# from game.player.player import PlayerCharacter

class HandleCollisions():
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    
    def execute(self, sprites):
        """Executes the action using the given actors.

        Args:
            sprites (dict): The game actors {key: tag, value: list}.
        """
        self.player = sprites['player'][0]
        # self.walls = sprites['walls']
        # self.boxes = sprites['boxes']
        self.sprites = sprites

        self._handle_walls_collision()
        # self._handle_box_collision()
    
    def _handle_walls_collision(self):
        # for wall in self.walls:
            # if self.player.collides_with_sprite(wall):
        
        if self.player.center_y < 65:
            self.player.center_y = 64
            self.player.change_y = 0
        elif self.player.center_y > 600:
            self.player.center_y = 599
            self.player.change_y = 0

    # def _handle_box_collision(self, player, boxes):
    #     for box in boxes:
    #         if player.collides_with_sprite(box):
    #             pass
        
        # if player.collides_with_sprite(box):
        #     # velocity of player
        #     box.center_x = int(constants.MAX_X / 2)
        #     box.center_y += int(constants.player_Y)