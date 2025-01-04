from settings import * 

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(join('images','player', 'down', '0.png')).convert_alpha()
        self.rect = self.image.get_frect(center = pos)
        self.hitbox_rect = self.rect.inflate(-60, -8)


        self.speed = 500
        self.direction = pygame.Vector2()

        # Groups
        self.collision_sprites = collision_sprites

    def key_input(self):
        keys = pygame.key.get_pressed()

        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, dt):

        # Handle horizontal movement
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.collision("horizontal")


        # Handle vertical movement
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.collision("vertical")

        # Update the actual player rectangle (not the hitbox)
        self.rect.center = self.hitbox_rect.center



    def collision(self, direction):
        
        # Loop through the collision sprites
        for collision_sprite in self.collision_sprites:
            # If the collision sprite collides with my rect
            if collision_sprite.rect.colliderect(self.hitbox_rect):
                
                # Handle horizontal collisions
                if direction == 'horizontal':
                    if self.direction.x > 0:  # player is moving to the right
                        self.hitbox_rect.right = collision_sprite.rect.left
                    if self.direction.x < 0:  # player is moving to the left
                        self.hitbox_rect.left = collision_sprite.rect.right
                else:
                    # Handle vertical collisions
                    if self.direction.y > 0:  # player is moving downwards
                        self.hitbox_rect.bottom = collision_sprite.rect.top
                    if self.direction.y < 0:  # player is moving upwards
                        self.hitbox_rect.top = collision_sprite.rect.bottom



    def update(self, dt):
        self.key_input()
        self.move(dt)