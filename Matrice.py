def menu():
    print('''
       --- Matrice ---
    1) Déterminez le déterminant d'une matrice
    2) Calculer la Matrice inverse.
    3) Déterminant et Matrice inverse
    4) Déterminez la Matrice de Gram.

    5) Quittez
			''')
    choix = int(input())

    if (choix == 1):
        m = def_matrix()
        print("Le Determinant de la matrice est " + str(getMatrixDeternminant(m)))
        print("\n Continuer...")
        hub = input()
        menu()

    if (choix == 2):
        m = def_matrix()
        print("La matrice inverse est " + str(getMatrixInverse(m)))
        print("\n Continuer...")
        hub = input()
        menu()

    if (choix == 3):
        m = def_matrix()
        print("Le Determinant de la matrice est " + str(getMatrixDeternminant(m)))
        if (getMatrixDeternminant(m) >= 0):
            print("La matrice inverse est " + str(getMatrixInverse(m)))
        else:
            print("La matrice n'est pas inversible")
        print("\n Continuer...")
        hub = input()
        menu()

    if (choix == 4):
        m = def_matrix()
        print("\n Continuer...")
        hub = input()
        menu()

    if (choix == 5):
        exit()

def def_matrix():
    print("Definition de la taille de la matrice.")
    print("Combien il y a t-il de ligne ?")
    row = int(input())
    print("Combien il y a t-il de colonne ?")
    collum = int(input())
    matrix = [0] * row
    for build in range(0, row, 1):
        matrix[build] = [0] * collum
    for i in range(0, row, 1):
        for j in range(0, collum, 1):
            print("Valeur de M" + str(i) + "," + str(j))
            matrix[i][j] = float(input())
    print(matrix)
    return matrix

def getMatrixMinor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def getMatrixDeternminant(m):
    # base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1) ** c) * m[0][c] * getMatrixDeternminant(getMatrixMinor(m, 0, c))
    return determinant

def transposeMatrix(m):
    return map(list,zip(*m))

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],[-1*m[1][0]/determinant, m[0][0]/determinant]]
    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = list(transposeMatrix(cofactors))
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

menu()