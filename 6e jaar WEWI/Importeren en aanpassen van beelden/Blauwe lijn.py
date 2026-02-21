from PIL import Image

def lijn(pad):
    
    # Open de afbeelding
    origineel = Image.open(pad)

    # Maak een kopie van de originele afbeelding en toon deze
    aangepast = origineel

    # Toon de originele afbeelding
    aangepast.show()

    # Haal de breedte en hoogte op
    breedte, hoogte = aangepast.size

    # Teken een blauwe lijn op de 10e rij (index 9)
    for x in range(breedte):
        aangepast.putpixel((x, 9), (0, 0, 255))

    # Toon de aangepaste afbeelding
    aangepast.show()
