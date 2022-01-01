import pygame as pg

pg.font.init()


class HeadsUpDisplay:
    def __init__(self, surface, win_w, win_h, md):
        self.surface = surface
        self.windowWidth = win_w
        self.windowHeight = win_h
        self.metaData = md
        self.width = win_w
        self.maxHeight = self.windowHeight*.2
        self.score_h_padding = self.windowWidth * .05
        self.top = self.windowHeight-self.maxHeight+1
        self.p1Score = self.metaData.p1Score
        self.p2Score = self.metaData.p2Score
        self.textLarge = pg.font.SysFont(None, 80)
        self.COLOR = {'WHITE': (255,255,255), 'BLACK': (0,0,0)}

    def draw(self, md):
        # update when game changes
        self.metaData = md
        self.p1Score = self.metaData.p1Score
        self.p2Score = self.metaData.p2Score

        # draw background
        pg.draw.rect(self.surface, (30,30,30), pg.Rect(0, self.top, self.width, self.maxHeight))
        pg.draw.line(self.surface, (255,255,255), (0,self.windowHeight-self.maxHeight), (self.windowWidth, self.windowHeight-self.maxHeight))
        
        # draw text
        self.titleText = self.textLarge.render('{}'.format(self.metaData.gameName), True, self.COLOR['WHITE'])
        
        titleTextX = self.windowWidth/2-self.titleText.get_width()/2
        titleTextY = self.top + self.maxHeight*.1
        self.surface.blit(self.titleText, (titleTextX, titleTextY))
        
        self.titleRect = self.titleText.get_rect()
        self.titleRect.x = titleTextX
        self.titleRect.y = titleTextY
        
        # draw score
        if self.metaData.gameName != 'menu':
            p1ScoreText = self.textLarge.render('{}'.format(self.p1Score), True, self.COLOR['WHITE'])
            self.surface.blit(p1ScoreText, (self.score_h_padding, self.top + self.maxHeight*.1))
            if self.metaData.gameName != 'drive':
                p2ScoreText = self.textLarge.render('{}'.format(self.p2Score), True, self.COLOR['WHITE'])
                self.surface.blit(p2ScoreText, (self.windowWidth - self.score_h_padding - p2ScoreText.get_width(), self.top + self.maxHeight*.1))


