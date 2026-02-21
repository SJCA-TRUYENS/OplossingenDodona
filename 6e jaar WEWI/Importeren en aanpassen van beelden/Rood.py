from PIL import Image

def rood(pad):
    # Open de afbeelding
    afbeelding = Image.open(pad)

    # Toon de originele afbeelding
    afbeelding.show()

    # Haal de breedte en hoogte op
    breedte, hoogte = afbeelding.size

    # Itereer over elke pixel
    for x in range(breedte):
        for y in range(hoogte):
            # Haal de RGB-waarde op
            r, g, b, a = afbeelding.getpixel((x, y))
            # Pas de pixel aan naar enkel rood
            afbeelding.putpixel((x, y), (r, 0, 0))

    # Toon de aangepaste afbeelding
    afbeelding.show()
