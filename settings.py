import math

RES = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH = WIDTH //2
HALF_HEIGHT = HEIGHT // 2

FPS = 60
PLAYER_POS = 1.5, 5  # mini_map
PLAYER_ANGLE = 0
# move speed
PLAYER_SPEED = 0.004
# rotation speed
PLAYER_ROT_SPEED = 0.002

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
# angle between the rays
DELTA_ANGLE = FOV / NUM_RAYS
# draw distance
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS
