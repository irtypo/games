import pygame as pg
HOVER_COST = .25
GRAVITY = 5

class Car(pg.sprite.Sprite):
    def __init__(self, surface, x, y):
        pg.sprite.Sprite.__init__(self)
        self.surface = surface
        self.groundLevel = y
        self.x = x
        self.y = y-200
        self.jumping = False
        self.falling = True
        self.flying = False
        self.speed = 3
        self.score = 0
        self.fuel = 1000
        self.maxFuel = 2000
        self.grounded = False
        self.hovering = False
        self.images = []
        self.index = 0
        self.counter = 0
        self.idleImgCount = 4
        for i in range(0, self.idleImgCount):
            img = pg.image.load(f'common/src/car/idle_{i}.png')
            img = pg.transform.scale(img, (175, 88))
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        # self.rect.center = [self.x, self.y]
        
    def update(self):
        self.counter += 1
        idleCooldown = 10
        if self.counter > idleCooldown:
            self.counter = 0
            self.index = (self.index + 1) % self.idleImgCount
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y-self.rect.height
        self.rect.height = self.rect.height *.8

    def draw(self):
        # ground collision and conditional gravity
        if not (self.jumping or self.flying) and self.y < self.groundLevel:
            self.falling = True
            self.grounded = False
            self.hovering = False
            self.y += GRAVITY

        # driving or falling
        if self.y >= self.groundLevel:
            self.falling = False
            self.grounded = True
            self.hovering = False

        # jumping
        if self.jumping and not self.falling:
            hangTime = pg.time.get_ticks()
            maxAir = 1200
            self.y -= GRAVITY

            if hangTime > self.startJump + maxAir:
                self.jumping = False
                self.hovering = True
            
        # hovering
        if self.hovering:
            self.fuel -= HOVER_COST

        if self.flying:
            self.y -= HOVER_COST*3
            if self.y < self.rect.height/2:
                self.y = self.rect.height/2
            self.fuel -= HOVER_COST*4

        if self.fuel <= 0:
            self.fuel = 0
            self.jumpStop()

        self.surface.blit(self.image, (self.x, self.y-100))



    def jumpStart(self):
        self.jumping = True
        self.startJump = pg.time.get_ticks()

    def jumpStop(self):
        if not self.falling:
            pg.time.wait(90)
        self.jumping = False
        self.flying = False

    def hover(self):
        if self.fuel > 0:
            self.jumping = True
            self.hovering = True

    def fly(self):
        if self.fuel > 0:
            self.flying = True
            self.jumping = True
            self.hovering = True

    def addFuel(self, amount):
        if self.fuel <= self.maxFuel:
            self.fuel += amount
        if self.fuel > self.maxFuel:
            self.fuel = self.maxFuel