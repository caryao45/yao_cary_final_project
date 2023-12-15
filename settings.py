# This file was created by: Chris Cozort
# Content from Chris Bradfield; Kids Can Code
# KidsCanCode - Game Development with Pygame video series
# Video link: https://youtu.be/OmlQ0XCvIn0 

# game settings 
WIDTH = 720
HEIGHT = 720
FPS = 30

# player settings
PLAYER_JUMP = 25
PLAYER_GRAV = 1.5
PLAYER_FRIC = 0.2

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (102, 178, 255)
YELLOW = (255, 255, 0)
GRAY = (128,128,128)

PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, "normal")]
HOOP_PLACEMENT = [(500,350)]
BALL_PLACEMENT = [(WIDTH/2,650)]