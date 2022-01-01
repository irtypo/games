from hud import HeadsUpDisplay

class DashBoard(HeadsUpDisplay):
    def __init__(self, surface, win_w, win_h, g):
        HeadsUpDisplay.__init__(self, surface, win_w, win_h, g)
        self.p1Score = 0
    
    
    def draw(self, car):
        HeadsUpDisplay.draw(self)
            
        # draw score
        p1ScoreText = self.textLarge.render('{}'.format(self.p1Score), True, (255,255,255))
        self.surface.blit(p1ScoreText, (self.score_h_padding, self.top + self.maxHeight*.1))

        # draw fuel
        fuelText = self.textLarge.render('{}'.format(int(car.fuel)), True, (255,255,255))
        self.surface.blit(fuelText, (self.score_h_padding, self.top + self.maxHeight*.45))



    def scored(self, points):
        self.p1Score += points