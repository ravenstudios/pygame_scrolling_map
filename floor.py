
from main_block import *

class Floor(Main_block):

    def __init__(self, x, y):


        super().__init__(x, y)
        self.image.fill((100, 100, 100))
