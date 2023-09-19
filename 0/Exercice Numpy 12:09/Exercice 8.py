# Créez une fonction qui prend un tableau NumPy en entrée et renvoie un nouveau tableau où tous les éléments inférieurs à 5 sont remplacés par 0 et tous les éléments supérieurs ou égaux à 5 sont remplacés par 1.

import numpy as np

# Création du tableau NumPy
tab = np.array([3, 7, 12, 15, 23, 29])

# Remplacer les éléments inférieurs à 5 par 0 et les éléments supérieurs ou égaux à 5 par 1
nouveau_tab = np.where(tab < 5, 0, 1)

# Affichage du nouveau tableau
print(nouveau_tab)
