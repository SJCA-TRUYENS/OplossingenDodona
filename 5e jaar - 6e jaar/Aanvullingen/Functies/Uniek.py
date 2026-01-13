def uniek(originele_lijst):
    unieke_elementen = []
    for element in originele_lijst:
        if element not in unieke_elementen:
            unieke_elementen.append(element)
    return unieke_elementen