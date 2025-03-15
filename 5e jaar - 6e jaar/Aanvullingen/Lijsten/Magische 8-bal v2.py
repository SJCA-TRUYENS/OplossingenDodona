import random
lijst_antwoorden = ["Helemaal akkoord", "Half akkoord", "geen mening", "Niet echt akkoord", "Volledig akkoord"]
vraag = input("Wat is je vraag? ")
antwoord = random.choice(lijst_antwoorden)
print(antwoord)