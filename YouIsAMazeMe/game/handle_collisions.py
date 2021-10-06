import arcade

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
        player = sprites['player'][0]
        walls = sprites['walls']
        boxes = sprites['boxes']

        self._handle_walls_collision(player, walls)
        self._handle_box_collision(player, boxes)
    
    def _handle_walls_collision(self, player, walls):
        for wall in walls:
            if player.collides_with_sprite(walls):
                pass

    def _handle_box_collision(self, player, boxes):
        for box in boxes:
            if player.collides_with_sprite(box):
                pass
        
        if player.collides_with_sprite(box):
            # velocity of player
            box.center_x = int(constants.MAX_X / 2)
            box.center_y += int(constants.player_Y)