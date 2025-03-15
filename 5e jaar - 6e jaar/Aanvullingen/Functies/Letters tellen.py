def telLetters(woord, letter):
    counter = 0
    for l in woord:
        if l == letter :
            counter += 1
    return counter