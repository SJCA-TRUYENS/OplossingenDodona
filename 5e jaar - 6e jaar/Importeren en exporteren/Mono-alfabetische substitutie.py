alfabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

vervangalfabet = [
    "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d",
    "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"
]

bestand = open("boodschap.txt", "r", encoding="utf-8")
tekst = bestand.read()
bestand.close()

versleutelde_tekst = ""

for teken in tekst:
    if teken in alfabet:
        plaats = alfabet.index(teken)
        versleutelde_tekst += vervangalfabet[plaats]
    else:
        versleutelde_tekst += teken

bestand = open("versleuteld.txt", "w", encoding="utf-8")
bestand.write(versleutelde_tekst)
bestand.close()
