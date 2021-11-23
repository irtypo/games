import pygame as pg
from hud import HeadsUpDisplay

pg.font.init()
textLarge = pg.font.SysFont(None, 80)
textSmall = pg.font.SysFont(None, 24)
COLOR = {'WHITE': (255,255,255), 'BLACK': (0,0,0)}


class ScoreBoard(HeadsUpDisplay):

    
    def draw(self, md):
#         pg.draw.rect(self.surface, (30,30,30), pg.Rect(0, self.top, self.width, self.maxHeight))
#         pg.draw.line(self.surface, (255,255,255), (0,self.windowHeight-self.maxHeight), (self.windowWidth, self.windowHeight-self.maxHeight))
        
#         # if event == 'goal':
#             # color = (0,255,0)
#         # else:
#         color = (255,255,255)

#  # draw text
#         displayText = textLarge.render('{}'.format(self.metaData.gameName), True, COLOR['WHITE'])
#         self.surface.blit(displayText, (self.windowWidth/2-displayText.get_width()/2, self.top + self.maxHeight*.1))

        HeadsUpDisplay.p1Score = md.p1Score    
        HeadsUpDisplay.p2Score = md.p2Score   
        # print('wat1: ', HeadsUpDisplay.p2Score) 
        HeadsUpDisplay.draw(self, md)

        # p1ScoreText = textLarge.render('{}'.format(p1Score), True, color)
        # p2ScoreText = textLarge.render('{}'.format(p2Score), True, color)
        # self.surface.blit(p1ScoreText, (self.score_h_padding, self.top + self.maxHeight*.1))
        # self.surface.blit(p2ScoreText, (self.windowWidth - self.score_h_padding - p2ScoreText.get_width(), self.top + self.maxHeight*.1))
