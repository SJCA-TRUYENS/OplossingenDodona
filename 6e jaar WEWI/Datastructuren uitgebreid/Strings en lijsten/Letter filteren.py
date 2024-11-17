def letter_filteren(lijst, letter):
    nieuwe_lijst = [x for x in lijst if letter in x]
    return nieuwe_lijst
