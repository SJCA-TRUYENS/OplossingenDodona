hand = ["klaveren", "koeken", "harten", "harten", "schoppen", "harten", "harten", "harten", "koeken", "klaveren", "klaveren", "harten", "harten"]
teller = 0

for kaart in hand:
    if kaart == "harten":
        teller += 1
    
print("Er zitten", teller, "harten in je hand.")