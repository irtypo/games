import pygame as pg
from pygame.constants import GL_BLUE_SIZE, K_ESCAPE
from menu.menu import Menu
from pong.pong import Pong
from drive.drive import Drive
from metadata import MetaData

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720 + (720 * .2)
WINDOW_ICON = pg.image.load('common/src/brain.png')
AVAILABLE_GAMES = ['menu', 'pong', 'drive', 'billards', '4']
GAME_LIST = {}
CURRENT_GAME = None
FPS = 60
metaData = MetaData()
mouseY = 10


def main():
    global GAME_LIST
    global CURRENT_GAME

    pg.init()
    pg.time.Clock()
    metaData.gameList = AVAILABLE_GAMES
    metaData.gameName = metaData.gameList[0]
    metaData.displayText = metaData.gameName

    surface = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pg.display.set_icon(WINDOW_ICON)
    GAME_LIST = {
        'menu': Menu(surface, WINDOW_WIDTH, WINDOW_HEIGHT, metaData),
        'pong': Pong(surface, WINDOW_WIDTH, WINDOW_HEIGHT, metaData),
        'drive': Drive(surface, WINDOW_WIDTH, WINDOW_HEIGHT, metaData)
    }
    CURRENT_GAME = GAME_LIST['menu']

    clock = pg.time.Clock()

    while not metaData.gameOver:
        clock.tick(FPS)

        # event
        for event in pg.event.get():
            pollInput(event)

        # draw
        pg.display.update()
        surface.fill((0,0,0))
        if metaData.gameName == 'menu':
            pg.mouse.set_visible(True)
            GAME_LIST['menu'].draw()
        elif metaData.gameName == 'pong':
            GAME_LIST['pong'].draw(mouseY, metaData)
        elif metaData.gameName == 'drive':
            GAME_LIST['drive'].draw()

        
    pg.quit()


def pollInput(e):
    global GAME_LIST
    global CURRENT_GAME

    ## GLOBAL CONTROLS ##
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
        if metaData.gameName == 'menu' and GAME_LIST['menu'].click(e) != None:
            metaData.gameName = GAME_LIST['menu'].click(e)




    ## PONG CONTROLS ##
    if metaData.gameName == 'pong':
        CURRENT_GAME = GAME_LIST['pong']
        global mouseY
        if e.type == pg.MOUSEMOTION:
            if e.pos[1] != None:
                mouseY = e.pos[1]


    ## DRIVE CONTROLS ##
    elif metaData.gameName == 'drive':
        CURRENT_GAME = GAME_LIST['drive']

       

        # press jump
        if (e.type == pg.MOUSEBUTTONDOWN and e.button == 1) or (e.type == pg.KEYDOWN and e.key == pg.K_SPACE):
            if not GAME_LIST['drive'].car.grounded:
                GAME_LIST['drive'].car.hover()
            else:
                GAME_LIST['drive'].car.jumpStart()
        
        # fly
        elif (e.type == pg.MOUSEBUTTONDOWN and e.button == 3) or (e.type == pg.KEYDOWN and e.key == pg.K_x):
            GAME_LIST['drive'].car.fly()
            GAME_LIST['drive'].car.jumpStart()


        # release jump/fly
        if e.type == pg.MOUSEBUTTONUP or (e.type == pg.KEYUP and e.key == pg.K_SPACE):
            GAME_LIST['drive'].car.jumpStop()
            # drive.car.flyStop()

        # fuel
        if e.type == pg.KEYDOWN and e.key == pg.K_f:
            GAME_LIST['drive'].car.addFuel(1000)

        # click on HUD
        if (e.type == pg.MOUSEBUTTONDOWN and e.button == 2) and e.pos[1] > GAME_LIST['drive'].dash.top:
            if GAME_LIST['drive'].dash.titleRect.collidepoint(e.pos[0],e.pos[1]):
                GAME_LIST['drive'].toggleDebugMode()

if __name__=="__main__":
    main()


