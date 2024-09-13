# a, b en c stellen opeenvolgende waarden voor uit de Fibonacci-reeks
# a, b, c zijn in oplopende volgorde gekozen
a = 1
b = 1
c = a + b

testwaarde = int(input("Welke waarde wil je controleren? "))

#Controle van c. De startwaarde van c is 2, dit komt overeen met de derde term
teller = 3

while c < testwaarde:
    # Alle waarden schuiven één plaats op naar rechts
    # De volgorde wordt hierdoor wel behouden
    a = b
    b = c
    c = a + b
    
    teller += 1

if c == testwaarde:
    print(teller)
else:
    print("Geen getal uit de reeks van Fibonacci!")