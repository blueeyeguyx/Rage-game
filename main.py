import pygame
from settings import WIDTH, HEIGHT, level_map
from level import Level
#from auxil import win
pygame.init()

ablak = pygame.display.set_mode((WIDTH,HEIGHT))
szint = Level(level_map,ablak)
clock = pygame.time.Clock()
run = True
szoveg=pygame.font.Font(None,60)
wtext_surf = szoveg.render('Gratulálok, nyertél.', True, 'red')
wtext_rect = wtext_surf.get_rect(center = (WIDTH/2,HEIGHT/2))
dtext_surf = szoveg.render('Sajnos vesztettél.', True, 'red')
dtext_rect = dtext_surf.get_rect(center = (WIDTH/2,HEIGHT/2))

atext_surf = szoveg.render('Press Space', True, 'red')
atext_rect = atext_surf.get_rect(center = (WIDTH/2,HEIGHT/2))
with open('win.txt','r') as ertek:
    wfeltetel = ertek.readline()
with open('dead.txt','r') as ertek:
    dfeltetel = ertek.readline()
ertek.close()    
game_active = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    
    with open('win.txt','r') as ertek:
        wfeltetel = ertek.readline()
    ertek.close()
    
    
    with open('dead.txt', 'r') as file:
        dfeltetel = file.readline()
    file.close()
    
    
    if game_active == 1:
        ablak.fill("lightblue")
        szint.run()
        if int(wfeltetel) == 1: 
            game_active = 2
            wfeltetel = 0
            with open('win.txt','w') as file:
                file.write(str(wfeltetel))
            file.close()
        elif int(dfeltetel) == 1:
            game_active = 3
            dfeltetel = 0
            with open('dead.txt','w') as file:
                file.write(str(dfeltetel))
            file.close()

    
    elif game_active == 0:
        ablak.fill("lightblue") 
        ablak.blit(atext_surf,atext_rect)
        activate = pygame.key.get_pressed()
        if activate[pygame.K_SPACE]:
            game_active = 1
        
   
    elif game_active == 2:
        ablak.fill('lightblue')
        ablak.blit(wtext_surf,wtext_rect)

    
    elif game_active == 3:
        ablak.fill('lightblue')
        ablak.blit(dtext_surf,dtext_rect)

    clock.tick(60)
    pygame.display.update()



pygame.quit()
    