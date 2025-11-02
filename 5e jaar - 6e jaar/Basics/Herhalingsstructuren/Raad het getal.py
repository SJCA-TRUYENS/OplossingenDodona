geheim_getal = 73
gok = 0 # Initialiseren met een foute waarde

while gok != geheim_getal:
    gok = int(input("Doe een gok: "))
    if gok < geheim_getal:
        print("Groter")
    elif gok > geheim_getal:
        print("Kleiner")

print("Goed geraden!")