import pygame as pg
import random

class Hazard(pg.sprite.Sprite):
    def __init__(self, surface, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.surface = surface
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)


    def scroll(self, speed):
        self.x -= speed
        self.rect.x = self.x

    def draw(self):
        
        # hazard
        pg.draw.rect(self.surface, self.color, self.rect)
        
        # hazard border
        for i in range(4):
            pg.draw.rect(self.surface, (0,0,0), (self.x-i, self.y-i, self.width, self.height), 1)
