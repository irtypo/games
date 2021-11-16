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
        self.color = (255,255,255)
        index += 1

    def draw(self, event):

        if event == None:
            pg.draw.rect(self.surface, self.color, pg.Rect(self.x, self.y, self.width, self.height))
        elif event == 'goal':
            pg.draw.rect(self.surface, (0,255,0), pg.Rect(self.x, self.y, self.width, self.height))

            