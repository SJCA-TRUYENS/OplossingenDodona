nummer = int(input("Het hoeveelste getal uit de rij van Fibonacci wil je? "))

def fibonacci(getal):
    if getal == 1:
        return 0
    if getal == 2:
        return 1
    
    tussenresultaat = fibonacci(getal - 1) + fibonacci(getal - 2)
    return tussenresultaat

print("Het " + str(nummer) + "e getal uit de rij van Fibonacci is", fibonacci(nummer))