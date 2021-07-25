import pygame
from constants import *


class Camera():
    '''
    To use camera we need to followe player and offset the rest of the world
    INCLUDING the player. So make sure camera is applied to ALL sprites
    of the game in the draw function. I.E.

    INSTEAD OF:
      sprites_group.draw(surface)
    we need to intercept the rect for each sprite and offset them so...
    USE:
      for sprite in self.sprites_group:
          surface.blit(sptite.image, self.camera.move(sprite.rect))
    '''

    # width and height are not screen size but world
    def __init__(self, width, height):
        self.rect = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def update(self, player):
        # offsets self.rect by pos of player
        x = -player.rect.x + int(GAME_WIDTH // 2)
        y = -player.rect.y + int(GAME_HEIGHT // 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - GAME_WIDTH), x)  # right
        y = max(-(self.height - GAME_HEIGHT), y)  # bottom
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect, 3)


    def move(self, sprite):
        return sprite.move(self.rect.topleft)
