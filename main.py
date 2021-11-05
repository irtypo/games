import pygame as pg
from pong.pong import Pong

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720 + (720 * .2)


pg.init()
wind = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pg.display.set_caption("ping")
game = Pong(wind, WINDOW_WIDTH, WINDOW_HEIGHT)
game.play()


