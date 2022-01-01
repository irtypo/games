import pygame as pg
pg.font.init()

class HeadsUpDisplay:
    def __init__(self, surface, win_w, win_h, g):
        self.surface = surface
        self.windowWidth = win_w
        self.windowHeight = win_h
        self.width = win_w
        self.gameName = g
        self.maxHeight = self.windowHeight*.2
        self.top = self.windowHeight-self.maxHeight+1
        self.textLarge = pg.font.SysFont(None, 80)
        self.score_h_padding = self.windowWidth * .05

    def draw(self):
        # draw background
        pg.draw.rect(self.surface, (30,30,30), pg.Rect(0, self.top, self.width, self.maxHeight))
        pg.draw.line(self.surface, (255,255,255), (0,self.windowHeight-self.maxHeight), (self.windowWidth, self.windowHeight-self.maxHeight))
        
        # draw text
        self.titleText = self.textLarge.render('{}'.format(self.gameName), True, (255,255,255))
        
        titleTextX = self.windowWidth/2-self.titleText.get_width()/2
        titleTextY = self.top + self.maxHeight*.1
        self.surface.blit(self.titleText, (titleTextX, titleTextY))
        
        self.titleRect = self.titleText.get_rect()
        self.titleRect.x = titleTextX
        self.titleRect.y = titleTextY
    