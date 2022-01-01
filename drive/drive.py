import pygame as pg
from drive.car import Car
from drive.dashboard import DashBoard

class Drive:
    def __init__(self, surface, win_w, win_h, md):
        self.surface = surface
        self.windowWidth = win_w
        self.windowHeight = win_h - (win_h * .2)
        self.md = md
        self.car = Car(self.surface, 200, win_h - (win_h * .2))
        self.dash = DashBoard(surface, win_w, win_h, md)


    def draw(self):
        self.car.draw()
        self.dash.draw(self.md, self.car.fuel)


