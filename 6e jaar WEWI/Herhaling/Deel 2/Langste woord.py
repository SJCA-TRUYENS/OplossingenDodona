bestand = open(r"C:\Users\sjca.be\Desktop\opgave.txt")
tekst = bestand.read()

huidig_woord = ""
langste_woord = ""

for symbool in tekst:
    if not(symbool == " " or symbool == "."): 
        huidig_woord = huidig_woord + symbool
    elif len(huidig_woord) > len(langste_woord):
        langste_woord = huidig_woord
        huidig_woord = ""
    else:
        huidig_woord = ""

print(langste_woord)
bestand.close()