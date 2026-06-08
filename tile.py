import pygame
from settings import TILE_SIZE

class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image = pygame.image.load('./assets/tile.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (x,y))
    def update(self, shift):
        self.rect.x += shift