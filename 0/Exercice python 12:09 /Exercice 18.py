# Écrivez une fonction qui prend une liste de nombres en entrée et renvoie une nouvelle liste contenant uniquement les nombres positifs en utilisant une boucle "while".

def filtrer_nombres_positifs(liste):
    i = 0
    resultats = []  # Liste pour stocker les nombres positifs
    while i < len(liste):
        if liste[i] > 0:
            resultats.append(liste[i])
        i += 1
    return resultats

# Exemple d'utilisation de la fonction avec une liste de nombres :
liste_de_nombres = [1, -2, 3, -4, 5, -6]
nombres_positifs = filtrer_nombres_positifs(liste_de_nombres)
print(nombres_positifs)
