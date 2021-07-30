
from main_block import *

class Wall(Main_block):

    def __init__(self, x, y):


        super().__init__(x, y)
        self.image.fill((180, 180, 180))


    def dig(self, player):
        p_dir = player.dir
        pdd = PLAYER_DIG_DISTANCE

        if p_dir == "up":
            temp = player.rect.move(0, -pdd)
        elif p_dir == "down":
            temp = player.rect.move(0, pdd)
        elif p_dir == "left":
            temp = player.rect.move(-pdd, 0)
        elif p_dir == "right":
            temp = player.rect.move(pdd, 0)

        if self.rect.colliderect(temp):
            self.kill()
        # pr = player.rect
        # sr = self.rect
        # y_snap = (pr.top // BLOCK_SIZE) * BLOCK_SIZE
        # if pr.right + 5 > sr.left  and sr.top == y_snap:
        #     self.kill()
