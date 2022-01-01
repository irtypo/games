import pygame as pg
from pygame.constants import K_ESCAPE
from menu.menu import Menu
from pong.pong import Pong
from drive.drive import Drive
from metadata import MetaData
from hud import HeadsUpDisplay as HUD
from pong.scoreboard import ScoreBoard



def main():
    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 720 + (720 * .2)
    WINDOW_ICON = pg.image.load('common\src\\brain.png')
    AVAILABLE_GAMES = ['menu', 'pong', 'drive', 'billards', '4']

    pg.init()
    pg.time.Clock()
    metaData = MetaData()
    metaData.gameList = AVAILABLE_GAMES
    metaData.gameName = metaData.gameList[0]
    metaData.displayText = metaData.gameName
    mouseY = 10

    surface = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pg.display.set_caption("ping")
    pg.display.set_icon(WINDOW_ICON)
    hud = HUD(surface, WINDOW_WIDTH, WINDOW_HEIGHT, metaData)
    sb = ScoreBoard(surface, WINDOW_WIDTH, WINDOW_HEIGHT, metaData)
    menu = Menu(surface, WINDOW_WIDTH, WINDOW_HEIGHT, hud.maxHeight, metaData)
    pong = Pong(surface, WINDOW_WIDTH, WINDOW_HEIGHT-hud.maxHeight, metaData)
    drive = Drive(surface, WINDOW_WIDTH, WINDOW_HEIGHT-hud.maxHeight, metaData)

    while not metaData.gameOver:

        # events
        for event in pg.event.get():
            # if event == "down":
            # print(event)

            
            # close window
            if event.type == pg.QUIT:
                metaData.gameOver = True
            # ctrl + c
            elif event.type == pg.KEYDOWN:
                if event.mod == 4160 and event.key == 99:
                    metaData.gameOver = True

                # go back to the menu
                if metaData.gameName != 'menu':
                    if event.type == pg.KEYDOWN:
                        if event.key == K_ESCAPE:
                            metaData.gameName = 'menu'

                if metaData.gameName == 'drive':
                    if event.key == pg.K_SPACE:
                        drive.car.jumpStart()
                        

            elif event.type == pg.MOUSEBUTTONUP:
                if metaData.gameName == 'menu' and menu.click(event) != None:
                    metaData.gameName = menu.click(event)


            elif event.type == pg.MOUSEMOTION:
                if metaData.gameName == 'pong':
                    if event.pos[1] != None:
                        mouseY = event.pos[1]


            elif event.type == pg.KEYUP:
                if metaData.gameName == 'drive':
                    if event.key == pg.K_SPACE:
                        drive.car.jumpStop()
        # drawing
        pg.display.update()
        surface.fill((0,0,0))
        if metaData.gameName == 'menu':
            pg.mouse.set_visible(True)
            menu.draw()
            hud.draw(metaData)
        elif metaData.gameName == 'pong':
            if mouseY > WINDOW_HEIGHT-hud.maxHeight:
                pg.mouse.set_visible(True)
            else:
                pg.mouse.set_visible(False)

            pong.draw(mouseY, metaData)
            sb.draw(metaData)
        # elif metaData.gameName == 'breaker':
            # pass
        elif metaData.gameName == 'drive':
            drive.draw(metaData)
            hud.draw(metaData)

    pg.quit()


if __name__=="__main__":
    main()
