note = int(input("Entrez un nombre:\n"))

if note > 20 or note < 0:
    print("La note est comprise entre 0 et 20.")
else:
    if note >= 16:
        print("TB")
    elif note >= 12:
        print("Bien")
    elif note >= 10:
        print("Réussi")
    else:
        print("Echec")