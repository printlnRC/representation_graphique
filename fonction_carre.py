from matplotlib.pyplot import plot, show, title # Imprtation de plot, show et title de matplotlib.pyplot
from numpy import linspace, sqrt # Importation de linspace et sqrt de numpy



title("Evolution de la puissance") # Titre du graphique


u = linspace(0, 1, 100) # u est défini entre 0 et 1 avec 100 points

def P(u):
    return 4 * sqrt(u) - 3 * u - u**4 # Fonction puissance


plot(u, P(u)) # Tracé de la fonction puissance
show() # Affichage du graphique
