from hud import HeadsUpDisplay

class ScoreBoard(HeadsUpDisplay):
    def __init__(self, surface, win_w, win_h, g):
        HeadsUpDisplay.__init__(self, surface, win_w, win_h, g)
        self.p1Score = 0
        self.p2Score = 0


    def draw(self):
        HeadsUpDisplay.draw(self)

        # draw score
        p1ScoreText = self.textLarge.render('{}'.format(self.p1Score), True, (255,255,255))
        self.surface.blit(p1ScoreText, (self.score_h_padding, self.top + self.maxHeight*.1))

        p2ScoreText = self.textLarge.render('{}'.format(self.p2Score), True, (255,255,255))
        self.surface.blit(p2ScoreText, (self.windowWidth - self.score_h_padding - p2ScoreText.get_width(), self.top + self.maxHeight*.1))

    def goal(self, player):
        if player == 'p1':
            self.p1Score += 1
        else:
            self.p2Score += 1