import pygame as pg
from pygame.constants import K_ESCAPE
from menu.menu import Menu
from pong.pong import Pong
from drive.drive import Drive
from metadata import MetaData

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
    menu = Menu(surface, WINDOW_WIDTH, WINDOW_HEIGHT, metaData)
    pong = Pong(surface, WINDOW_WIDTH, WINDOW_HEIGHT, metaData)
    drive = Drive(surface, WINDOW_WIDTH, WINDOW_HEIGHT, metaData)

    while not metaData.gameOver:

        # events
        for event in pg.event.get():
            
            menuControls(menu, event)
            if metaData.gameName == 'drive':
                driveControls(drive, event)
            elif metaData.gameName == 'pong':
                pongControls(pong, event)


        # drawing
        pg.display.update()
        surface.fill((0,0,0))
        if metaData.gameName == 'menu':
            pg.mouse.set_visible(True)
            menu.draw()
        elif metaData.gameName == 'pong':
            pong.draw(mouseY, metaData)
        elif metaData.gameName == 'drive':
            drive.draw()
    pg.quit()



def driveControls(drive, e):
    # press jump
    if e.type == pg.MOUSEBUTTONDOWN or (e.type == pg.KEYDOWN and e.key == pg.K_SPACE):
        
        if not drive.car.grounded:
            drive.car.hover()
            # drive.car.hovering = True
        else:
            drive.car.jumpStart()
            # drive.car.hovering = False

    # release jump
    if e.type == pg.MOUSEBUTTONUP or (e.type == pg.KEYUP and e.key == pg.K_SPACE):
        drive.car.jumpStop()

    if e.type == pg.KEYDOWN and e.key == pg.K_r:
        drive.car.refuel(1000)


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


