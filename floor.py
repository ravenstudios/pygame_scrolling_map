
from main_block import *

class Floor(Main_block):

    def __init__(self, x, y):


        super().__init__(x, y)
        self.image = pygame.image.load(os.path.join('images', 'floor_block.png'))
