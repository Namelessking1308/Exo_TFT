# Créez un programme qui permet à l'utilisateur de choisir un menu pour chaque repas (petit-déjeuner, déjeuner, dîner)
# parmi des options préétablies. Après la sélection, il affiche les choix de l'utilisateur pour chaque repas et résume
# l'ensemble des repas de la journée.

petit_dej = {"Oeuf" : 1, "Pancake": 1, "Céréale" : 1}

dej = {"Salade" : 1, "Sandwich" : 1, "Fromage": 1}

diner = {"Lasagne": 1, "Riz poulet": 1, "Grattin": 1}

print("--- Petit Déjeuner ---")
for i in petit_dej:
    print(i)
    
print("--- Déjeuner ---")
for i in dej:
    print(i)

print("--- Dîner ---")
for i in diner:
    print(i)

choix1 = input("Que voulez-vous pour le petit-déjeuner ?\n")

choix2 = input("Que voulez-vous pour le déjeuner ?\n")

choix3 = input("Que voulez-vous pour le dîner ?\n")

if choix1 in petit_dej and choix2 in dej and choix3 in diner:
    print("--- Votre séléction ---")
    print(f"Vous avez pris un/une {choix1} en petit-déjeuner\nUn/Une {choix2} en déjeuner \nEt un/une {choix3} en dîner")
