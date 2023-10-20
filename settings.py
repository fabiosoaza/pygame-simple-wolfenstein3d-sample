import math

RES = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH = WIDTH //2
HALF_HEIGHT = HEIGHT // 2

# DOOM original FPS 35
FPS = 60
PLAYER_POS = 1.5, 5  # mini_map
PLAYER_ANGLE = 0
# move speed
PLAYER_SPEED = 0.004
# rotation speed
PLAYER_ROT_SPEED = 0.002

PLAYER_SIZE_SCALE = 60

MOUSE_VISIBLE = False
MOUSE_ENABLED = False
MODE_2D = True
SIGHT_LINE = MODE_2D and True
MOUSE_SENSITIVITY = 0.0003
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT

FLOOR_COLOR = (30, 30, 30)

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
# angle between the rays
DELTA_ANGLE = FOV / NUM_RAYS
# max ray draw distance step
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

#texture resolution
TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE //2

TEXTURES_PATH='resources/textures'
SPRITES_PATH='resources/sprites'
SOUND_PATH='resources/sound'

