def tel_positieve_getallen(getallen_lijst):
    aantal_positief = 0
    for getal in getallen_lijst:
        if getal > 0:
            aantal_positief += 1
    print("De lijst bevat " + str(aantal_positief) + " positieve getallen.")