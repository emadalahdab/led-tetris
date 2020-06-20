""" Store global constants """
# LEDmatrix configuration
CHAIN_LENGTH = 3
PARALLEL_CHAINS = 2
LED_BRIGHTNESS = 100

# The dimensions of the board
BOARD_WIDTH = 96
BOARD_HEIGHT = 64

# Game properties
NUM_GAMES = 6
GAME_SPEED = 150
DROP_SPACING = 16

# Heuristic factors
COMPLETE_LINES_FACTOR = 50
COVERED_EMPTY_SPACES_FACTOR = -2
TOTAL_EMPTY_SPACES_FACTOR = -0.5
AVERAGE_COLUMN_HEIGHT_FACTOR = -2
HEIGHT_VARIATION_FACTOR = -0.1
DISTANCE_FACTOR = -0.01
