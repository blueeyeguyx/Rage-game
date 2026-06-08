import pygame
import time
from settings import WIDTH, HEIGHT, level_map1, level_map2
from level import Level
from setup import setupText, setupDeathText
from filereader import readWinDeath, WriteFile
#from auxil import win
pygame.init()

ablak = pygame.display.set_mode((WIDTH,HEIGHT))
level_map = level_map1
szint = Level(level_map,ablak)
clock = pygame.time.Clock()
run = True
szoveg = pygame.font.Font(None,60)
lives = 3
lives_decreased_this_round = False
wtext_surf, wtext_rect, dtext_surf, dtext_rect, atext_surf, atext_rect = setupText(szoveg)
d1text_surf, d1text_rect = setupDeathText(szoveg, lives)
wfeltetel, dfeltetel = readWinDeath()
game_active = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    activate = pygame.key.get_pressed()
    if activate[pygame.K_ESCAPE]:
        run = False
    
    wfeltetel, dfeltetel = readWinDeath()
    
    
    if game_active == 1:
        ablak.fill("lightblue")
        lives_decreased_this_round = False
        szint.run()
        if int(wfeltetel) == 1: 
            game_active = 2
            wfeltetel = 0
            WriteFile('./assets/win.txt', str(wfeltetel))
        elif int(dfeltetel) == 1:
            game_active = 3
            dfeltetel = 0
            WriteFile('./assets/dead.txt', str(dfeltetel))

    
    elif game_active == 0:
        ablak.fill("lightblue") 
        ablak.blit(atext_surf,atext_rect)
        activate = pygame.key.get_pressed()
        if activate[pygame.K_SPACE]:
            game_active = 1
        
   
    elif game_active == 2:
        ablak.fill('lightblue')
        ablak.blit(wtext_surf,wtext_rect)
        level_map = level_map2
        activate = pygame.key.get_pressed()
        if activate[pygame.K_SPACE]:
            szint.__init__(level_map,ablak)
            game_active = 1

    
    elif game_active == 3:
        ablak.fill('lightblue')
        if not lives_decreased_this_round:
            lives_decreased_this_round = True
            lives -= 1
        d1text_surf, d1text_rect = setupDeathText(szoveg, lives) 
        ablak.blit(d1text_surf,d1text_rect)
        activate = pygame.key.get_pressed()
        if activate[pygame.K_SPACE]:
            szint.__init__(level_map,ablak)
            game_active = 1


    clock.tick(60)
    pygame.display.update()



pygame.quit()
    