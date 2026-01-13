import random

aantal = int(input("Hoeveel dobbelstenen wil je rollen? "))
dobbelstenen = []

for i in range(aantal):
    dobbelstenen.append(random.randint(1, 6))

print(dobbelstenen)