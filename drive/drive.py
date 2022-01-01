import pygame as pg
from drive.car import Car
from drive.dashboard import DashBoard
from drive.hazard import Hazard
LEVELS = ['moon', 'mountains', 'space', 'plains', 'chill']
DEBUG_MODE = False

class Drive:
    def __init__(self, surface, win_w, win_h, md):
        global LEVELS
        self.gameName = 'drive'
        self.surface = surface
        self.windowWidth = win_w
        self.windowHeight = win_h - (win_h * .2)
        self.md = md
        self.car = Car(self.surface, 200, win_h - (win_h * .2))
        self.dash = DashBoard(surface, win_w, win_h, md)
        self.car_group = pg.sprite.Group()
        self.car_group.add(self.car)
        self.background = pg.image.load(f'common/src/background/{LEVELS[3]}.png')
        self.scrolledDist = 0
        self.hazard = Hazard(self.surface, win_w + 50, self.windowHeight-100, 50, 100)

    def draw(self):
        # draw background
        self.surface.blit(self.background, (self.scrolledDist, 0))
        self.scrolledDist -= self.car.speed
        if self.scrolledDist <= -640:
            self.scrolledDist = 0

        # draw hud
        self.dash.draw(self.md, int(self.car.fuel))

        # draw hitboxes
        if DEBUG_MODE:
            pg.draw.rect(self.surface, (0, 255, 0), self.car.rect)
    
        # draw car
        self.car.draw()
        self.car_group.update()

        # draw hazard
        if self.hazard.rect.x > 0-self.hazard.rect.width:
            self.hazard.scroll(self.car.speed)
        self.hazard.draw()

        # collision
        if self.car.rect.colliderect(self.hazard.rect):
            self.car.speed = 0


        # print(self.dash.titleText.get_rect())
        

    def toggleDebugMode(self):
        global DEBUG_MODE
        DEBUG_MODE = True if DEBUG_MODE == False else False