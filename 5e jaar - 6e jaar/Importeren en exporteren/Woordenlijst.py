alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
pad = "opgave.txt"

bestand = open(pad)
tekst = bestand.read()
bestand.close()

woordenlijst = []
huidig_woord = ""
for karakter in tekst:
    if karakter in alfabet:
        huidig_woord += karakter
    else:
        if huidig_woord:
            woordenlijst.append(huidig_woord)
            huidig_woord = ""

if huidig_woord:
    woordenlijst.append(huidig_woord)

print(woordenlijst)