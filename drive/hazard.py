import pygame as pg

class Hazard(pg.sprite.Sprite):
    def __init__(self, surface, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.surface = surface
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pg.draw.rect(self.surface, self.color, self.rect)

