import pygame as pg
from pong.ball import Ball
from pong.paddle import Paddle
from pong.cpu import CPU

color_green = (0x32, 0xcd, 0x32)
ballOnPaddle = False

class Pong:
    def __init__(self, surface, win_w, play_h):
        self.surface = surface
        self.windowWidth = win_w
        self.windowHeight = play_h
        self.playArea = pg.Rect(0, 0, self.windowWidth, self.windowHeight)
        self.balls = []
        self.players = []
        self.cpu = CPU(10)
        self.balls.append(Ball(self.surface, color_green, 200, 200, 10))
        self.players.append(Paddle(self.surface, 60, 10))
        self.players.append(Paddle(self.surface, self.windowWidth-(60+10), 10))
        self.balls[0].spawn()


    def draw(self, p1Y):
        self.players[0].y = p1Y

        # paddle boundrary collision check
        for p in self.players:
            if self.playArea.collidepoint(p.x, p.y + p.height) == False:
                p.y = self.windowHeight - p.height

            if p.rect.collidepoint(self.balls[0].x, self.balls[0].y) == True:
                self.balls[0].bounce('horizontal')


        self.goalCheck()

        # top bot collide
        if self.balls[0].y <= 0 or self.balls[0].y >= self.windowHeight:
            self.balls[0].bounce('vert')

        self.cpu.run(self.players[1], self.balls[0], 10)
        self.players[0].draw()
        self.players[1].draw()
        self.balls[0].draw()

        # green border
        pg.draw.rect(self.surface, (0, 0xff, 0), self.playArea, width=10)

    def goalCheck(self):
        if self.balls[0].x <= 0:
            # self.players[1].score +=1
            self.balls[0].spawn()
        
        if self.balls[0].x >= self.windowWidth:
            # self.players[0].score +=1
            self.balls[0].spawn()


