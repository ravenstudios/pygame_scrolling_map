
from main_block import *

class Wall(Main_block):

    def __init__(self, x, y):


        super().__init__(x, y)
        self.image.fill((180, 180, 180))
