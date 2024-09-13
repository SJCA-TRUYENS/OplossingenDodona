N = int(input("Hoeveel leerlingen zullen antwoorden? "))
aantal = 0

for _ in range(0,N):
    antwoord = input("Geef je favoriete fruitsoort in: ")
    if antwoord == "appel":
        aantal += 1

print(aantal)