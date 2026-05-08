# 6. Créez une fonction nombres_pairs_impairs() qui prend une liste de nombres en entrée et retourne deux listes
# distinctes, l'une contenant les nombres pairs et l'autre les nombres impairs.

def nombres_pairs_impairs():
    nb = [21, 22, 13, 14, 18, 19, 17, 16]

    pairs = []
    impairs = []

    for i in nb:
        if i % 2 == 1:
            impairs.append(i)
        else:
            pairs.append(i)

    return pairs, impairs
        
a = nombres_pairs_impairs()
print(a)