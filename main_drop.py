from constants import *
import pygame

class Main_drop(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 32
        self.height =  32
        self.image = pygame.Surface((BLOCK_SIZE // 2, BLOCK_SIZE // 2))
        self.image.fill((0, 0, 0))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (x, y)





    def update(self, player):
        if pygame.sprite.spritecollide(self, player, False):
            self.kill()
