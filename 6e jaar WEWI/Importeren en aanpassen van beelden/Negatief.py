from PIL import Image

def negatief(pad):
    afbeelding = Image.open(pad)
    afbeelding.show()
    
    breedte, hoogte = afbeelding.size
    
    for x in range(breedte):
        for y in range(hoogte):
            r, g, b, a = afbeelding.getpixel((x, y))
            afbeelding.putpixel((x,y), (255-r, 255-g, 255-b, a))

    afbeelding.show()