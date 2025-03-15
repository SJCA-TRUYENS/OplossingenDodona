woord = input("Geef een woord op: ")
antwoord = ""
for letter in woord:
    antwoord += letter + letter
print(antwoord)