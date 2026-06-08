import pygame
from settings import TILE_SIZE

class BlueTile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image.fill('lightblue')
        self.rect = self.image.get_rect(topleft = (x,y+10))
        
    def update(self, shift):
        self.rect.x += shift