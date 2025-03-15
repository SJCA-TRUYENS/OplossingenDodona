woord = input("Geef een woord op: ")
letter = input("Geef een letter op: ")
antwoord = ""

for symbool in woord:
    if symbool != letter:
        antwoord += symbool
    
print(antwoord)