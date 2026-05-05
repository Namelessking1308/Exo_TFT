taille_dic = {"S": 3, 
              "M": 5, 
              "L": 8}

taille = input("Quel tailles souhaitez-vous ? S/M/L\n")

cafe = {"Espresso": 10, 
        "Macchiato" : 5, 
        "Latté": 6}

print("---Liste des cafés---")
for i in cafe:
    print(i)

choix1 = input("Quel café souhaitez-vous ?\n")

if choix1 in cafe:
    print(f"Vous avez choisis {choix1}\n")
    demande2 = input("Souhaitez-vous un extra ? Oui/Non\n").lower().strip()

    if demande2 == "oui":
        extra = {"sucre" : 2, 
                 "Double dose" : 3, 
                 "Lait" : 4}
        print("---Liste des Extras---")

        for i in extra:
            print(i)
        Extra2 = input("Quel extra souhaitez-vous ?\n")

        if Extra2 in extra:
            print(f"Vous avez choisi un {choix1} taille {taille} avec {Extra2} en extra.\n")
            print("---TOTAL---")
            print(f"{cafe[choix1] + taille_dic[taille]+ extra[Extra2]} €")
    else:
        print(f"Vous avez choisi un {choix1} taille {taille}")
        print("---TOTAL---")
        print(f"{cafe[choix1] + taille_dic[taille]} €")