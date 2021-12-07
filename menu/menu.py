from menu.choice import GameChoice

gameBoxWidth = 200
gameBoxHeight = 200
gameBoxPadding = 75

class Menu:
    def __init__(self, surface, win_w, win_h, hud_h, md):
        self.surface = surface
        self.windowWidth = win_w
        self.windowHeight = win_h
        self.hudHeight = self.windowHeight * hud_h
        self.playHeight = self.windowHeight - (self.windowHeight * hud_h)
        self.md = md
        self.gamesAvailable = self.md.gameList
        self.gamesAvailable.remove('menu')
        self.gamesChoices = self.wheresTheMelee(self.gamesAvailable)
        
    def draw(self):
        # self.gamesChoices = self.wheresTheMelee(self.gamesAvailable)
        for g in self.gamesChoices:
            g.draw()

    def click(self, event):
        self.clickX = event.pos[0]
        self.clickY = event.pos[1]

        if event != 0:
            for g in self.gamesChoices:
                if g.rect.collidepoint(self.clickX,self.clickY):
                    self.selectedGame = g.name
                    return self.selectedGame


    def wheresTheMelee(self, gameList):
        num = len(gameList)
        res = []
        for gameName in gameList:
            res.append(GameChoice(self.surface, self.windowWidth, self.windowHeight, gameName, num))

        return res





