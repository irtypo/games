import random
import pygame as pg
from drive.car import Car
from drive.dashboard import DashBoard
from drive.hazard import Hazard
LEVELS = ['moon', 'mountains', 'space', 'plains', 'chill']
DEBUG_MODE = False
HAZARD_NUMBER = 3
# LVL_NAME = ['moon', 'mountains', 'space', 'plains', 'chill']
# LVL_HAZ_NUM = [3, 6, 9, 12]

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
        self.currentLevel = 1
        self.hazards = []
        self.nextHazardIndex = 0
        self.generateHazards(HAZARD_NUMBER)
        self.hazards[HAZARD_NUMBER-1].color = (255,0,0)
        self.hazards[HAZARD_NUMBER-1].lastHazard = True


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

        # scored
        if self.car.x-(self.car.speed+1) < self.hazards[self.nextHazardIndex].x < self.car.x:
            if self.nextHazardIndex < HAZARD_NUMBER-1:
                self.nextHazardIndex += 1
                
            if self.hazards[self.nextHazardIndex].lastHazard:
                # self.nextStage()
                earned = 100 
            else:
                earned = 50 

            self.dash.scored(earned)


    def toggleDebugMode(self):
        global DEBUG_MODE
        DEBUG_MODE = True if DEBUG_MODE == False else False
        

    def nextStage(self):
        print('next stage')
        self.currentLevel += 1
        self.generateHazards(HAZARD_NUMBER * self.currentLevel)

    def generateHazards(self, num):
        for i in range(1, num+1):
            height = random.randint(20, 300)
            haz = Hazard(self.surface, 700 * i, self.windowHeight-height, 50, height)
            self.hazards.append(haz)
