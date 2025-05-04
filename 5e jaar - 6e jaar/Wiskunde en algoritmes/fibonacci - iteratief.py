nummer = int(input("Het hoeveelste getal uit de rij van Fibonacci wil je? "))

kleinste = 0
grootste = 1
aantal = 2

if nummer == 1:
    antwoord = kleinste
if nummer == 2:
    antwoord = grootste

while aantal < nummer:
    aantal += 1
    som = kleinste + grootste
    kleinste = grootste
    grootste = som
    

antwoord = grootste
print("Het " + str(nummer) + "e getal uit de rij van Fibonacci is", antwoord)