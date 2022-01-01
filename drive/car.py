from os import truncate
import pygame as pg
index = 0

class Car:
    def __init__(self, surface, x, y):
        global index
        self.i = index
        self.surface = surface
        self.groundLevel = y
        self.x = x
        self.y = y-200
        self.jumping = False
        self.falling = False
        self.jumpForce = 100
        self.airTime = 0
        self.velX = 1
        self.velY = 1
        # self.width = 100
        # self.height = 75
        self.score = 0
        self.fuel = 1000
        self.maxFuel = 2000
        self.grounded = False
        self.hovering = False
        # self.color = (255,255,255)
        # index += 1
        # self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.jumpHeight = 20
        self.img = pg.image.load('common\src\car.png')
        self.img = pg.transform.scale(self.img, (175, 88))


    def draw(self):

        # ground collision and conditional gravity
        if not self.jumping and self.y < self.groundLevel:
            self.falling = True
            self.grounded = False
            self.hovering = False
            self.y += self.velY

        # driving or falling
        if self.y >= self.groundLevel:
            self.falling = False
            self.grounded = True
            self.hovering = False

        # jumping
        if self.jumping and not self.falling:
            hangTime = pg.time.get_ticks()
            maxAir = 500
            self.y -= 1

            if hangTime > self.startJump + maxAir:
                self.jumping = False
            
        # hovering
        if self.hovering:
            self.fuel -= 1
            if self.fuel <= 0:
                self.fuel = 0
                self.jumpStop()

        self.surface.blit(self.img, (self.x, self.y-100))



    def jumpStart(self):
        if self.fuel > 0:
            self.jumping = True
            self.startJump = pg.time.get_ticks()

    def jumpStop(self):
        if not self.falling:
            pg.time.wait(90)
        self.jumping = False

    def hover(self):
        self.jumping = True
        self.hovering = True

    def refuel(self, amount):
        if self.fuel <= self.maxFuel:
            self.fuel += amount
        if self.fuel > self.maxFuel:
            self.fuel = self.maxFuel