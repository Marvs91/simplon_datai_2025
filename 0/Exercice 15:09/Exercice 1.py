# Faire un générateur de nombre aléatoire pour le loto et l'euromillion. Attention c’est un tirage aléatoire sans remise (c.a.d que la boule trouvée n’est pas remise en jeu) et tous les chiffres ont la même probabilité d’apparaître.

import numpy as np 

# Générer une liste de nombre aléatoire 
loto_aleatoire = np.random.choice(range(1, 50), size = 5, replace = False)
euro_million_aleatoire = np.random.choice(range(1, 50), size = 5, replace = False)
etoiles_numerotes = np.random.choice(range(1, 12), size= 2, replace = False)

# Resultat chiffres aléatoires 
resultats_euro_million = np.array(euro_million_aleatoire)
resultats_loto = np.array(loto_aleatoire)
resultats_etoiles = np.array(etoiles_numerotes)

# Afficher les chiffres aléatoires loto, euromillions, étoiles numérotés 
print(f"Les numéros de l'euromillions sont", resultats_euro_million)
print(f"Les numéros du loto sont", resultats_loto)
print(f"Les résultats étoiles sont", resultats_etoiles)