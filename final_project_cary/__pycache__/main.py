# This file was created by Cary Yao
# Sources: 
# https://levelup.gitconnected.com/writing-tetris-in-python-2a16bddb5318 

# Goals:
# Make platforms that are different shapes
# Make platforms constantly move down
# Make platforms stop on other platforms/the bottom of the window
# Make line disappear once entire line is filled
# Make score go up 1 when line disappears, more points for tetris
# Make platforms rotate
# harder/more levels (faster falling speed)

import pygame as pg
import random

# Screen dimensions
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 25

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255,255,0)
ORANGE = (255,165,0)
PURPLE = (128,0,128)
COLORS = [RED, BLUE, GREEN, ORANGE, YELLOW, PURPLE]

# Tetris pieces
FIGURES = [
    [
        ['.....',
         '.....',
         '.....',
         'OOOO.',
         '.....'],
        ['.....',
         '..O..',
         '..O..',
         '..O..',
         '..O..']
    ],
    [
        ['.....',
         '.....',
         '..O..',
         '.OOO.',
         '.....'],
        ['.....',
         '..O..',
         '.OO..',
         '..O..',
         '.....'],
        ['.....',
         '.....',
         '.OOO.',
         '..O..',
         '.....'],
        ['.....',
         '..O..',
         '..OO.',
         '..O..',
         '.....']
    ],
    [
        [
         '.....',
         '.....',
         '..OO.',
         '.OO..',
         '.....'],
        ['.....',
         '.....',
         '.OO..',
         '..OO.',
         '.....'],
        ['.....',
         '.O...',
         '.OO..',
         '..O..',
         '.....'],
        ['.....',
         '..O..',
         '.OO..',
         '.O...',
         '.....']
    ],
    [
        ['.....',
         '..O..',
         '..O.',
         '..OO.',
         '.....'],
        ['.....',
         '...O.',
         '.OOO.',
         '.....',
         '.....'],
        ['.....',
         '.OO..',
         '..O..',
         '..O..',
         '.....'],
        ['.....',
         '.....',
         '.OOO.',
         '.O...',
         '.....']
    ],
]



# figure class
class Figure:
    def __init__(self, x, y, shape):
        # defines shapes using 
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(COLORS)
        self.rotation = 0

    def update(self):
        self.speed = 5
        self.rect.y += self.speed
        if self.rect.y + self.rect.h > HEIGHT or self.rect.y < 0:
            self.speed = -self.speed

        
class Game:
    def __init__ (self, width, height):
        self.height = height
        self.width = width
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.current_figure = self.new_figure()
        self.score = 0

    def new_figure(self):
        shape = random.choice(FIGURES)
        return Figure(self.width // 2,0, shape)

