import pygame as pg
index = 0

class Paddle:
    def __init__(self, surface, x):
        global index
        self.i = index
        self.surface = surface
        self.x = x
        self.y = 10
        self.width = 10
        self.height = 75
        self.score = 0
        self.color = (0,255,0)
        index += 1

    def draw(self):
        pg.draw.rect(self.surface, self.color, pg.Rect(self.x, self.y, self.width, self.height))
