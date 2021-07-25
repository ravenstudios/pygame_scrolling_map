from main_block import *
import pygame


class Health(Main_block):

    def __init__(self, x, y):


        super().__init__(x, y)

        self.image = pygame.image.load("health.png")
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (x, y)
