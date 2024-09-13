def som(lijst):
    antwoord = 0
    for waarde in lijst:
        antwoord += waarde
    return antwoord

print(som([1,2,3,4,5]))