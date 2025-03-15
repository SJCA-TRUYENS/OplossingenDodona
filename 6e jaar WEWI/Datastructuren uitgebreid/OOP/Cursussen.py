class Cursus:
    def __init__(self, naam, docent, studiepunten):
        self.naam = naam
        self.docent = docent
        self.studiepunten = studiepunten

class Student:
    def __init__(self, naam):
        self.naam = naam
        self.cursussen = []

    def registreer_cursus(self, cursus):
        self.cursussen.append(cursus)

    def toon_cursussen(self):
        return [cursus.naam for cursus in self.cursussen]

    def toon_docenten(self):
        docentenLijst = []
        for cursus in self.cursussen:
            if cursus.docent not in docentenLijst:
                docentenLijst.append(cursus.docent)
        return docentenLijst

    def toon_studiepunten(self):
        return sum(cursus.studiepunten for cursus in self.cursussen)