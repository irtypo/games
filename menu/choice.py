import pygame as pg
import random
pg.font.init()

index = 0
COLORS = [(255,0,0), (0,255,0), (0,255,255), (255,0,255), (0,255 ,0), (30, 30, 30)]
textSize = pg.font.SysFont(None, 60)


class GameChoice:
    global index
    def __init__(self, surface, win_w, win_h, name, maxNum):
        self.surface = surface
        self.windowWidth = win_w
        self.windowHeight = win_h
        self.columnWidth = self.windowWidth//maxNum
        self.name = name
        self.color = random.choice(COLORS)
        self.displayText = textSize.render('{}'.format(self.name), True, (255,255,255))
        self.width = self.displayText.get_width() + (self.displayText.get_width()//2) 
        self.height = 100
        self.xOffset = self.columnWidth/8
        self.index = index
        self.left = ((self.index+1) * self.columnWidth) - self.columnWidth//2
        self.top = (win_h/2 - self.height)
        self.rect = pg.Rect(self.left, self.top, self.width, self.height)
        self.count()


    def draw(self):
        pg.draw.rect(self.surface, self.color, self.rect)
        self.surface.blit(self.displayText, (self.left+self.width//6, self.top+10+(self.displayText.get_height()//2)))
        
    def count(self):
        global index
        index += 1