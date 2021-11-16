import pygame as pg
from pong.scoreboard import ScoreBoard as hud
from menu.choice import GameChoice
# from menu.hud import hud
gameBoxWidth = 200
gameBoxHeight = 200
gameBoxPadding = 75
AVAILABLE_GAMES = ['pong', 'breaker', '3', '4']

class Menu:
    def __init__(self, surface, win_w, win_h, md):
        self.surface = surface
        self.windowWidth = win_w
        self.windowHeight = win_h
        self.hudHeight = self.windowHeight * .2
        self.playHeight = self.windowHeight - (self.windowHeight * .2)
        self.gameOver = False
        self.hud = hud(self.surface, self.windowWidth, self.windowHeight, 'pong')
        self.metaData = md
        self.selectedGame = md.game
        self.gamesAvailable = self.wheresTheMelee()
        
    def play(self):
        while not self.gameOver:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.gameOver = True
                elif event.type == pg.MOUSEBUTTONUP:
                    for g in self.gamesAvailable:
                        if g.rect.collidepoint(event.pos[0],event.pos[1]):
                            self.selectedGame = g.name
                            print(self.selectedGame)

        # draw background
            pg.display.update()
            self.surface.fill((0,0,0))
        # draw game
            

            self.hud.draw()
            for games in self.gamesAvailable:
                games.draw()

        pg.quit()



    def wheresTheMelee(self):
        num = len(AVAILABLE_GAMES)
        res = []
        for gameName in AVAILABLE_GAMES:
            res.append(GameChoice(self.surface, self.windowWidth, self.windowHeight, gameName, num))

        print(res[0])
        return res





