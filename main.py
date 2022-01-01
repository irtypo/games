import pygame as pg
from pygame import surface
from menu.menu import Menu
from pong.pong import Pong
from drive.drive import Drive

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720 + (720 * .2)
WINDOW_ICON = pg.image.load('common/src/brain.png')
AVAILABLE_GAMES = ['menu', 'pong', 'drive', 'billards', '4']
GAME_LIST = {}
CURRENT_GAME = None
SURFACE = None
FPS = 60
mouseY = 10
GAME_OVER = False


def main():
    global GAME_LIST
    global CURRENT_GAME
    global SURFACE

    pg.init()
    pg.time.Clock()
    clock = pg.time.Clock()
    SURFACE = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pg.display.set_icon(WINDOW_ICON)

    GAME_LIST = {
        'menu': Menu(SURFACE, WINDOW_WIDTH, WINDOW_HEIGHT, AVAILABLE_GAMES),
        'pong': Pong(SURFACE, WINDOW_WIDTH, WINDOW_HEIGHT),
        'drive': Drive(SURFACE, WINDOW_WIDTH, WINDOW_HEIGHT)
    }
    CURRENT_GAME = GAME_LIST['menu']

    while not GAME_OVER:
        clock.tick(FPS)

        # event
        for event in pg.event.get():
            pollInput(event)

        # draw
        pg.display.update()
        SURFACE.fill((0,0,0))
        if CURRENT_GAME.gameName == 'menu':
            pg.mouse.set_visible(True)
            GAME_LIST['menu'].draw()

        elif CURRENT_GAME.gameName == 'pong':
            GAME_LIST['pong'].draw(mouseY)
        
        elif CURRENT_GAME.gameName == 'drive':
            GAME_LIST['drive'].draw()

        
    pg.quit()


def pollInput(e):
    global GAME_LIST
    global CURRENT_GAME
    global GAME_OVER

    ## GLOBAL CONTROLS ##
    # close window
    if e.type == pg.QUIT:
        GAME_OVER = True
        
    # go back to the menu
    if CURRENT_GAME.gameName != 'menu':
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_ESCAPE:
                CURRENT_GAME = GAME_LIST['menu']

    # ctrl + c
    if e.type == pg.KEYDOWN:
        if e.mod and pg.KMOD_LCTRL and e.key == pg.K_c:
            GAME_OVER = True

    # select game
    if e.type == pg.MOUSEBUTTONUP:
        clicked = GAME_LIST['menu'].click(e)
        if CURRENT_GAME.gameName == 'menu' and clicked:
            try:
                CURRENT_GAME = GAME_LIST[clicked]
            except:
                pass

    ## PONG CONTROLS ##
    if CURRENT_GAME.gameName == 'pong':
        global mouseY
        if e.type == pg.MOUSEMOTION:
            if e.pos[1] != None:
                mouseY = e.pos[1]


    ## DRIVE CONTROLS ##
    elif CURRENT_GAME.gameName == 'drive':

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

        # restart
        if e.type == pg.KEYDOWN and e.key == pg.K_r:
            GAME_LIST['drive'] = Drive(SURFACE, WINDOW_WIDTH, WINDOW_HEIGHT)


        # click on HUD
        if (e.type == pg.MOUSEBUTTONDOWN and e.button == 2) and e.pos[1] > GAME_LIST['drive'].dash.top:
            if GAME_LIST['drive'].dash.titleRect.collidepoint(e.pos[0],e.pos[1]):
                GAME_LIST['drive'].toggleDebugMode()

if __name__=="__main__":
    main()


