import pygame as pg

pg.font.init()
textLarge = pg.font.SysFont(None, 80)
textSmall = pg.font.SysFont(None, 24)


class HeadsUpDisplay:
    def __init__(self, surface, win_w, win_h, md):
        self.surface = surface
        self.windowWidth = win_w
        self.windowHeight = win_h
        self.metaData = md
        self.width = win_w
        self.gameBasedConfig()
        self.displayText = 'mad'

    def draw(self, md):
        self.metaData = md
        pg.draw.rect(self.surface, (30,30,30), pg.Rect(0, self.top, self.width, self.maxHeight))
        pg.draw.line(self.surface, (255,255,255), (0,self.windowHeight-self.maxHeight), (self.windowWidth, self.windowHeight-self.maxHeight))
        
        # if event == 'goal':
            # color = (0,255,0)
        # else:
        color = (255,255,255)


        who = textLarge.render('{}'.format(self.displayText), True, color)
        self.surface.blit(who, (self.windowWidth/2-who.get_width(), self.top + self.maxHeight*.1))
        # if self.p1Score or self.p2Score != None:
        #     p1ScoreText = textLarge.render('{}'.format(self.p1Score), True, color)
        #     p2ScoreText = textLarge.render('{}'.format(self.p2Score), True, color)
        #     self.surface.blit(p1ScoreText, (self.score_h_padding, self.top + self.maxHeight*.1))
        #     self.surface.blit(p2ScoreText, (self.windowWidth - self.score_h_padding - p2ScoreText.get_width(), self.top + self.maxHeight*.1))

    def gameBasedConfig(self):
        # print('----------------',self.metaData.gameName)
        wat = 'menu'
        if wat == 'menu':
            self.maxHeight = self.windowHeight*.2
            self.score_h_padding = self.windowWidth * .05
            self.top = self.windowHeight-self.maxHeight+1
            self.p1Score = None
            self.p2Score = None
        if wat == 'pong':
            self.maxHeight = self.windowHeight*.2
            self.score_h_padding = self.windowWidth * .05
            self.top = self.windowHeight-self.maxHeight+1
            self.p1Score = 0
            self.p2Score = 0

