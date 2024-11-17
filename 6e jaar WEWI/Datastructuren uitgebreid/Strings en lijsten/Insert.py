def insert_value(index, waarde, lijst):
    linkerdeel = lijst[:index]
    linkerdeel.append(waarde)
    rechterdeel = lijst[index:]
    return linkerdeel+rechterdeel

print(insert_value(4, 15, [1, 2, 3, 4, 5]))