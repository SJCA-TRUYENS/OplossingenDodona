alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
bestand = open("opgave.txt")
tekst = bestand.read()
bestand.close()

eerste_woord = ""
i = 0
while i < len(tekst) and tekst[i] in alfabet:
    eerste_woord += tekst[i]
    i += 1

print(eerste_woord)