def eerste_X(lijst, x):
    return lijst[:x]

def laatste_X(lijst, x):
    return lijst[-x:]

def tussenin(lijst, ondergrens, bovengrens):
    return lijst[ondergrens:bovengrens+1]