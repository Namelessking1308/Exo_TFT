from random import randint

hasard = randint(1, 5)

print("Deviner le nombre entre 1-5\n")
deviner = int(input("Entrez un nombre:\n"))

if hasard != deviner:
    print("Mauvaise réponse !")
    if hasard > deviner:
        print("C'est plus...")
    else:
        print("C'est moins...")

print("Dernière chance...")
deviner = int(input("Entrez un nombre:\n"))

if hasard == deviner:
    print(f"C'était le Bon chiffre ! |{deviner}|")
else:
    print("Perdu...")