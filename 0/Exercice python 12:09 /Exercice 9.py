# Écrivez une fonction qui prend une liste de nombres en entrée et renvoie une nouvelle liste contenant uniquement les nombres pairs de la liste initiale.

liste_de_nombres = [3,7,10,12,15,23,29,]      # Liste de nombre 
nombres_pairs = []     # Liste vide 

for nombre in liste_de_nombres:
    if nombre %2 == 0:
        nombres_pairs.append((nombre))
       
print(nombres_pairs)