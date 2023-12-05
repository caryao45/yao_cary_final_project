# This file was created by Cary Yao
# Sources: 
# https://levelup.gitconnected.com/writing-tetris-in-python-2a16bddb5318 

# Goals:
# format in grid
# Make platforms that are different shapes
# Make platforms constantly move down
# Make platfroms stop on other platforms/the bottom of the window
# Make line disappear once entire line is filled
# Make score go up 1 when line disappears, more points for tetris
# Make platforms rotate
# harder levels (faster falling speed)
# more levels 



import pygame as pg
import random


# figure class
class Figure:
    def __init__(self, x, y):
        # defines shapes using 
        self.figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
        [[1, 5, 6, 10], [1, 2, 4, 5]],
        [[1, 4, 5, 8], [0, 1, 5, 6]]
        ]
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.rotation = 0

    def piece_image(self):
        return self.figures[self.type][self.rotation]
    
    def rotation(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])
        
class Game:
    WIDTH = 600
    HEIGHT = 600
    FPS = 30
    def __ini__ (self):
        # init pygame and create a window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption("My Game...")
        self.clock = pg.time.Clock()
        self.running = True

    def new(self): 
            # create a group for all sprites
            self.score = 0
            self.all_figures = pg.sprite.Group()

            # prints platforms
                # instantiation of the Platform class
            fig = Figure
            self.all_platforms.add(fig)

            self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(self.FPS)
            self.events()

    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False


g = Game()
while g.running:
    g.new()

pg.quit()
