getal = int(input("Geef een natuurlijk getal op: "))
som = 0

while getal > 0:
    som += getal % 10
    getal = getal // 10

print(som)