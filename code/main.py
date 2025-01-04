from settings import *
from player import Player
import sys
from sprites import *
from random import randint

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Vampire Survivors Py")
        self.clock =  pygame.time.Clock()
        self.is_running = True

        # Groups
        self.all_sprites = pygame.sprite.Group()

        self.collision_sprites = pygame.sprite.Group()

        # Sprites
        self.player = Player((WINDOW_WIDTH/2, WINDOW_HEIGHT/2), self.all_sprites, self.collision_sprites)

        # Create collision objects
        for i in range(8):

            x, y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
            w, h = randint(60, 100), randint(50, 100)

            CollisionSprite((x, y), (w, h), (self.all_sprites, self.collision_sprites))


    def run(self):
        while self.is_running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                    sys.exit()

            # Update sprites
            self.all_sprites.update(dt)

            # Draw the game
            self.display_surface.fill('Black')
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()


        pygame.quit()




if __name__ == '__main__':
    game = Game()
    game.run()