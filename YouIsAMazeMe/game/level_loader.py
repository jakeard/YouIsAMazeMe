import game.constants as constants
from game.walls import Walls
from game.boxes import Box
from game.player.player import PlayerCharacter

class levelLoader():

    def __init__(self, sprite_dict):

        self.current_level = 0
        self.level_dir = "YouIsAMazeMe/levels"
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
        #print(f"Sprite: {sprite} ; location: {x}, {y}")

        if sprite == "w":
            # add wall at specified coordinates
            wall = Walls(x,y)
            self.sprites["wall_list"].append(wall)
            pass
        elif sprite == "p":
            # player
            player = PlayerCharacter(x,y)
            self.sprites["player"].append(player)
        elif sprite == "c":
            # box
            box = Box(x,y)
            self.sprites["boxes"].append(box)
        elif sprite == "vw":
            wall = Walls(x,y)
            self.sprites["wall_list"].append(wall)
            # vertical wall
            pass
        elif sprite == "hw":
            wall = Walls(x,y)
            self.sprites["wall_list"].append(wall)
            # horizontal wall

    def next_level(self):
        pass
    
