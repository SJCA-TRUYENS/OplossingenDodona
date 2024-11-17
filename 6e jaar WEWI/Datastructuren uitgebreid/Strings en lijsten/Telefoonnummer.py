nummer = input("Geef een telefoonnummer in: ")
antwoord = "+32 " + nummer[1:4] + " " + nummer[4:7] + " " + nummer[7:]
print(antwoord)