def stukken_fruit(fruitmand):
    totaal = 0
    for fruitsoort in fruitmand:
        totaal += fruitmand[fruitsoort]
        
    return totaal