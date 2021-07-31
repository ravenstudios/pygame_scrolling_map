from constants import *
from main_block import *
import pygame

class Main_drop(Main_block):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.Surface((BLOCK_SIZE // 2, BLOCK_SIZE // 2))
        self.image.fill((0, 0, 0))
        





    def update(self, player):
        if pygame.sprite.spritecollide(self, player, False):
            self.kill()
