import pygame as pg

pg.font.init()
textLarge = pg.font.SysFont(None, 80)
textSmall = pg.font.SysFont(None, 24)


class HeadsUpDisplay:
    def __init__(self, surface, win_w, win_h, game):
        self.windowHeight = win_h
        self.windowWidth = win_w
        self.maxHeight = self.heightFromGame(game)
        self.width = win_w
        self.score_h_padding = self.windowWidth * .025
        self.top = self.windowHeight-self.maxHeight+1
        self.surface = surface

    def draw(self, p1Score, p2Score):
        pg.draw.rect(self.surface, (30,30,30), pg.Rect(0, self.top, self.width, self.maxHeight))
        pg.draw.line(self.surface, (255,255,255), (0,self.windowHeight-self.maxHeight), (self.windowWidth, self.windowHeight-self.maxHeight))
        
        p1ScoreText = textLarge.render('{}'.format(p1Score), True, (255,255,255))
        p2ScoreText = textLarge.render('{}'.format(p2Score), True, (255,255,255))
        self.surface.blit(p1ScoreText, (self.score_h_padding, self.top + self.maxHeight*.1))
        self.surface.blit(p2ScoreText, (self.windowWidth - self.score_h_padding - p2ScoreText.get_width(), self.top + self.maxHeight*.1))

    def heightFromGame(self, game):
        if game == 'pong':
            return self.windowHeight*.2