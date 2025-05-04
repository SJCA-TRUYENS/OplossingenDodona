getal = int(input("Geef een natuurlijk getal op: "))

antwoord = 1
for waarde in range(1, getal+1):
    antwoord *= waarde

print(str(getal)+"! =", antwoord)