class Auto:
    def __init__(self, tankinhoud):
        self.tankinhoud = tankinhoud

    def tank_vullen(self, hoeveelheid):
        self.tankinhoud += hoeveelheid

class Tankstation:
    def tank_auto(self, auto, hoeveelheid):
        auto.tank_vullen(hoeveelheid)