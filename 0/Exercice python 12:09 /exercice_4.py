#Écrivez une fonction qui prend un nombre entier en entrée et affiche si ce nombre est positif, négatif ou nul.

nombre = 24 

def check(n):
    
#Si le nombre est positif 
    if n > 0: 
        print("positif")

#Si le nombre est négatif 
    elif n < 0:
        print("negatif")

#Si le nombre est égal à zero 
    else:
        print("zéro")