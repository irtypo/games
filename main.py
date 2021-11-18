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
    AVAILABLE_GAMES = ['menu', 'pong', 'breaker', 'drive', '4']

    pg.init()
    metaData = MetaData()
    metaData.gameName = AVAILABLE_GAMES[0]
    metaData.displayText = metaData.gameName
    mouseY = 10

    surface = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pg.display.set_caption("ping")
    pg.display.set_icon(WINDOW_ICON)
    hud = HUD(surface, WINDOW_WIDTH, WINDOW_HEIGHT, metaData)
    menu = Menu(surface, WINDOW_WIDTH, WINDOW_HEIGHT, hud.maxHeight)

    while not metaData.gameOver:

        # events
        for event in pg.event.get():
            # close window
            if event.type == pg.QUIT:
                metaData.gameOver = True
            # ctrl + c
            elif event.type == pg.KEYDOWN:
                if event.mod == 4160 and event.key == 99:
                    metaData.gameOver = True
            
            elif metaData.gameName == 'menu':
                if event.type == pg.MOUSEBUTTONUP and menu.click(event) != None:
                    metaData.gameName = menu.click(event)
            elif metaData.gameName == 'pong':
                if event.type == pg.MOUSEMOTION:
                    if event.pos[1] != None:
                        mouseY = event.pos[1]

        # drawing
        pg.display.update()
        surface.fill((0,0,0))
        if metaData.gameName == 'menu':
            menu.draw()
        elif metaData.gameName == 'pong':
            pong = Pong(surface, WINDOW_WIDTH, WINDOW_HEIGHT-hud.maxHeight)
            pong.draw(mouseY)
        elif metaData.gameName == 'breaker':
            pass
        elif metaData.gameName == 'drive':
            pass

        hud.draw()
    pg.quit()


if __name__=="__main__":
    main()
