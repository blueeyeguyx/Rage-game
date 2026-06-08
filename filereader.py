def readWinDeath():
    with open('./assets/win.txt','r') as ertek:
        wfeltetel = ertek.readline()
    with open('./assets/dead.txt','r') as ertek:
        dfeltetel = ertek.readline()
    ertek.close()
    return [wfeltetel, dfeltetel]

def WriteFile(path, value):
    with open(path, 'w') as file:
        file.write(value)
    
    file.close()