import pygame as pg
index = 0

class Paddle:
    def __init__(self, surface, x, y):
        global index
        self.i = index
        self.surface = surface
        self.x = x
        self.y = y
        self.width = 10
        self.height = 75
        self.score = 0
        self.color = (255,255,255)
        index += 1
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.rect = rect
        
        pg.draw.rect(self.surface, self.color, rect)

            