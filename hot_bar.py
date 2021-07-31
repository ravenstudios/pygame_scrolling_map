from constants import *
import pygame
import random
import wood
class Hot_bar(pygame.sprite.Sprite):
    def __init__(self, x, y ,width, height):
        super().__init__()

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = 5
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((128, 128 ,128))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)

    def update(self):

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image.fill((220, 220 ,220))

        else:
            self.image.fill((128, 128 ,128))
