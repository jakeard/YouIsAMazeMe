import game.constants as constants
from game.walls import Walls, ThinWalls
from game.boxes import Box
from game.button import Buttons
from game.player.player import PlayerCharacter
from game.immovableSprite import ImmovableSprite
import game.enemy.enemies as enemies
import arcade

class LevelLoader():
    """
    Loads a level with all sprites based on a CSV file that is 
    determined from the current level that is passed in.
    """
    def __init__(self, choose_level, sprite_dict=None, curr_level=1):
        if choose_level is None:
            self.current_level = curr_level
        else:
            self.current_level = choose_level
        self.level_dir = "YouIsAMazeMe/levels"
        self.sprites = {}
        if sprite_dict is not None:
            self.sprites = sprite_dict
        
    
    def load_level(self):

        level_path = f"{self.level_dir}/level_{self.current_level:02d}.csv"
        tile_size = constants.TILE_SIZE

        with open(level_path) as level:
            y = constants.SCREEN_HEIGHT
            for row in level:
                x = 0
                curr_char = ""
                for n in row:
                    if n != ",":
                        curr_char = f"{curr_char}{n}"
                    else:
                        self._load_tile(curr_char.strip(), x, y)
                        curr_char = ""
                        x += tile_size
                # Call it again after the for loop, since not all rows will end with a comma
                self._load_tile(curr_char.strip(),x,y)
                y -= tile_size

    def _load_tile(self, sprite, x, y):

        if sprite == "w":
            # add wall at specified coordinates
            wall = Walls(x,y)
            self.sprites["wall_list"].append(wall)
        
        elif sprite == "c":
            # add a 'crate' or 'box'
            box = Box(x,y)
            self.sprites["boxes"].append(box)
        elif sprite == "p":
            # player
            player = PlayerCharacter(x,y)
            self.sprites["player"].append(player)
        
        elif sprite == "b":
            button = Buttons(x, y)
            self.sprites["button"].append(button)
        
        elif sprite == "d":
            # door
            door = ImmovableSprite(x, y, constants.DOOR_SPRITE)
            self.sprites["door"].append(door)
        
        elif sprite == "s":
            # door
            slime = ImmovableSprite(x, y, constants.SLIME_SPRITE)
            self.sprites["slimes"].append(slime)

        elif sprite == "start":
            # box
            box = Box(x, y, 'start')
            self.sprites["boxes"].append(box)
        
        elif sprite == "print":
            # box
            box = Box(x, y, 'print(')
            self.sprites["boxes"].append(box)
        
        elif sprite == "del":
            # box
            box = Box(x, y, 'del(')
            self.sprites["boxes"].append(box)
        
        elif sprite == "door":
            # box
            box = Box(x, y, 'door')
            self.sprites["boxes"].append(box)
        
        elif sprite == "bugs":
            # box
            box = Box(x, y, 'bugs')
            self.sprites["boxes"].append(box)

        elif sprite == "slimes":
            # box
            box = Box(x, y, 'slimes')
            self.sprites["boxes"].append(box)
        
        elif sprite == ")":
            # box
            box = Box(x, y, ')')
            self.sprites["boxes"].append(box)
            
        elif sprite == "vw":
            wall = ThinWalls(x,y,1)
            self.sprites["wall_list"].append(wall)
            # vertical wall
            pass
        elif sprite == "hw":
            wall = ThinWalls(x,y,0)
            self.sprites["wall_list"].append(wall)
            # horizontal wall

        elif sprite == "eb":
            enemy_basic = enemies.EnemyBasic(x,y)
            self.sprites["enemies"].append(enemy_basic)
        
        elif sprite == "em":
            enemy_mover = enemies.EnemyMover(x,y)
            self.sprites["enemies"].append(enemy_mover)

        elif sprite == "ea":
            enemy_attacker = enemies.EnemyAttacker(x,y)
            self.sprites["enemies"].append(enemy_attacker)

    def next_level(self):
        self.current_level += 1