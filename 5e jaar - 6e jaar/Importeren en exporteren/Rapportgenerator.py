bestand = open("punten.txt", "r", encoding="utf-8")
regels = bestand.readlines()
bestand.close()

rapport = ""

for regel in regels:
    naam = ""
    score_tekst = ""
    score_lezen = False

    for teken in regel:
        if teken == " ":
            score_lezen = True
        elif teken != "\n":
            if score_lezen:
                score_tekst += teken
            else:
                naam += teken

    score = int(score_tekst)

    if score >= 10:
        resultaat = "geslaagd"
    else:
        resultaat = "niet geslaagd"

    if rapport != "":
        rapport += "\n"
    rapport += naam + ": " + resultaat

bestand = open("rapport.txt", "w", encoding="utf-8")
bestand.write(rapport)
bestand.close()
