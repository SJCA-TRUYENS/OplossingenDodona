def MAS(tekst, alfabet):
    # Maak de tekst volledig lowercase
    tekst = tekst.lower()
    
    # Maak de dictionary die de letters met elkaar verbindt
    letters_lijst = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letter_dict = {}
    for num in range(len(letters_lijst)):
        letter_dict[letters_lijst[num]] = alfabet[num]
    
    # Gebruik de dictionary om MAS uit te voeren
    gecodeerde_tekst = ""
    for symbool in tekst:
        if symbool in letter_dict:
            gecodeerde_tekst += letter_dict[symbool]
        else:
            gecodeerde_tekst += symbool
            
    return gecodeerde_tekst