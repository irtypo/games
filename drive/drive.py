import random
import pygame as pg
from drive.car import Car
from drive.dashboard import DashBoard
from drive.hazard import Hazard
LEVELS = ['moon', 'mountains', 'space', 'plains', 'chill']
DEBUG_MODE = False

class Drive:
    def __init__(self, surface, win_w, win_h):
        global LEVELS
        self.gameName = 'drive'
        self.surface = surface
        self.windowWidth = win_w
        self.windowHeight = win_h - (win_h * .2)
        self.car = Car(self.surface, 200, win_h - (win_h * .2))
        self.dash = DashBoard(surface, win_w, win_h, 'drive')
        self.car_group = pg.sprite.Group()
        self.car_group.add(self.car)
        self.background = pg.image.load(f'common/src/background/{LEVELS[3]}.png')
        self.scrolledDist = 0
        self.hazards = []
        for i in range(1, 2):
            height = random.randint(20, 300)
            haz = Hazard(self.surface, 700 * i, self.windowHeight-height, 50, height)
            self.hazards.append(haz)

    def draw(self):
        # draw background
        self.surface.blit(self.background, (self.scrolledDist, 0))
        self.scrolledDist -= self.car.speed
        if self.scrolledDist <= -640:
            self.scrolledDist = 0

        # draw hud
        self.dash.draw(self.car)

        # draw hitboxes
        if DEBUG_MODE:
            pg.draw.rect(self.surface, (0, 255, 0), self.car.rect)
    
        # draw car
        self.car.draw()
        self.car_group.update()

        # draw hazard
        for i in range(0, len(self.hazards)):
            if self.hazards[i].rect.x > 0-self.hazards[i].rect.width:
                self.hazards[i].scroll(self.car.speed)
            self.hazards[i].draw()

        # collision check
        for i in range(0, len(self.hazards)):
            if self.car.rect.colliderect(self.hazards[i].rect):
                self.car.speed = 0


        # score check
        for i in range(0, len(self.hazards)):
            # print(self.hazards[i].x)
            if self.hazards[i].x < self.car.x:
                self.dash.scored(50)
                # print('scored')

    def toggleDebugMode(self):
        global DEBUG_MODE
        DEBUG_MODE = True if DEBUG_MODE == False else False
        