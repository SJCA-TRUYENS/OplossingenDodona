aantal = int(input("Hoeveel dagen wil je overslaan: "))

rest = aantal % 7

if rest == 0:
    print("maandag")
elif rest == 1:
    print("dinsdag")
elif rest == 2:
    print("woensdag")
elif rest == 3:
    print("donderdag")
elif rest == 4:
    print("vrijdag")
elif rest == 5:
    print("zaterdag")
else :
    print("zondag")