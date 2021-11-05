import pygame as pg
import random

class Ball:
    def __init__(self, surface, color, x, y, radias):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.radius = radias
        self.direction = 6
        self.speedX = .5
        self.speedY = .5
        pg.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)
    
    def draw(self):
        if self.speedX > 0:
            self.x += 1
        else:
            self.x -= 1

        if self.speedY > 0:
            self.y += 1
        else:
            self.y -= 1

        pg.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)

    def spawn(self):
        self.x = 1280/2 + self.radius/2
        self.y = random.randint(10, 700)
        if random.randint(0,10) % 2 == 0:
            self.speedX *= 1
        else:
            self.speedX *= -1


    def scored(self, p):
        p.score += 1