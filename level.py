import pygame
from tile import Tile
from tile_b import Tile_b
from settings import level_map, TILE_SIZE, WIDTH, HEIGHT
from player_1 import Player223
from winflag import wFlag
from spikes import Spike
from unvis_tile_a import unvis_Tile_a

win = 0
lose = 0
class Level():
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.Wflag = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.greentile = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
        self.unvis_tiles_a = pygame.sprite.Group()
        self.world_shift = 0
        self.setup_level(level_data)

    def setup_level(self, layout):
        for rowindex,row in enumerate(level_map):
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

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right    
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left
        
        for sprite in self.greentile.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right    
                    sprite.kill()
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    sprite.kill()

        for sprite in self.Wflag.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right    
                    win = 1
                    with open('win.txt','w') as wfile:
                        wfile.write(str(win))
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    win = 1
                    with open('win.txt','w') as wfile:
                        wfile.write(str(win))

        for sprite in self.spikes.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    sprite.image = pygame.image.load('spikes.png')    
                    lose = 1
                    with open('dead.txt','w') as wfile:
                        wfile.write(str(lose))
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    sprite.image = pygame.image.load('spikes.png')    
                    lose = 1
                    with open('dead.txt','w') as wfile:
                        wfile.write(str(lose))
        
        for sprite in self.unvis_tiles_a.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right    
                    sprite.image = pygame.image.load('tile.png')
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    sprite.image = pygame.image.load('tile.png')
        
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        if player.rect.centery > HEIGHT:
            lose = 1
            with open('dead.txt','w') as file:
                file.write(str(lose))

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0: 
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0 
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0 

        
        for sprite in self.greentile.sprites():
            if sprite.rect.colliderect(player.rect):
                # if player.direction.y > 0: 
                #     player.rect.bottom = sprite.rect.top
                #     player.direction.y = 0 
                #     player.on_ground = True
                # elif player.direction.y < 0:
                #     player.rect.top = sprite.rect.bottom
                #     player.direction.y = 0 
                sprite.kill()
       
        for sprite in self.unvis_tiles_a.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0: 
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0 
                    player.on_ground = True
                    sprite.image = pygame.image.load('tile.png')
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    sprite.image = pygame.image.load('tile.png')

        for sprite in self.Wflag.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0: 
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0 
                    player.on_ground = True
                    win = 1
                    with open('win.txt','w') as wfile:
                        wfile.write(str(win))
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0 
                    win = 1
                    
                    with open('win.txt','w') as wfile:
                        wfile.write(str(win))
        
        for sprite in self.spikes.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0: 
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0 
                    player.on_ground = True
                    sprite.image = pygame.image.load('spikes.png')    
                    lose = 1
                    with open('dead.txt','w') as wfile:
                        wfile.write(str(lose))
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    sprite.image = pygame.image.load('spikes.png')    
                    lose = 1
                    
                    with open('dead.txt','w') as wfile:
                        wfile.write(str(lose))
    

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