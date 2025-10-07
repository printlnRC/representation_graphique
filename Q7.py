from Q6 import dichotomie
from matplotlib.pyplot import plot, show, title, grid # Imprtation de plot, show et title de matplotlib.pyplot
from numpy import linspace, sqrt # Importation de linspace et sqrt de numpy


def P(u):
    return 2 / sqrt(u) - 3 - 4 * u**3 # Fonction dérivée de la puissance

racine = dichotomie(P, 0.01, 1) 
print(f"Racine de P(u) sur [0.01, 1] : u = {racine}")


grid()
title("Evolution de la puissance") # Titre du graphique


u = linspace(0, 1, 100) # u est défini entre 0 et 1 avec 100 points

plot(u, P(u)) # Tracé de la fonction puissance
plot(racine, P(racine), 'ro')  # Marque la racine trouvée en rouge
show() # Affichage du graphique