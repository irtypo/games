import pygame as pg
from drive.car import Car


class Drive:
    def __init__(self, surface, win_w, play_h, md):
        self.surface = surface
        self.windowWidth = win_w
        self.windowHeight = play_h
        self.md = md
        self.car = Car(self.surface, 200, play_h)

    def draw(self, md):
        self.car.draw()


