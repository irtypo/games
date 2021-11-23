import pygame as pg

pg.font.init()
COLOR = {'WHITE': (255,255,255), 'BLACK': (0,0,0)}
textLarge = pg.font.SysFont(None, 80)
textSmall = pg.font.SysFont(None, 24)


class HeadsUpDisplay:
    def __init__(self, surface, win_w, win_h, md):
        self.surface = surface
        self.windowWidth = win_w
        self.windowHeight = win_h
        self.metaData = md
        self.width = win_w
        self.curGame = 'menu'
        self.gameBasedConfig()


    def draw(self, md):
        # update when game changes
        self.metaData = md
        self.p1Score = self.metaData.p1Score
        self.p2Score = self.metaData.p2Score
        if self.curGame != self.metaData.gameName:
            self.curGame = self.metaData.gameName
            self.gameBasedConfig()

        # draw background
        pg.draw.rect(self.surface, (30,30,30), pg.Rect(0, self.top, self.width, self.maxHeight))
        pg.draw.line(self.surface, (255,255,255), (0,self.windowHeight-self.maxHeight), (self.windowWidth, self.windowHeight-self.maxHeight))
        
        # draw text
        displayText = textLarge.render('{}'.format(self.metaData.gameName), True, COLOR['WHITE'])
        self.surface.blit(displayText, (self.windowWidth/2-displayText.get_width()/2, self.top + self.maxHeight*.1))
        
        # draw score
        if self.p1Score or self.p2Score != None:
            p1ScoreText = textLarge.render('{}'.format(self.p1Score), True, COLOR['WHITE'])
            p2ScoreText = textLarge.render('{}'.format(self.p2Score), True, COLOR['WHITE'])
            self.surface.blit(p1ScoreText, (self.score_h_padding, self.top + self.maxHeight*.1))
            self.surface.blit(p2ScoreText, (self.windowWidth - self.score_h_padding - p2ScoreText.get_width(), self.top + self.maxHeight*.1))

        
    def gameBasedConfig(self):
        if self.curGame == 'menu':
            self.maxHeight = self.windowHeight*.2
            self.score_h_padding = self.windowWidth * .05
            self.top = self.windowHeight-self.maxHeight+1
            self.p1Score = None
            self.p2Score = None
        elif self.curGame == 'pong':
            self.maxHeight = self.windowHeight*.2
            self.score_h_padding = self.windowWidth * .05
            self.top = self.windowHeight-self.maxHeight+1
            self.p1Score = self.metaData.p1Score
            self.p2Score = self.metaData.p2Score
        

