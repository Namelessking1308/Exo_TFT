# Créez un programme qui calcule l'indice de masse corporelle (IMC) d'une personne en fonction de son poids et de sa
# taille. Utilisez des correspondances pour interpréter et catégoriser l'IMC résultant en différentes catégories de poids.

poids = int(input("Entrez votre poids en kg: "))

taille = float(input("Entrez votre taille en m: "))


imc = poids / (taille**2)

print(imc)
if imc < 18.5:
    print("Maigreur")
elif imc <= 25 and imc >= 18.5:
    print("Corpulence normale")
else:
    print("Surpoids")