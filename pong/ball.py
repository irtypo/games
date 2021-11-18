import pygame as pg
import random

class Ball:
    def __init__(self, surface, color, x, y, radias):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.radius = radias
        self.directionX = 1
        self.directionY = 1
        self.speed = .0001
        # pg.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)
    
    def draw(self):
        if self.directionX > 0:
            self.x += self.speed
        else:
            self.x -= self.speed

        if self.directionY > 0:
            self.y += self.speed
        else:
            self.y -= self.speed

        pg.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)

    def spawn(self):
        self.x = 1280/2 + self.radius/2
        self.y = random.randint(10, 700)
        if random.randint(0,10) % 2 == 0:
            self.directionX *= 1
        else:
            self.directionX *= -1


    def scored(self, p):
        p.score += 1
        p.draw('goal')