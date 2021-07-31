
from main_block import *

class Wall(Main_block):

    def __init__(self, x, y):


        super().__init__(x, y)
        self.image.fill((180, 180, 180))
        self.y_vel = 0


    def update(self, all_group, player_group):
        self.falling(all_group, player_group)

    def falling(self, all_group, player_group):

        self.y_vel += GRAVITY
        self.rect = self.rect.move(0, self.y_vel)

        # WALL HITS
        wall_hits = pygame.sprite.spritecollide(self, all_group, False)
        # # if we did hit anything move back to make sure were not stuck
        for h in wall_hits:
            if h != self:
                if self.rect.bottom > h.rect.top:
                    self.y_vel = 0
                    self.rect.bottom = h.rect.top
                    # self.rect = self.rect.move(0, -self.y_vel)
                else:
                    self.y_vel += GRAVITY

        # PLAYERS HITS
        player_hits = pygame.sprite.spritecollide(self, player_group, False)
        # # if we did hit anything move back to make sure were not stuck
        for p in player_hits:
            if self.rect.bottom > p.rect.top:
                self.y_vel = 0
                self.rect.bottom = p.rect.top
                # self.rect = self.rect.move(0, -self.y_vel)
            else:
                self.y_vel += GRAVITY

        # sets the bottom of screen to stop falling
        if self.rect.bottom > GAME_WORLD_H:
            self.rect.bottom = GAME_WORLD_H
            self.y_vel = 0


    def dig(self, player):
        p_dir = player.dir
        pdd = PLAYER_DIG_DISTANCE

        if p_dir == "up":
            temp = player.rect.move(0, -pdd)
        elif p_dir == "down":
            temp = player.rect.move(0, pdd)
        elif p_dir == "left":
            temp = player.rect.move(-pdd, 0)
        elif p_dir == "right":
            temp = player.rect.move(pdd, 0)

        if self.rect.colliderect(temp):
            self.kill()
