from game.shared.color import Color
import random

COLUMNS = 40
ROWS = 20
CELL_SIZE = 15
MAX_X = 900
MAX_Y = 600
FRAME_RATE = 15
FONT_SIZE = 15
CAPTION = "SNAKE"
SNAKE_LENGTH = 8
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
ORANGE = Color(255,165,0)
AQUA = Color(0, 255, 255)
BLUE = (0,0,255)
Colors = [RED, YELLOW, GREEN, ORANGE, AQUA,BLUE]
Color = random.choice(Colors)

