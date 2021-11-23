from menu.choice import GameChoice

gameBoxWidth = 200
gameBoxHeight = 200
gameBoxPadding = 75
AVAILABLE_GAMES = ['pong', 'drive']

class Menu:
    def __init__(self, surface, win_w, win_h, hud_h):
        self.surface = surface
        self.windowWidth = win_w
        self.windowHeight = win_h
        self.hudHeight = self.windowHeight * hud_h
        self.playHeight = self.windowHeight - (self.windowHeight * hud_h)
        self.gamesAvailable = self.wheresTheMelee()
        
    def draw(self):
        for g in self.gamesAvailable:
            g.draw()

    def click(self, event):
        self.clickX = event.pos[0]
        self.clickY = event.pos[1]

        if event != 0:
            for g in self.gamesAvailable:
                if g.rect.collidepoint(self.clickX,self.clickY):
                    self.selectedGame = g.name
                    return self.selectedGame



    def wheresTheMelee(self):
        num = len(AVAILABLE_GAMES)
        res = []
        for gameName in AVAILABLE_GAMES:
            res.append(GameChoice(self.surface, self.windowWidth, self.windowHeight, gameName, num))

        return res





