# Écrivez un programme qui demande à l'utilisateur de saisir un mot et affiche si ce mot contient plus de 5 caractères en utilisant une boucle "while".

def main():
    mot = input("Entrez un mot : ")  # Demande à l'utilisateur de saisir un mot
    longueur = 0  # Initialisation de la longueur du mot
    i = 0  # Initialisation de l'indice pour parcourir le mot

    while i < len(mot):
        longueur += 1  
        i += 1

    if longueur > 5:
        print("Le mot contient plus de 5 caractères.")
    else:
        print("Le mot ne contient pas plus de 5 caractères.")

if __name__ == "__main__":
    main()
