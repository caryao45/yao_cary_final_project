# This file was created by Cary Yao
# Sources: 
# https://levelup.gitconnected.com/writing-tetris-in-python-2a16bddb5318 

# Goals:
# Make platforms that are different shapes
# Make platforms constantly move down
# Make platfroms stop on other platforms/the bottom of the window
# Make line disappear once entire line is filled
# Make score go up 1 when line disappears, more points for tetris
# Make platforms rotate
# harder/more levels (faster falling speed)

import pygame as pg
import random

WIDTH = 600
HEIGHT = 600
FPS = 30

BLACK = (0,0,0)

colors = [
    (255,0,0),
    (0,255,0),
    (0,0,255),
    (255,255,0),
    (255,140,0),
    (128,0,128),
    (0,255,255),
]

FIGURE_LIST = [
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

# figure class
class Figure:
    def __init__(self, x, y):
        # defines shapes using 
        self.x = x
        self.y = y
        self.type = random.randint(0, len(FIGURE_LIST) - 1)
        self.color = random.randint(1, len(colors) - 1)
        self.rotation = 0

    def piece_image(self):
        return self.figures[self.type][self.rotation]
    
    def rotation(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])

    def update(self):
        self.speed = 5
        self.rect.y += self.speed
        if self.rect.y + self.rect.h > HEIGHT or self.rect.y < 0:
            self.speed = -self.speed

        
class Game:
    WIDTH = 600
    HEIGHT = 600
    FPS = 30
    def __init__ (self):
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
        self.all_sprites = pg.sprite.Group()
        self.all_figures = pg.sprite.Group()

        for f in FIGURE_LIST:
            # instantiation of Figure class
            fig = Figure(*f)
            self.all_figures.add(fig)

        self.run()
    
    def new_figure(self):
        self.figure = Figure(3,0)

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

    def draw(self):
            ############ Draw ################
            # draw the background screen
            self.screen.fill(BLACK)
            # draw all sprites
            self.all_sprites.draw(self.screen)


    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    

g = Game()
while g.running:
    g.new()

pg.quit()
