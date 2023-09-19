# Écrivez une fonction qui prend une chaîne de caractères en entrée et renvoie True si cette chaîne est un palindrome (c'est-à-dire qu'elle se lit de la même manière de gauche à droite et de droite à gauche), sinon renvoie False

def func(a):
  
        return True if a == a[::-1] else False

    
out = func("2002") 
print(out)