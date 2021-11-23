import pygame as pg
index = 0

class Car:
    def __init__(self, surface, x, y):
        global index
        self.i = index
        self.surface = surface
        self.x = x
        self.y = y
        self.jumping = False
        self.falling = False
        self.jumpForce = 100
        self.airTime = 0
        # self.width = 100
        # self.height = 75
        self.score = 0
        # self.color = (255,255,255)
        # index += 1
        # self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.jumpHeight = 20
        self.img = pg.image.load('common\src\car.png')
        self.img = pg.transform.scale(self.img, (175, 88))


    def draw(self):
        if self.jumping == True:
            self.y -= 1
            self.airTime += 1
        if self.airTime >= self.jumpForce:
            self.jumping = False
            self.falling = True

        # if self.falling == True:
        #     self.y -= 1
        #     self.airTime += 1

        # if self.y
        # self.rect = pg.Rect(self.x, self.y-200, self.width, self.height)
        # pg.draw.rect(self.surface, self.color, self.rect)
        self.surface.blit(self.img, (self.x, self.y-100))
        # self.hover()
        # print(self.y)

    def jump(self):
        self.jumping = True
        # for i in range(0,self.jumpHeight):
            # self.y -= i

    def hover(self):
        for i in range(0, 10):
            self.y += i

        for i in range(0, 10):
            self.y -= i