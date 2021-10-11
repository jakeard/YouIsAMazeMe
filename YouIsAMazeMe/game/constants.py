import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Move with a Sprite Animation Example"

# COIN_SCALE = 0.5
# COIN_COUNT = 50
CHARACTER_SCALING = 2.5
SPRITE_SCALING = 1

# How fast to move, and how fast to run the animation
# MOVEMENT SPEED MUST BE A POWER OF 2
MOVEMENT_SPEED = 4
UPDATES_PER_FRAME = 1

# Constants used to track if the player is facing left or right
RIGHT_FACING = 1
LEFT_FACING = 0

# One tile is how many pixels?
TILE_SIZE = 64

PATH = os.path.dirname(os.path.abspath(__file__))

# Asset Pathing
PLAYER_SPRITE = os.path.join(PATH, '..', 'assets','kenney_assets', 'Characters', 'character_000') # Trim off the last digit and .png 
WALL_SPRITE = os.path.join(PATH, '..', 'assets', 'kenney_assets', 'Tiles', 'tile_0000.png')
MOVING_WALL_SPRITE = ""



