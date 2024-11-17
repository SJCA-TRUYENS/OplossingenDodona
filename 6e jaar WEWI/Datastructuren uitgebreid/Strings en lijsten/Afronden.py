teller = int(input("Wat is de teller? "))
noemer = int(input("Wat is de noemer? "))
afronding = int(input("Hoeveel decimalen wenst u? "))

antwoord = teller/noemer

print(f"{antwoord:.{afronding}f}")