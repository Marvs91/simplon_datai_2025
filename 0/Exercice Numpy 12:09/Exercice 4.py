# Créez une fonction qui prend deux tableaux NumPy en entrée et renvoie le produit scalaire de ces deux tableaux (dot product).

import numpy as np 

# Création des tableaux NumPy 

tab_1 = np.array([1,3,5,7,9])
tab_2 = np.array([2,4,6,8,10])

# Produit scalaire des deux tableaux 

resultat = np.dot(tab_1, tab_2)

# Résultat des deux produits scalaire 

print("Produit scalaire des deux tableaux", resultat)
