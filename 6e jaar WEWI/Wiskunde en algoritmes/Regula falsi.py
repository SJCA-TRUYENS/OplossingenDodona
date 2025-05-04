#Maakt een functievoorschrift
def f(x):
    return x**3 - 7*x**2 + 11

#Startgrenzen en tolerantie ingeven
links = float(input("Geef de linkse grens op: "))
rechts = float(input("Geef de rechtse grens op: "))
tolerantie = float(input("Geef de gewenste tolerantie op: "))

xsnijpunt = (links*f(rechts)-rechts*f(links))/(f(rechts)-f(links))
ysnijpunt = f(xsnijpunt)

while abs(ysnijpunt) > tolerantie:
    #Is de functiewaarde strikt positief
    if ysnijpunt > 0:
        #De nulwaarde zit in het linkse deel
        rechts = xsnijpunt
    else:
        #De nulwaarde zit in het rechtse deel 
        links = xsnijpunt
        
    #Nieuw snijpunt berekenen
    xsnijpunt = (links*f(rechts)-rechts*f(links))/(f(rechts)-f(links))
    ysnijpunt = f(xsnijpunt)

print("De nulwaarde bedraagt", round(xsnijpunt, 5))