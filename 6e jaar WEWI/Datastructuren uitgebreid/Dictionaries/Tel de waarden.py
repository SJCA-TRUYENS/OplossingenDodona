lijst = ["appel", "peer", "appel", "banaan", "banaan", "peer", "kers", "appel", "peer", "kers", "appel"]
dictionary = {}


for fruit in lijst:
    if fruit in dictionary:
        dictionary[fruit] += 1
    else:
        dictionary[fruit] = 1

print(dictionary)