woordenlijst = ["appel", "banaan", "computer", "democratie", "encyclopedie", "fiets", "geschiedenis", "huis", "ijs", "jas", "kat", "lamp", "muis", "noot", "olifant", "paard", "quiz", "raket", "stoel", "tafel", "uil", "vis", "web", "xylofoon", "yoghurt", "zebra", "auto", "boot", "clown", "dier", "eten", "fluit", "gitaar", "hond", "inkt", "jacht", "kasteel", "leeuw", "maan", "neus", "oog", "pen", "quinoa", "roos", "schaap", "trein", "uniform", "vliegtuig", "wol", "xenon", "yeti", "zeep", "boek", "dans", "elf", "film", "gras", "haard", "ijsbeer", "jungle", "kikker", "lucht", "zee", "ster", "planeet", "universum", "melkweg", "sterrenstelsel", "nevel", "komeet", "meteoor", "astronaut", "kosmonaut", "ruimteschip", "satelliet", "telescoop", "observatorium", "zwaartekracht", "lichtsnelheid", "atoom", "molecuul", "element", "proton", "neutron", "elektron", "quark", "boson", "lepton", "foton", "gluon", "zwaartekrachtsgolf", "singulariteit", "wormgat", "multiversum", "dimensie"]
minimum_lengte = int(input("Geef een minimum aantal karakters op: "))
aantal_lange_woorden = 0

for woord in woordenlijst:
    if len(woord) >= minimum_lengte:
        aantal_lange_woorden += 1

print("Er zijn", aantal_lange_woorden, "lange woorden in de lijst.")