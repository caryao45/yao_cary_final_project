from typing import Any
import pygame as pg
from pygame.sprite import Sprite
from random import randint
import math

from pygame.math import Vector2 as vec
import os
from settings import *

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

# player class
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, 'theBigBell.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, 400)
        self.score = 0
        self.speed = 5
    # defines controls for player
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.rect.x -= 5
        if keys[pg.K_d]:
            self.rect.x += 5
    def update(self):
        self.controls()
        if self.rect.left < 0:
            self.pos.x = WIDTH - self.rect.right
        if self.rect.right > WIDTH:
            self.pos.x = WIDTH - self.rect.left
        

# hoop class
class Hoop(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, 'basketball_hoop.jpg')).convert()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2 , 100)
        self.speed = 5
        self.direction = 1
    def update(self):
        # basket's continous movement
        self.rect.x += self.speed 
        # change direction when hitting the screen edge
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.speed = -self.speed

# ball class
class Ball(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, 'basketball.jpg')).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, 400)
        self.speed = 5
    def update(self):
        # Move basketball up when shooting
        if self.rect.y > 0:
            self.rect.y -= self.speed