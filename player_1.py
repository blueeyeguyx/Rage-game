import pygame 
from settings import TILE_SIZE

class Player223 (pygame.sprite.Sprite):
    on_ground = True
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image = pygame.image.load('catmario1.png')
        self.rect = self.image.get_rect(midbottom = pos)
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 4
        self.gravity = 0.5
        self.jump_speed = -16

    def key_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.image = pygame.image.load('catmario1.png')
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1 
            self.image = pygame.image.load('catmario2.png')
        else:
            self.direction.x = 0
        if keys[pygame.K_UP] and self.on_ground:
            self.jumping()
            self.on_ground = False

    def apply_gravity(self):
        
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        

    def jumping(self):
        self.direction.y = self.jump_speed

    def update(self):
        # self.apply_gravity()    
        self.key_input()
        