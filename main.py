import pygame as pg
from pygame.constants import K_ESCAPE
from menu.menu import Menu
from pong.pong import Pong
from drive.drive import Drive
from metadata import MetaData
from hud import HeadsUpDisplay as HUD
from pong.scoreboard import ScoreBoard

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720 + (720 * .2)
WINDOW_ICON = pg.image.load('common\src\\brain.png')
AVAILABLE_GAMES = ['menu', 'pong', 'drive', 'billards', '4']

metaData = MetaData()
mouseY = 10

def main():

    pg.init()
    pg.time.Clock()
    metaData.gameList = AVAILABLE_GAMES
    metaData.gameName = metaData.gameList[0]
    metaData.displayText = metaData.gameName

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

            if metaData.gameName == 'drive':
                driveControls(drive, event)

            elif metaData.gameName == 'pong':
                pongControls(pong, event)

            menuControls(menu, event)



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

def driveControls(drive, e):
    if e.type == pg.MOUSEBUTTONDOWN or (e.type == pg.KEYDOWN and e.key == pg.K_SPACE):
        drive.car.jumpStart()

    if e.type == pg.MOUSEBUTTONUP or (e.type == pg.KEYUP and e.key == pg.K_SPACE):
        drive.car.jumpStop()

def pongControls(pong, e):
    global mouseY
    if e.type == pg.MOUSEMOTION:
        if e.pos[1] != None:
            mouseY = e.pos[1]


def menuControls(menu, e):
    # close window
    if e.type == pg.QUIT:
        metaData.gameOver = True
        
    # go back to the menu
    if metaData.gameName != 'menu':
        if e.type == pg.KEYDOWN:
            if e.key == K_ESCAPE:
                metaData.gameName = 'menu'

    # ctrl + c
    if e.type == pg.KEYDOWN:
        if e.mod and pg.KMOD_LCTRL and e.key == pg.K_c:
            metaData.gameOver = True

    # select game
    if e.type == pg.MOUSEBUTTONUP:
        if metaData.gameName == 'menu' and menu.click(e) != None:
            metaData.gameName = menu.click(e)



if __name__=="__main__":
    main()


