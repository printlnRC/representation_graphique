from numpy import sqrt

def dichotomie(f, a0, b0, epsilon=1e-6, max_iter=100):
    """
    Recherche une racine de f(x)=0 dans [a0, b0] par dichotomie.
    Arrête lorsque l'intervalle est plus petit que epsilon.
    """
    an, bn = a0, b0
    for  in range(max_iter):
        cn = (an + bn) / 2
        if abs(bn - an) < epsilon:
            return cn
        if f(an) * f(cn) > 0:
            an = cn
        else:
            bn = cn
    return (an + bn) / 2  


def P(u):
    return 4 * sqrt(u) - 3 * u - u**4 # Fonction puissance

racine = dichotomie(P, 0.01, 1) 
print(f"Racine de P(u) sur [0.01, 1] : u = {racine}")