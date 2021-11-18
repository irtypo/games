import pygame as pg
from pong.scoreboard import ScoreBoard as hud
from pong.ball import Ball
from pong.paddle import Paddle
from pong.cpu import CPU

color_green = (0x32, 0xcd, 0x32)

class Pong:
    def __init__(self, surface, win_w, play_h):
        self.surface = surface
        self.windowWidth = win_w
        self.windowHeight = play_h
        # self.hudHeight = self.windowHeight * .2
        self.playArea = pg.Rect(0, 0, self.windowWidth, self.windowHeight)
        # self.playHeight = self.windowHeight - (self.windowHeight * .2)
        self.balls = []
        self.players = []
        # self.hud = hud(self.surface, self.windowWidth, self.windowHeight, 'pong')
        self.cpu = CPU(10)
        self.balls.append(Ball(self.surface, color_green, 200, 200, 10))
        self.players.append(Paddle(self.surface, 60, 10))
        self.players.append(Paddle(self.surface, self.windowWidth-(60+10), 10))
        # self.balls[0].spawn()


    def draw(self, p1Y):
        self.players[0].y = p1Y
        
        # draw game
        self.cpu.run(self.players[1], self.balls[0], 10)
        self.players[0].draw()
        self.players[1].draw()
        self.balls[0].draw()

        print(self.balls[0].x, self.balls[0].y)
        # self.collisionCheck(self.balls[0], self.players)

        pg.draw.rect(self.surface, (0, 0xff, 0), self.playArea, width=10)















    # def play(self):
    #     self.balls.append(Ball(self.surface, (0x32, 0xcd, 0x32), 200, 200, 10))
    #     self.players.append(Paddle(self.surface, 60))
    #     self.players.append(Paddle(self.surface, self.windowWidth-(60+10)))
    #     self.balls[0].spawn()

    #     while not self.gameOver:
    #         for event in pg.event.get():
    #             if event.type == pg.QUIT:
    #                 self.gameOver = True
    #             elif event.type == pg.MOUSEMOTION:
    #                 self.players[0].y = event.pos[1]

    #     # draw background
    #         pg.display.update()
    #         self.surface.fill((0,0,0))
    #     # draw game
            

    #         self.cpu.run(self.players[1], self.balls[0], 10)
    #         self.players[0].draw(None)
    #         self.players[1].draw(None)
    #         self.hud.draw(self.players[0].score, self.players[1].score)
    #         self.balls[0].draw()
    #         self.collisionCheck(self.balls[0], self.players)

    #     pg.quit()

    # def collisionCheck(self, b, players):
    #     # goal
    #     if b.x <= 0:
    #         b.scored(players[1])
    #         b.spawn()
    #     elif b.x >= self.windowWidth:
    #         b.scored(players[0])
    #         b.spawn()

    #     # top/bottom bounce
    #     if b.y <= 0:
    #         b.directionY *= -1
    #         b.y = 0 + b.radius
    #     elif b.y >= self.windowHeight - self.hudHeight:
    #         b.directionY *= -1
    #         b.y = self.windowHeight - self.hudHeight - b.radius
    
    #     for p in players:
    #     # paddle boundaries
    #         if p.y < 0:
    #             p.y = 0
    #         elif p.y > (self.playHeight - p.height):
    #             p.y = int(self.playHeight - p.height)
            

    #         # blocked shot (add deflected shots later)
    #         if p.y < b.y < p.y+p.height:
    #             if p.i == 0:
    #                 if b.x < p.x + p.width:
    #                         b.directionX *= -1
    #             if p.i == 1:
    #                 if b.x > p.x - p.width:
    #                     b.directionX *= -1
