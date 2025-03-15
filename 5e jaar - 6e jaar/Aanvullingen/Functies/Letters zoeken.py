def zoekLetters(woord, letter) :
    lijst = []
    for i in range(len(woord)):
        if woord[i] == letter:
            lijst.append(i)
    return lijst