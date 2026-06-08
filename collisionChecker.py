import pygame
from settings import HEIGHT
from filereader import WriteFile

def horizontalMovementCollision(level):
    player = level.player.sprite
    player.rect.x += player.direction.x * player.speed
        
    for sprite in level.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right    
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left
        
    for sprite in level.greentile.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right    
                    sprite.kill()
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    sprite.kill()

    for sprite in level.Wflag.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right    
                    win = 1
                    WriteFile('./assets/win.txt', str(win))
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    win = 1
                    WriteFile('./assets/win.txt', str(win))

    for sprite in level.spikes.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    sprite.image = pygame.image.load('./assets/spikes.png')    
                    lose = 1
                    WriteFile('./assets/dead.txt', str(lose))
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    sprite.image = pygame.image.load('./assets/spikes.png')    
                    lose = 1
                    WriteFile('./assets/dead.txt', str(lose))
        
    for sprite in level.unvis_tiles_a.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0 and sprite.active:
                    player.rect.left = sprite.rect.right    
                    sprite.image = pygame.image.load('./assets/tile.png')
                if player.direction.x > 0 and sprite.active:
                    player.rect.right = sprite.rect.left
                    sprite.image = pygame.image.load('./assets/tile.png')


def verticalMovementCollision(level):
     player = level.player.sprite
     player.apply_gravity()

     if player.rect.centery > HEIGHT:
            lose = 1
            WriteFile('./assets/dead.txt', str(lose))

     for sprite in level.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0: 
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0 
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0 

        
     for sprite in level.greentile.sprites():
            if sprite.rect.colliderect(player.rect):
                sprite.kill()
       
     for sprite in level.unvis_tiles_a.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0 and sprite.active: 
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0 
                    player.on_ground = True
                    sprite.image = pygame.image.load('./assets/tile.png')
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    sprite.image = pygame.image.load('./assets/tile.png')
                    sprite.active = True

     for sprite in level.Wflag.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0: 
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0 
                    player.on_ground = True
                    win = 1
                    WriteFile('./assets/win.txt', str(win))
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0 
                    win = 1
                    WriteFile('./assets/win.txt', str(win))
        
     for sprite in level.spikes.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0: 
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0 
                    player.on_ground = True
                    sprite.image = pygame.image.load('./assets/spikes.png')    
                    lose = 1
                    WriteFile('./assets/dead.txt', str(lose))
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    sprite.image = pygame.image.load('./assets/spikes.png')    
                    lose = 1
                    WriteFile('./assets/dead.txt', str(lose))

     for sprite in level.blueTiles.sprites():
          if sprite.rect.colliderect(player.rect):
               if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    sprite.image = pygame.image.load('./assets/tile.png')
    