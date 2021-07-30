
from main_block import *

class Player(Main_block):

    def __init__(self):


        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        super().__init__(self.x, self.y)

        self.speed = BLOCK_SIZE // 8
        self.grav = 5
        self.dir = "right"





    def update(self, all_group):
        self.input(all_group)
        self.falling(all_group)







    def falling(self, all_group):
        self.rect = self.rect.move(0, self.grav)
        # # gets all sprites that it collided with
        hits = pygame.sprite.spritecollide(self, all_group, False)
        # # if we did hit anything move back to make sure were not stuck
        if hits:

            self.rect = self.rect.move(0, -self.grav)

    def input(self, all_group):

        keys = pygame.key.get_pressed()


        # DOWN
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]):
            self.dir = "down"
        #     self.rect = self.rect.move(0, self.speed)
            # # move
            # self.rect = self.rect.move(0, self.speed)
            # # gets all sprites that it collided with
            # hits = pygame.sprite.spritecollide(self, all_group, False)
            # # if we did hit anything move back to make sure were not stuck
            # if hits:
            #     self.rect = self.rect.move(0, -self.speed)
            #
            # # if not center on a block move right or left to assist in going down if blocked
            # for h in hits:
            #     if self.rect.center[0] < h.rect.left and self.rect.right > h.rect.left:
            #         self.rect = self.rect.move(-self.speed, 0)
            #     if self.rect.center[0] > h.rect.right and self.rect.left < h.rect.right:
            #         self.rect = self.rect.move(self.speed, 0)

        # UP
        if (keys[pygame.K_w] or keys[pygame.K_UP]):
            self.dir = "up"
        #     if self.rect.top > BLOCK_SIZE:
        #         self.rect = self.rect.move(0, -self.speed)
            # move
            # self.rect = self.rect.move(0, -self.speed)
            # # gets all sprites that it collided with
            # hits = pygame.sprite.spritecollide(self, all_group, False)
            # # if we did hit anything move back to make sure were not stuck
            # if hits:
            #     self.rect = self.rect.move(0, self.speed)
            #
            # # if not center on a block move right or left to assist in going down if blocked
            # for h in hits:
            #     if self.rect.center[0] < h.rect.left and self.rect.right > h.rect.left:
            #         self.rect = self.rect.move(-self.speed, 0)
            #     if self.rect.center[0] > h.rect.right and self.rect.left < h.rect.right:
            #         self.rect = self.rect.move(self.speed, 0)

        # LEFT
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]):
            self.dir = "left"
            # move
            self.rect = self.rect.move(-self.speed, 0)
            # gets all sprites that it collided with
            hits = pygame.sprite.spritecollide(self, all_group, False)
            # if we did hit anything move back to make sure were not stuck
            if hits:
                self.rect = self.rect.move(self.speed, 0)
            #
            # # if not center on a block move right or left to assist in going down if blocked
            # for h in hits:
            #     if self.rect.center[1] < h.rect.top and self.rect.bottom > h.rect.top:
            #         self.rect = self.rect.move(0, -self.speed)
            #     if self.rect.center[1] > h.rect.bottom and self.rect.top < h.rect.bottom:
            #         self.rect = self.rect.move(0, self.speed)

        # RIGHT
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
            self.dir = "right"
            # # move
            self.rect = self.rect.move(self.speed, 0)
            # gets all sprites that it collided with
            hits = pygame.sprite.spritecollide(self, all_group, False)
            # if we did hit anything move back to make sure were not stuck
            if hits:
                self.rect = self.rect.move(-self.speed, 0)
            #
            # # if not center on a block move right or left to assist in going down if blocked
            # for h in hits:
            #     if self.rect.center[1] < h.rect.top and self.rect.bottom > h.rect.top:
            #         self.rect = self.rect.move(0, -self.speed)
            #     if self.rect.center[1] > h.rect.bottom and self.rect.top < h.rect.bottom:
            #         self.rect = self.rect.move(0, self.speed)

        # SPACE / SET Bomb
        # if (keys[pygame.K_SPACE]):
        #     self.set_bomb(bombs_group)

    def get_rect(self):
        return self.get_rect


    def set_bomb(self, bombs_group):
        bombs_group.add(bomb.Bomb(self.rect.x, self.rect.y, self.fire_length))
        print("bomb set ")
        print(bombs_group)
