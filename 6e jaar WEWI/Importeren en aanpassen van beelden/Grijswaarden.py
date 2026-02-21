from PIL import Image

def grijswaarden(pad):
    afbeelding = Image.open(pad)
    afbeelding.show()
    
    breedte, hoogte = afbeelding.size
    
    for x in range(breedte):
        for y in range(hoogte):
            r, g, b, a = afbeelding.getpixel((x, y))
            gemiddelde = (r + g + b) // 3
            afbeelding.putpixel((x, y), (gemiddelde, gemiddelde, gemiddelde))

    afbeelding.show()
