
from main_block import *

class Player(Main_block):

    def __init__(self):


        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE * 2
        super().__init__(self.x, self.y)

        self.speed = BLOCK_SIZE // 8
        self.grav = GRAVITY
        self.jump_vel = PLAYER_JUMP_VEL
        self.dir = "right"
        self.y_vel = 0.1





    def update(self, all_group):
        self.input(all_group)
        self.falling(all_group)







    def falling(self, all_group):

        if self.y_vel > PLAYER_MAX_Y_VEL:
            self.y_vel = PLAYER_MAX_Y_VEL

        if self.y_vel < -PLAYER_MAX_Y_VEL:
            self.y_vel = -PLAYER_MAX_Y_VEL


        self.y_vel += self.grav


        self.rect = self.rect.move(0, self.y_vel)
        # # gets all sprites that it collided with
        hits = pygame.sprite.spritecollide(self, all_group, False)
        # # if we did hit anything move back to make sure were not stuck
        if hits:

            self.rect = self.rect.move(0, -self.y_vel)
            self.y_vel = 0
            # y_snap = self.rect.y // BLOCK_SIZE * BLOCK_SIZE
            # self.rect.y = y_snap

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

        #z jump
        if (keys[pygame.K_z] or keys[pygame.K_w]):
            # self.rect = self.rect.move(0, -10)
            self.y_vel += self.jump_vel
