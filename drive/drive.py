import pygame as pg
from drive.car import Car
from drive.dashboard import DashBoard
LEVELS = ['moon', 'mountains', 'space', 'plains', 'chill']

class Drive:
    def __init__(self, surface, win_w, win_h, md):
        global LEVELS
        self.surface = surface
        self.windowWidth = win_w
        self.windowHeight = win_h - (win_h * .2)
        self.md = md
        self.car = Car(self.surface, 200, win_h - (win_h * .2))
        self.dash = DashBoard(surface, win_w, win_h, md)
        self.car_group = pg.sprite.Group()
        self.car_group.add(self.car)
        self.background = pg.image.load(f'common/src/background/{LEVELS[3]}.png')
        self.scroll = 0

    def draw(self):
        self.surface.blit(self.background, (self.scroll, 0))
        self.scroll -= self.car.speed
        if self.scroll <= -640:
            self.scroll = 0
        self.dash.draw(self.md, int(self.car.fuel))
        self.car.draw()
        self.car_group.update()


