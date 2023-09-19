# Créez une fonction qui prend un tableau NumPy en entrée et renvoie la moyenne, la médiane et l'écart type de ses éléments.

import numpy as np 
# Création d'un tableau NumPy 
tab = np.array([3,7,12,15,23,29])

# Calcul de la moyenne
moyenne = np.mean(tab)

# Calcul de la médiane 
mediane = np.median(tab)

# Calcul de l'écart type 
ecart_type = np.std(tab)

# Affichage des résultats 
print("Moyenne", moyenne)
print("Médiane", mediane)
print("Ecart-type", ecart_type)

