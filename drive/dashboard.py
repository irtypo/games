from hud import HeadsUpDisplay

class DashBoard(HeadsUpDisplay):
    def __init__(self, surface, win_w, win_h, md):
        HeadsUpDisplay.__init__(self, surface, win_w, win_h, md)
    
    
    def draw(self, md, fuel):
        HeadsUpDisplay.draw(self, md)
        fuelText = self.textLarge.render('{}'.format(fuel), True, self.COLOR['WHITE'])
        self.surface.blit(fuelText, (self.score_h_padding, self.top + self.maxHeight*.45))
            