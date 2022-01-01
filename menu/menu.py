from menu.choice import GameChoice
from hud import HeadsUpDisplay as HUD

gameBoxWidth = 200
gameBoxHeight = 200
gameBoxPadding = 75

class Menu:
    def __init__(self, surface, win_w, win_h, games):
        self.gameName = 'menu'
        self.surface = surface
        self.windowWidth = win_w
        self.windowHeight = win_h
        self.hudHeight = self.windowHeight * (win_h * 2)
        self.playHeight = self.windowHeight - (self.windowHeight * (win_h * 2))
        self.gamesAvailable = games
        self.gamesAvailable.remove('menu')
        self.gamesChoices = self.wheresTheMelee(self.gamesAvailable)
        self.hud = HUD(surface, win_w, win_h, 'menu')
        
    def draw(self):
        # self.gamesChoices = self.wheresTheMelee(self.gamesAvailable)
        for g in self.gamesChoices:
            g.draw()
        
        self.hud.draw()

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





