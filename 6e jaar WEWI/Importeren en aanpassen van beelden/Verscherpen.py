from PIL import Image

#Stap 1
def grijswaarden(afb):
    breedte, hoogte = afb.size
    for x in range(0, breedte):
        for y in range(0, hoogte):
            r, g, b, a = afb.getpixel((x, y))
            gemiddelde = (r + g + b) // 3
            afb.putpixel((x, y), (gemiddelde, gemiddelde, gemiddelde, a))
    return afb


afbeelding = Image.open(r"C:\Users\Dries.Truyens\OneDrive - VZW Arcadia\Bureaublad\afbeeldingICW.png")
if afbeelding.mode != 'RGBA':
    afbeelding = afbeelding.convert('RGBA')

afbeeldingGrijs = grijswaarden(afbeelding.copy())
#Stap 1

#Stap 2
breedte, hoogte = afbeeldingGrijs.size
afbeeldingNieuw = Image.new("RGBA", (breedte, hoogte))

for y in range(0, hoogte):
    afbeeldingNieuw.putpixel((0, y), afbeeldingGrijs.getpixel((0, y)))
    afbeeldingNieuw.putpixel((breedte-1, y), afbeeldingGrijs.getpixel((breedte-1, y)))

for x in range(0, breedte):
    afbeeldingNieuw.putpixel((x, 0), afbeeldingGrijs.getpixel((x, 0)))
    afbeeldingNieuw.putpixel((x, hoogte-1), afbeeldingGrijs.getpixel((x, hoogte-1)))
#Stap 2
    
#Stap 3    
for x in range(1, breedte - 1):
    for y in range(1, hoogte - 1):
        # Filter: [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
        
        waarde_na_filter = (
            -1 * afbeeldingGrijs.getpixel((x, y - 1))[0] +
            -1 * afbeeldingGrijs.getpixel((x - 1, y))[0] +
            5 * afbeeldingGrijs.getpixel((x, y))[0] +
            -1 * afbeeldingGrijs.getpixel((x + 1, y))[0] +
            -1 * afbeeldingGrijs.getpixel((x, y + 1))[0]
        )
        
        # Clamp value to be in 0-255 range
        waarde = max(0, min(waarde_na_filter, 255))
        
        afbeeldingNieuw.putpixel((x, y), (waarde, waarde, waarde, 255))

afbeeldingGrijs.show()
afbeeldingNieuw.show()
#Stap 3
