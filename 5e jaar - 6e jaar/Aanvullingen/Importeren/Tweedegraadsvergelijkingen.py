import math

a = float(input("In ax² + bx + c = 0, geef de waarde van a op: "))
b = float(input("In ax² + bx + c = 0, geef de waarde van b op: "))
c = float(input("In ax² + bx + c = 0, geef de waarde van c op: "))

D = b ** 2 - 4 * a * c

if D > 0:
    x1 = (-1 * b - math.sqrt(D)) / (2 * a)
    x2 = (-1 * b + math.sqrt(D)) / (2 * a)
    print("x =", x1, "of x =", x2)
    
elif D == 0:
    x1 = (-1 * b) / (2 * a)
    print("x =", x1)
else:
    print("Geen nulwaarden")