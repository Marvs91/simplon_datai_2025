# Écrivez un programme qui demande à l'utilisateur de deviner un nombre secret (par exemple 42). Le programme indique à l'utilisateur si le nombre à deviner est plus grand ou plus petit que sa proposition et continue de demander un nombre tant que l'utilisateur ne trouve pas le nombre secret. Une fois que l'utilisateur trouve le nombre secret, affichez un message de félicitations.

while True:
    x = int( input("Veuillez saisir le chiffre correct") )

    if(x==42):

        print("Félicitations vous avez trouvé le chiffre secret")
        break
