def transponeren(matrix):
    # Aangezien er nooit een lege matrix zal worden gegeven, is een controle hierop niet nodig.
    
    rijen = len(matrix)
    kolommen = len(matrix[0])
    
    getransponeerde_matrix = []
    for j in range(kolommen):
        nieuwe_rij = []
        for i in range(rijen):
            nieuwe_rij.append(matrix[i][j])
        getransponeerde_matrix.append(nieuwe_rij)
    return getransponeerde_matrix