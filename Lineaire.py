# Library
import math

def menu():
    print('''
    --- Maths ---
    1) Moyenne / Variance
    2) Calculer la Covariance / Correlation.
    3) Calculer l'estimation d'un vecteur.
    4) Calculez SCT, SCM, SCR
    5) All (SC,Moy, Var,B̂,µ,Cov,Cor,R²,regression)
    
    --- Modele Lineaire ---
    6) Calculez B̂ et µ + Cov et Cor
    7) Calculer l'équation de la droite de regression.
    8) Calculer le Coefficient de determination R².
    9) Calculez les estimations du modèle d’ANOVA

    --- Intervalle ---
    10) Calculer l'intervalle de confiance d'un estimateur.

    11) Quittez
			''')

    choix = int(input())

    if (choix == 1):
        x = Fix_Value_x()
        print("La moyenne est " + str(moy(x)))
        print("La variance est " + str(var(x)))
        print("La variance corrige est " + str(var_corrige(x)))
        print("\n Continuer...")
        hub = input()
        menu()

    if (choix == 2):
        x = Fix_Value_y()
        y = Fix_Value_x()
        print("La Covariance est " + str(cov(x, y)))
        print("La Correlation est " + str(cor(x, y)))
        print("\n Continuer...")
        hub = input()
        menu()

    if (choix == 4):
        print("SCT est " + str(moy(x)))
        print("SCM est " + str(var(x)))
        print("\n Continuer...")
        hub = input()
        menu()

    if (choix == 4):
        x = Fix_Value_y()
        y = Fix_Value_x()
        B = Beta(x, y)
        mu = Mu(x, y)
        print("La Covariance est " + str(cov(x, y)))
        print("La Correlation est " + str(cor(x, y)))
        print("B̂ est egale a " + str(B))
        print("µ est egale a " + str(mu))
        print("\n Continuer...")
        hub = input()
        menu()

    if (choix == 5):
        if (B and mu is None):
            x = Fix_Value_y()
            y = Fix_Value_x()
            B = Beta(x, y)
            mu = Mu(x, y)
        else:
            print('''
        Modele de Regression:
        1) Regression Simple
        2) Regression exponentielle
        3) Regression logarithmique
        4) Regression multiple
			''')
            choix2 = int(input())
            if (choix2 == 1):
                print("L'équation de la droite est " + str(simple(B, mu, x)))
            if (choix2 == 2):
                print("L'équation de la droite est " + str(simple(B, mu, x)))
            if (choix2 == 3):
                print("L'équation de la droite est " + str(simple(B, mu, x)))
            if (choix2 == 4):
                print("L'équation de la droite est " + str(simple(B, mu, x)))

    if (choix == 6):
        print("R2 est " + str(R2(x, y)))
        print("\n Continuer...")
        hub = input()
        menu()

    if (choix == 11):
        exit()


def Fix_Value_y():
    print("Entrer le nombre de variable dans la serie")
    ini = int(input())
    y = [0] * ini

    for i in range(0, ini, 1):
        print("Valeur de y" + str(i + 1) + " :")
        y[i] = float(input())
    return y


def Fix_Value_x():
    print("Entrer le nombre de variable dans la serie")
    ini = int(input())
    x = [0] * ini

    for i in range(0, ini, 1):
        print("Valeur de x" + str(i + 1) + " :")
        x[i] = float(input())
    return x


def moy(x):
    return sum(x) / len(x)


def var(x):
    var = 0
    mu = moy(x)
    for i in x:
        var += (i - mu) ** 2
    return var / len(x)


def var_corrige(x):
    return (len(x) / (len(x) - 1)) * var(x)


def cov(x, y):
    sum = 0
    for i in range(0, len(x), 1):
        sum += (x[i] - moy(x)) * (y[i] - moy(y))
    return sum / len(x)


def cor(x, y):
    return cov(x, y) / (math.sqrt(var(x)) * math.sqrt(var(y)))


def SCT(x):
    sum = 0
    for i in x:
        sum += ((i - moy(x)) ** 2)
    return sum


def SCM(x):
    return SCT(x) / len(x)


def R2(x, y):
    return cor(x, y) ** 2


def Beta(x, y):
    return cov(x, y) / var(x)


def Mu(x, y):
    return moy(y) - Beta(x, y) * moy(x)


def simple(B, mu, x):
    return

menu()