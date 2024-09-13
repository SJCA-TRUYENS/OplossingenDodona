som = 0
antwoord = input("Geef een waarde in of 'Stop': ")

while antwoord != "Stop":
    waarde = int(antwoord)
    som += waarde
    antwoord = input("Geef een waarde in of 'Stop': ")

print(som)