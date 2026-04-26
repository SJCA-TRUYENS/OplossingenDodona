regels = [
    "Maandag: informatica",
    "Dinsdag: wiskunde",
    "Woensdag: Nederlands",
    "Donderdag: geschiedenis",
    "Vrijdag: informatica",
]

bestand = open("weekplanning.txt", "w")
for regel in regels:
    bestand.write(regel)
    if regel != regels[-1]:
        bestand.write("\n")
bestand.close()
