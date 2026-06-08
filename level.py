import pygame
from tile import Tile
from tile_b import Tile_b
from settings import TILE_SIZE, WIDTH
from player_1 import Player223
from winflag import wFlag
from spikes import Spike
from unvis_tile_a import unvis_Tile_a
from collisionChecker import *
from bluetile import BlueTile
from unvis_tile_b import unvis_Tile_b

class Level():
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.Wflag = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.greentile = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
        self.unvis_tiles_a = pygame.sprite.Group()
        self.blueTiles = pygame.sprite.Group()
        self.world_shift = 0
        self.setup_level(level_data)

    def setup_level(self, layout):
        for rowindex,row in enumerate(layout):
            for colindex,col in enumerate(row):
                x = colindex * TILE_SIZE
                y = rowindex * TILE_SIZE
                if col == 'X':
                    tile = Tile(TILE_SIZE, x, y )
                    self.tiles.add(tile)
                elif col == 'P':
                    jatekos = Player223((x,y))
                    self.player.add(jatekos)
                elif col == 'B':
                    tile_g = Tile_b(TILE_SIZE,x,y)
                    self.greentile.add(tile_g)
                elif col == 'W':
                    flag_w = wFlag(TILE_SIZE,x,y)
                    self.Wflag.add(flag_w)
                elif col == 'S':
                    spike_gen = Spike(TILE_SIZE,x,y)
                    self.spikes.add(spike_gen)
                elif col == 'U':
                    unvis = unvis_Tile_a(TILE_SIZE,x,y)
                    self.unvis_tiles_a.add(unvis)
                elif col == 'G':
                    blueTile = BlueTile(TILE_SIZE, x,y)
                    self.blueTiles.add(blueTile)
                elif col == 'C':
                    unvis_tile_b = unvis_Tile_b(TILE_SIZE, x, y)
                    self.unvis_tiles_a.add(unvis_tile_b)

    def horizontal_movement_collision(self):
        horizontalMovementCollision(self)

    def vertical_movement_collision(self):
        verticalMovementCollision(self)
    

    def scroll(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        
        if player_x < WIDTH/4 and direction_x < 0:
            self.world_shift = 4
            player.speed = 0

        elif player_x > WIDTH - (WIDTH / 4) and direction_x > 0:
            self.world_shift = -4
            player.speed = 0 

        else: 
            self.world_shift = 0
            player.speed = 4

    def run(self):
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.greentile.update(self.world_shift)
        self.greentile.draw(self.display_surface)
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.Wflag.update(self.world_shift)
        self.Wflag.draw(self.display_surface)
        self.spikes.draw(self.display_surface)
        self.spikes.update(self.world_shift)
        self.unvis_tiles_a.update(self.world_shift)
        self.unvis_tiles_a.draw(self.display_surface)
        self.scroll()
        self.player.draw(self.display_surface)