import pygame as pg
import random

index = 0
COLORS = [(255,0,0), (0,255,0), (0,255,255), (255,0,255), (0,255 ,0), (30, 30, 30)]


class GameChoice:
    global index
    def __init__(self, surface, win_w, win_h, name, maxNum):
        self.surface = surface
        self.windowWidth = win_w
        self.windowHeight = win_h
        self.maxNumChoices = maxNum
        self.name = name
        self.color = random.choice(COLORS)
        self.img = None
        self.text = None
        self.width = 200
        self.height = 100
        self.padding = 75
        self.index = index
        self.left = self.padding + self.width * self.index * 1.5
        self.top = (win_h/2 - self.height)
        self.rect = pg.Rect(self.left+300, self.top, self.width, self.height)
        self.count()

    def draw(self):
        pg.draw.rect(self.surface, self.color, self.rect)

    def count(self):
        global index
        index += 1