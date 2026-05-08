# 7. Implémentez une fonction inverser_chaine() qui prend une chaîne de caractères en entrée et retourne cette chaîne
# inversée

def inverser_chaine():
    chaine = input("Entrez une chaîne de caractère à inverser: ")
    return chaine[:: -1]

a = inverser_chaine()
print(a)