def voorraad(huidige_voorraad, gewenste_voorraad):
    aankopen = {}
    for product in gewenste_voorraad:
        if product in huidige_voorraad:
            aantal = gewenste_voorraad[product] - huidige_voorraad[product]
            if aantal > 0: 
                aankopen[product] = aantal
        else:
            aankopen[product] = gewenste_voorraad[product]
        
    return aankopen
