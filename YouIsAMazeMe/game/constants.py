import os
import arcade

"""
Holds all constants used for the program.
"""

SCREEN_WIDTH = 1216 
SCREEN_HEIGHT = 768 
SCREEN_TITLE = "You Is AMaze Me"

WIDTH_RATIO = SCREEN_WIDTH / 800
HEIGHT_RATIO = SCREEN_HEIGHT / 600



CHARACTER_SCALING = .9
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

#Sounds
PIXEL = os.path.join(PATH, '..', 'assets', 'sounds', 'pixel_polka.mp3')
AUTUMN = os.path.join(PATH, '..', 'assets', 'sounds', 'autumn_day.mp3')
BOING = os.path.join(PATH, '..', 'assets', 'sounds', 'boing.mp3')
BONK = os.path.join(PATH, '..', 'assets', 'sounds', 'bonk.mp3')
HOORAY = os.path.join(PATH, '..', 'assets', 'sounds', 'hooray.mp3')
YAY = os.path.join(PATH, '..', 'assets', 'sounds', 'yay.mp3')
IWIN = os.path.join(PATH, '..', 'assets', 'sounds', 'i_win.mp3')
OHNO = os.path.join(PATH, '..', 'assets', 'sounds', 'oh_no.mp3')
OUCH = os.path.join(PATH, '..', 'assets', 'sounds', 'ouch.mp3')
OWIE = os.path.join(PATH, '..', 'assets', 'sounds', 'owie.mp3')
AHH = os.path.join(PATH, '..', 'assets', 'sounds', 'ahh.mp3')
GRUNT = os.path.join(PATH, '..', 'assets', 'sounds', 'grunt.mp3')
BUTTON = os.path.join(PATH, '..', 'assets', 'sounds', 'button.mp3')
DIED = os.path.join(PATH, '..', 'assets', 'sounds', 'idied.mp3')
EW = os.path.join(PATH, '..', 'assets', 'sounds', 'eww.mp3')

autumn_sound = arcade.Sound(AUTUMN)
pixel_sound = arcade.Sound(PIXEL)
ouch_sound = arcade.Sound(OUCH)
owie_sound = arcade.Sound(OWIE)
ahh_sound = arcade.Sound(AHH)
ohno_sound = arcade.Sound(OHNO)
win_sound = arcade.Sound(IWIN)
yay_sound = arcade.Sound(YAY)
hooray_sound = arcade.Sound(HOORAY)
bonk_sound = arcade.Sound(BONK)
boing_sound = arcade.Sound(BOING)
grunt_sound = arcade.Sound(GRUNT)
button_sound = arcade.Sound(BUTTON)
died_sound = arcade.Sound(DIED)
ew_sound = arcade.Sound(EW)

# Asset Pathing
NEW_PLAYER_SPRITE = os.path.join(PATH, '..', 'assets', 'images', 'character_000') # Trim off the last digit and .png 
PLAYER_SPRITE = os.path.join(PATH, '..', 'assets','kenney_assets', 'Characters', 'character_000') # Trim off the last digit and .png 
WALL_SPRITE = os.path.join(PATH, '..', 'assets', 'kenney_assets', 'Tiles', 'tile_0006.png')
BACKGROUND_SPRITE = os.path.join(PATH, '..', 'assets', 'kenney_assets', 'Tiles', 'tile_0122.png')
MOVING_WALL_SPRITE = os.path.join(PATH, '..', 'assets', 'kenney_assets', 'Tiles', 'tile_0026.png')
FLAG_SPRITE = os.path.join(PATH, '..', 'assets', 'kenney_assets', 'Tiles', 'tile_0112.png')
DOOR_SPRITE = os.path.join(PATH, '..', 'assets', 'images', 'tile_0150.png')
SLIME_SPRITE = os.path.join(PATH, '..', 'assets', 'images', 'slimeBlock.png')
GRASS_SPRITE = os.path.join(PATH, '..', 'assets', 'images', 'grass5.png')
KEY_SPRITE = os.path.join(PATH, '..', 'assets', 'kenney_assets', 'Tiles', 'tile_0027.png')
LOCK_SPRITE = os.path.join(PATH, '..', 'assets', 'kenney_assets', 'Tiles', 'tile_0028.png')
BUTTON_SPRITE = os.path.join(PATH, '..', 'assets', 'images', 'button.png')
BUTTON_PRESSED_SPRITE = os.path.join(PATH, '..', 'assets', 'images', 'button_pressed.png')
BACKGROUND_SPRITE = os.path.join(PATH, '..', 'assets', 'kenney_assets', 'Background', 'background_0002.png')
START_SCREEN = os.path.join(PATH, '..', 'assets', 'images', 'start_screen.png')
WIN_SCREEN = os.path.join(PATH, '..', 'assets', 'images', 'win.png')
LOSE_SCREEN = os.path.join(PATH, '..', 'assets', 'images', 'you_lose.png') 
CODE_BLOCKS = os.path.join(PATH, '..', 'assets', 'images')
ENEMY_BASIC_SPRITE = os.path.join(PATH, '..', 'assets', 'kenney_assets', 'Enemy_sprites', 'snail')
ENEMY_MOVER_SPRITE = os.path.join(PATH, '..', 'assets', 'kenney_assets', 'Enemy_sprites', 'fly')
ENEMY_ATTACKER_SPRITE = os.path.join(PATH, '..', 'assets', 'kenney_assets', 'Enemy_sprites', 'spider')
ENEMY_OBSTACLE_SPRITE = os.path.join(PATH, '..', 'assets', 'kenney_assets', 'Enemy_sprites', 'slime')
INSTRUCT = os.path.join(PATH, '..', 'assets', 'images', 'instructions.png')



