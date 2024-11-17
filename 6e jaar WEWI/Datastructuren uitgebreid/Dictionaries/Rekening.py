def rekening(bestelling, menukaart):
    prijs = 0
    for item in bestelling:
        prijs += bestelling[item] * menukaart[item]
        
    return prijs
