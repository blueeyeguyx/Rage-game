from settings import WIDTH, HEIGHT

def setupText(font):
    wtext_surf = font.render('Gratulálok, nyertél.', True, 'red')
    wtext_rect = wtext_surf.get_rect(center = (WIDTH/2,HEIGHT/2))
    dtext_surf = font.render('Sajnos vesztettél.', True, 'red')
    dtext_rect = dtext_surf.get_rect(center = (WIDTH/2,HEIGHT/2))

    atext_surf = font.render('Press Space', True, 'red')
    atext_rect = atext_surf.get_rect(center = (WIDTH/2,HEIGHT/2))

    return [wtext_surf, wtext_rect, dtext_surf, dtext_rect, atext_surf, atext_rect]

def setupDeathText(font, lives):

    dtext_surf = font.render(f"{str(lives)}x", True, 'red')
    dtext_rect = dtext_surf.get_rect(center = (WIDTH/2,HEIGHT/2))

    return [dtext_surf, dtext_rect]
