class CPU:
    def __init__(self, level):
        self.level = level

    def run(self, player, ball, level):

        # if ball.x > player.x - (60 * 3):
        player.y = ball.y - player.height/2


