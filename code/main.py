from settings import *
from player import Player
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Vampire Survivors Py")
        self.clock =  pygame.time.Clock()
        self.is_running = True

        # Groups
        self.all_sprites = pygame.sprite.Group()

        # Sprites
        self.player = Player((WINDOW_WIDTH/2, WINDOW_HEIGHT/2), self.all_sprites)


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