def recept_afdrukken(naam_gerecht):
    ingredienten_lijst = []
    if naam_gerecht == "Pannenkoeken":
        ingredienten_lijst = ["250g bloem", "2 eieren", "500ml melk", "snuifje zout", "boter om te bakken"]
    elif naam_gerecht == "Spaghetti Bolognese":
        ingredienten_lijst = ["500g gehakt", "1 ui", "2 teentjes knoflook", "1 blik tomatenblokjes", "1 blikje tomatenpuree", "kruiden (oregano, basilicum)", "spaghetti"]
    elif naam_gerecht == "Caesarsalade":
        ingredienten_lijst = ["1 krop Romeinse sla", "1 kipfilet", "croutons", "Parmezaanse kaas", "caesardressing"]
    
    if ingredienten_lijst:
        print("Recept voor " + naam_gerecht + ":")
        for ingredient in ingredienten_lijst:
            print("- " + ingredient)