# Écrivez un programme qui demande à l'utilisateur de deviner le code secret,faites en sorte que le nombre à trouver soit aléatoire et compris entre 1 et 1000. Le programme indique à l'utilisateur si le nombre à deviner est plus grand ou plus petit que sa proposition et continue de demander un nombre tant que l'utilisateur ne trouve pas le nombre secret. Une fois que l'utilisateur trouve le nombre secret, affichez un message de félicitations.”

import numpy as np

# Générez un nombre aléatoire entre 1 et 1000 comme le nombre secret
nombre_secret = np.random.randint(1, 1000)

# Boucle tant que l'utilisateur n'a pas trouvé le nombre secret
while True:
    # Demande à l'utilisateur de deviner le nombre
    try:
        proposition = int(input("Devinez le nombre secret entre 1 et 1000 : "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        continue

    # Compare la proposition de l'utilisateur avec le nombre secret
    if proposition < nombre_secret:
        print("Le nombre secret est plus grand.")
    elif proposition > nombre_secret:
        print("Le nombre secret est plus petit.")
    else:
        print("Félicitations ! Vous avez trouvé le nombre secret.")
        break  # Sort de la boucle lorsque le nombre secret est trouvé

