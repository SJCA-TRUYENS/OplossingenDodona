def f1(pad):
    bestand = open(pad)
    regels = bestand.readlines()
    bestand.close()
    return len(regels)

def f2(pad, plaats):
    bestand = open(pad)
    tekst = bestand.read()
    bestand.close()
    return tekst[plaats]

def f3(pad, regelnummer):
    bestand = open(pad)
    regels = bestand.readlines()
    gekozen_regel = regels[regelnummer]
    bestand.close()
    return len(gekozen_regel)

def f4(pad):
    bestand = open(pad)
    tekst = bestand.read()
    bestand.close()
    return len(tekst)