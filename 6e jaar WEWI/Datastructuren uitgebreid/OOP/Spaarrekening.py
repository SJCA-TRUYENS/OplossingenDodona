class Spaarrekening:
    def __init__(self, pincode):
        self.__saldo = 0  # Privé-attribuut met startsaldo 0
        self.__pincode = pincode  # Privé-attribuut voor pincode

    def stort(self, bedrag):
        """Voegt geld toe aan de rekening."""
        if bedrag > 0:
            self.__saldo += bedrag

    def opnemen(self, bedrag, pincode):
        """Neemt geld op als de pincode correct is en er voldoende saldo is."""
        if pincode != self.__pincode:
            print("Foute pincode!")
            return
        if bedrag > self.__saldo:
            print("Onvoldoende saldo!")
            return
        self.__saldo -= bedrag

    def saldo_opvragen(self, pincode):
        """Toont het saldo als de juiste pincode wordt ingevoerd."""
        if pincode == self.__pincode:
            return f"Saldo: {self.__saldo} euro"
        else:
            return "Foute pincode!"