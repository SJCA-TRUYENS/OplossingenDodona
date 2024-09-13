soort = input("Welke fruitsoort zal ik tellen? ")
N = int(input("Hoeveel leerlingen zullen antwoorden? "))
aantal = 0

for _ in range(0,N):
    antwoord = input("Geef je favoriete fruitsoort in: ")
    if antwoord == soort:
        aantal += 1

print(aantal)