import time

class CPU:
    def __init__(self):
        self.t0 = time.time()
        self.t = self.t0
        self.tPrev = self.t
        self.level = 0

    def run(self, player, ball, level):
        self.level = level
        self.t = time.time()


        # time.sleep(1)
        # if self.t > (self.tPrev + .033):
        player.y = ball.y
            # self.tPrev = self.t


