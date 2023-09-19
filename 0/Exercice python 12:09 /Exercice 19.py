# Écrivez une fonction qui prend une liste de mots en entrée et renvoie une nouvelle liste contenant les mots dont la première lettre est une voyelle (a, e, i, o, u) en utilisant une boucle "while".

def mots_commencant_par_voyelle(liste_de_mots):
    i = 0
    mots_voyelles = []  # Liste pour stocker les mots commençant par une voyelle
    voyelles = ['a', 'e', 'i', 'o', 'u']
    
    while i < len(liste_de_mots):
        mot = liste_de_mots[i]
        if mot[0].lower() in voyelles:  
            mots_voyelles.append(mot)
        i += 1
    
    return mots_voyelles

# Utilisation de la fonction avec une liste de mots :
liste_de_mots = ['Abricot', 'Banane', 'Carotte', 'Orange', 'Pomme', 'Kiwi']
mots_voyelles = mots_commencant_par_voyelle(liste_de_mots)
print(mots_voyelles)
