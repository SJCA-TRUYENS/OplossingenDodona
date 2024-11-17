def letters_tellen(pad):
    letter_lijst = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letter_dictionary = {}

    bestand = open(pad)
    tekst = bestand.read()
    lowercase_tekst = tekst.lower()
    
    for letter in lowercase_tekst:
        if letter in letter_lijst:
            if letter in letter_dictionary:
                letter_dictionary[letter] += 1
            else:
                letter_dictionary[letter] = 1
    return letter_dictionary

print(letters_tellen(r"C:\Users\sjca.be\Documents\GitHub\dodona_oefeningen\exercises\6e jaar\Datastructuren uitgebreid\Dictionaries\Letters tellen\workdir\opgave.txt"))