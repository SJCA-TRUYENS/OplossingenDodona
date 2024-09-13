a = int(input("Het eerste gehele getal: "))
b = int(input("Het tweede gehele getal: "))

if a > 0 and b < 0:
    antwoord = "EXACT 1 POSITIEF"
elif a < 0 and b > 0:
    antwoord = "EXACT 1 POSITIEF"    
else:
    antwoord = "NIET VOLDAAN"

print(antwoord)