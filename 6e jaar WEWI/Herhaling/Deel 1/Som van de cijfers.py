getal = int(input("Geef een natuurlijk getal (kleiner dan 1000) op: "))

honderdtallen = getal // 100
tientallen = (getal - honderdtallen * 100) // 10
eenheden =  getal - honderdtallen * 100 - tientallen * 10

som = honderdtallen + tientallen + eenheden

print(som)