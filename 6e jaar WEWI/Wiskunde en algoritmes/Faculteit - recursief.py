getal = int(input("Geef een natuurlijk getal op: "))

def faculteit(factor):
    if factor == 1:
        return 1
    
    tussenresultaat = factor * faculteit(factor - 1)
    return tussenresultaat

antwoord = faculteit(getal)
print(str(getal)+"! =", antwoord)