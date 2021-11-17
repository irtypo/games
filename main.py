import pygame as pg
from pygame import display
from pong.pong import Pong
from menu.menu import Menu
from metadata import MetaData
from hud import HeadsUpDisplay as HUD



def main():
    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 720 + (720 * .2)
    WINDOW_ICON = pg.image.load('common\src\\brain.png')
    AVAILABLE_GAMES = ['menu', 'pong', 'breaker', '3', '4']

    pg.init()
    clickEvent = 0
    metaData = MetaData()
    metaData.gameName = AVAILABLE_GAMES[0]
    displayText = None  

    surface = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pg.display.set_caption("ping")
    pg.display.set_icon(WINDOW_ICON)
    hud = HUD(surface, WINDOW_WIDTH, WINDOW_HEIGHT, metaData)
    menu = Menu(surface, WINDOW_WIDTH, WINDOW_HEIGHT, hud.maxHeight)
    pong = Pong(surface, WINDOW_WIDTH, WINDOW_HEIGHT-hud.maxHeight)
    gameOver = False

    while not gameOver:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameOver = True
            elif event.type == pg.MOUSEBUTTONUP:
                if metaData.gameName == 'menu' and menu.click(event) != None:
                    metaData.gameName = menu.click(event)
            # elif event.type == pg.MOUSEMOTION:
                # if metaData.gameName == 'pong':
                    # pong.players[0].y = event.pos[1]
                # self.players[0].y = event.pos[1]



        pg.display.update()
        surface.fill((0,0,0))
        
        hud.draw(metaData)

        if metaData.gameName == 'menu':
            menu.draw()
        else:
            displayText = metaData.gameName
            # print(metaData.gameName)


        # if metaData.gameName == 'pong':
        #     pong.draw()
        # if metaData.gameName == 'breaker':
        #     breaker.draw()

        
    pg.quit()

if __name__=="__main__":
    main()