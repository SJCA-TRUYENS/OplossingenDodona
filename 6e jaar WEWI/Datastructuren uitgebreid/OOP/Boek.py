class Boek:
    def __init__(self, titel, auteur, prijs):
        self.titel = titel
        self.auteur = auteur
        self.prijs = prijs

    def korting_toepassen(self, korting_percentage):
        self.prijs -= self.prijs * (korting_percentage / 100)
        print(round(self.prijs, 2))  # Afronden tot 2 decimalen voor nettere uitvoer