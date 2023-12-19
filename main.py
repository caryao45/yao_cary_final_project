# This file was created by Cary Yao
# Sources: 
# My old mygame code

# Goals:
# Make hoop and ball with all the proper attributes
# Make ball follow player when touched
# Make ball go in shooting motion after released from player
# If ball goes in net, add to score
# Add second player and hoop for multiplayer

import pygame as pg
from pygame.sprite import Sprite
from random import randint
import os
from settings import *
from sprites import *
import math

vec = pg.math.Vector2

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

# this will always run
class Game:
    def __init__(self): 
        # init pygame and create a window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Basketball Game")
        self.clock = pg.time.Clock()
        self.running = True

    def new(self): 
        # score value
        self.score = 0

        # create a group for all sprites
        self.all_sprites = pg.sprite.Group()
        self.all_hoops = pg.sprite.Group()

        # instantiate classes
        self.player = Player()
        self.ball = Ball()
        self.hoop = Hoop()

        # add instances to groups
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.ball)
        self.all_sprites.add(self.hoop)
        self.all_hoops.add(self.hoop)
      
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

        # Check for collision between ball and hoop, adds to score and resets ball position
        if pg.sprite.spritecollide(self.ball, self.all_hoops, False):
            self.player.score += 1
            self.ball.rect.center = (WIDTH // 2, 400)
            if self.player.score > 10:
                self.player.score = 10

    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            # got help from dad
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self.ball.rect.center = self.player.rect.center

    def draw(self):
        ############ Draw ################
        # draw the background screen
        self.screen.fill(LIGHTBLUE)
        # draw all sprites
        self.all_sprites.draw(self.screen)
        # Displays score values
        self.draw_text("Score: " + str(self.player.score), 22, WHITE, 50, 550)
        # buffer - after drawing everything, flip display
        pg.display.flip()
        # Checks if score is ten; if ten, then prints you win text
        if self.player.score >= 10:
            self.draw_text("You Win!", 22, WHITE, 400, 320)
            self.draw_text("Score: " + str(self.player.score), 22, WHITE, 400, 360)
            pg.display.flip()

    # draw text function
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass


g = Game()
while g.running:
    g.new()


pg.quit()
