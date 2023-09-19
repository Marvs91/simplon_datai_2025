# Écrivez une fonction qui prend une chaîne de caractères en entrée et renvoie une nouvelle chaîne où chaque mot est en majuscules.

# Nouvelle chaine en majuscule 
def func(phrase):
    new_maj = phrase.upper()
    return new_maj

# Chaine de caractère en entrée 
phrase = ("boa tarde")

# Afficher nouvelle chaine 
print(func(phrase))