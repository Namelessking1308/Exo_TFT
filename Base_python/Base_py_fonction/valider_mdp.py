# 8. Créez une fonction valider_mot_de_passe() qui prend un mot de passe en entrée et vérifie s'il répond à certains
# critères de complexité (longueur minimale, présence de chiffres, de lettres majuscules et minuscules, de caractères
# spéciaux, etc.). La fonction devrait renvoyer True si le mot de passe est valide et False sinon

import re
def valider_mot_de_passe():
    mdp = input("Entrer le mot de passe à vérifier: ")

    maj = re.search(r"[A-Z]", mdp)
    min = re.search(r"[a-z]", mdp)
    num = re.search(r"[0-9]", mdp)
    speciaux = re.search(r"[^A-Za-z0-9]", mdp)

    if len(mdp) >= 10 and maj and min and num and speciaux:
        return True
    else:
        return False
    
print(valider_mot_de_passe())