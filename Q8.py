from Q6 import dichotomie
from numpy import sqrt # Importation de sqrt de numpy


a = 0.1

while a >= 10*10**-10:
    def P(u):
        return 2 / sqrt(u) - 3 - 4 * u**3 # Fonction dérivée de la puissance

    racine = dichotomie(P, 0.01, 1, a) 
    print(f"Racine de P(u) à la pression {a} : u = {racine}")
    a = a/10