class Kluis:
    def __init__(self):
        self.__code = "1234"  # Privé-attribuut met standaardcode

    def wijzig_code(self, nieuwe_code, oude_code):
        if oude_code == self.__code:
            self.__code = nieuwe_code

    def open_kluis(self, ingevoerde_code):
        if ingevoerde_code == self.__code:
            return "Kluis geopend!"
        else:
            return "Foute code, toegang geweigerd."
