import pygame as pg
from pong.pong import Pong
from menu.menu import Menu
from metadata import MetaData

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720 + (720 * .2)
WINDOW_ICON = pg.image.load('common\src\\brain.png')


pg.init()
metaData = MetaData()
wind = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pg.display.set_caption("ping")
pg.display.set_icon(WINDOW_ICON)

game = Menu(wind, WINDOW_WIDTH, WINDOW_HEIGHT, metaData)
game.play()

print(metaData.game)

# game = Pong(wind, WINDOW_WIDTH, WINDOW_HEIGHT)