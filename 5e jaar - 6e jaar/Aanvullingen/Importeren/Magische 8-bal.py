import random

vraag = input("Wat is je vraag? ")
antwoord_nummer = random.randint(1,5)

if antwoord_nummer == 1:
    print("Helemaal akkoord")
elif antwoord_nummer == 2:
    print("Half akkoord")
elif antwoord_nummer == 3:
    print("geen mening")
elif antwoord_nummer == 4:
    print("Niet echt akkoord")
else:
    print("Volledig niet akkoord")