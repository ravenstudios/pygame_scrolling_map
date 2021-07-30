
from main_block import *

class Block(Main_block):

    def __init__(self):


        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        super().__init__(self.x, self.y)
        self.image.fill((100, 110, 255))
        



    def update(self):
        pass
