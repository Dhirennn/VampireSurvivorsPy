from settings import *
from player import Player
import sys
from sprites import *
from random import randint
from pytmx.util_pygame import load_pygame
from groups import AllSprites

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Vampire Survivors Py")
        self.clock =  pygame.time.Clock()
        self.is_running = True

        # Groups
        self.all_sprites = AllSprites()

        self.collision_sprites = pygame.sprite.Group()

        self.setup_game_tiles()

        # Sprites
        self.player = Player((500, 300), self.all_sprites, self.collision_sprites)

        # Create collision objects
        # for i in range(8):

        #     x, y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
        #     w, h = randint(60, 100), randint(50, 100)

        #     CollisionSprite((x, y), (w, h), (self.all_sprites, self.collision_sprites))


    def setup_game_tiles(self):
        map = load_pygame(join('data', 'maps', 'world.tmx'))
        
        # Render tiles (non-collision objects)
        for x, y, image in map.get_layer_by_name('Ground').tiles():
            NonCollisionSprite((x*TILE_SIZE, y*TILE_SIZE), image, self.all_sprites)

        # Render collision objects
        for obj in map.get_layer_by_name('Objects'):
            CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))

        # Collision (invisible) layer
        for obj in map.get_layer_by_name('Collisions'):
            # print(obj)
            CollisionSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites)





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
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()


        pygame.quit()




if __name__ == '__main__':
    game = Game()
    game.run()