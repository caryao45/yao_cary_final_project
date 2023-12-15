# This file was created by Cary Yao
# Sources: 


# Goals:

# content from kids can code: http://kidscancode.org/blog/
# got inspiration for game over from: https://www.youtube.com/watch?v=QuM-jEQ7fAA&ab_channel=CodingWithRuss 
# Got a little help from my dad
# import libraries and modules

# Design Goals:
# Make platformer game 
# Allow player to move and collect coins
# Make score go up when coin is collected
# Make hitpoints go down when collide with mobs
# Make player not fall off map
# Make game over screen once hitpoints zero or score is ten
# Make play again - figure out how to respawn coins (Kinda)
# Add timer to increase difficulty (Didn't do)

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

# need variable first
game_over = False

# this will always run
if game_over == False:
    class Game:
        def __init__(self): 
            # init pygame and create a window
            pg.init()
            pg.mixer.init()
            self.screen = pg.display.set_mode((WIDTH, HEIGHT))
            pg.display.set_caption("My Game...")
            self.clock = pg.time.Clock()
            self.running = True

        def new(self): 
            # create a group for all sprites
            self.score = 0
            self.all_sprites = pg.sprite.Group()
            self.all_platforms = pg.sprite.Group()
            self.all_hoops = pg.sprite.Group()
            self.all_balls = pg.sprite.Group()
            # instantiate classes
            self.player = Player(self)
            self.ball = Ball(self)
            # add instances to groups
            self.all_sprites.add(self.player)

            # prints platforms
            for p in PLATFORM_LIST:
                # instantiation of the Platform class
                plat = Platform(*p)
                self.all_sprites.add(plat)
                self.all_platforms.add(plat)

            for h in HOOP_PLACEMENT:
                # instantiation of the Hoop class
                hoop = Hoop(*h)
                self.all_sprites.add(hoop)
                self.all_hoops.add(hoop)

            for b in BALL_PLACEMENT:
                # instantiation of the Ball class
                ball = Ball(*b)
                self.all_sprites.add(ball)
                self.all_balls.add(ball)

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

            # this is what prevents the player from falling through the platform when falling down...
            if self.player.vel.y >= 0:
                hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
                if hits:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    self.player.vel.x = hits[0].speed*1.5

            # this is what prevents the ball from falling through the platform when falling down...
            if self.ball.vel.y >= 0:
                bhits = pg.sprite.spritecollide(self.ball, self.all_platforms, False)
                if bhits:
                    self.ball.pos.y = hits[0].rect.top
                    self.ball.vel.y = 0
                    self.ball.vel.x = hits[0].speed*1.5

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
            self.screen.fill(LIGHTBLUE)
            # draw all sprites
            self.all_sprites.draw(self.screen)
            # Displays score values
            self.draw_text("Score: " + str(self.player.score), 22, WHITE, 50, HEIGHT/10)
            # buffer - after drawing everything, flip display
            pg.display.flip()
            # Checks if score is ten; if ten, then prints you win text
            if self.player.score == 10:
                self.draw_text("You Win!", 22, WHITE, 360, 320)
                self.draw_text("Score: " + str(self.player.score), 22, WHITE, 360, 360)
                self.draw_text("Press R to Play Again!", 22, WHITE, 360, 400)
                pg.display.flip()


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
