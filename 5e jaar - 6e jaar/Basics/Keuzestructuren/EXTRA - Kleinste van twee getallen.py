a = int(input("Het eerste gehele getal: "))
b = int(input("Het tweede gehele getal: "))
c = int(input("Het derde gehele getal: "))

if a < b and a < c:
    kleinste = a
elif b < a and b < c:
    kleinste = b
else:
    kleinste = c

print(kleinste)