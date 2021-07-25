from constants import *
import sys, pygame, player, camera, wall, health



class States_manager:
    def __init__(self):
        self.running = True
        self.states = ["start", "running", "paused", "dead"]
        self.state = self.states[1]

        self.health_bar = health.Health(0, 0)

        self.all_group = pygame.sprite.Group()

        n = 20
        self.player = player.Player()
        # the args for this need to be the w, h, of the world map NOT THE SCREEN SIZE!
        self.camera = camera.Camera(n * BLOCK_SIZE, n * BLOCK_SIZE)

        # self.player_group.add(self.player)
        self.all_group.add(self.player)

        for r in range(n):
            for c in range(n):
                if r == 0 or r == (n - 1) or c == 0 or c == (n - 1):
                    self.all_group.add(wall.Wall(r * BLOCK_SIZE, c * BLOCK_SIZE))


    def events(self, events):

        # print(events)
        for event in events:
            # if event.type == pygame.QUIT:
            #     self.running = False

            #Keyboard
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                #used to kill outside loop
                if event.key == pygame.K_q:
                    return True

                if event.key == pygame.K_r:
                    # Reset map
                    self.map.reset()

                if event.key == pygame.K_p:

                    if self.state == "paused":
                        self.state = "running"
                    else:
                        self.state = "paused"

            if event.type == pygame.KEYUP:
                if event.key == 32:#SPACE
                    if self.state == "start":
                        self.state = "running"


    def draw(self, surface):
        # surface.fill((100, 100, 100))#background
        self.draw_grid(surface)

        if self.state == "start":
            surface.fill((100, 100, 255))#background

        elif self.state == "running":


            for wall in self.all_group:
                surface.blit(wall.image, self.camera.move(wall.rect))




            # self.player_group.draw(surface)
            self.camera.draw(surface)

            r = pygame.Rect(0, 0, self.player.health, 64)
            pygame.draw.rect(surface, RED, r)
            surface.blit(self.health_bar.image, self.health_bar.rect)

        elif self.state == "paused":
            surface.fill((255, 100, 100))#background


        elif self.state == "dead":
            surface.fill((50, 50, 50))#background

        pygame.display.flip()


    def update(self, surface):
        surface.fill((100, 100, 100))#background
        self.camera.update(self.player)

        if self.state == "start":
            pass
        elif self.state == "running":
            self.camera.update(self.player)
            self.all_group.update()

        elif self.state == "paused":
            pass
        elif self.state == "dead":
            pass


    def draw_grid(self, surface):
        for x in range(0, GAME_WIDTH, BLOCK_SIZE):
            pygame.draw.line(surface, BLUE, (x, 0), (x, GAME_HEIGHT))
        for y in range(0, GAME_HEIGHT, BLOCK_SIZE):
            pygame.draw.line(surface, BLUE, (0, y), (GAME_WIDTH, y))
