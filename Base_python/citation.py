import random

citations = {
    "Persévérance": [
        "Le succès n’est pas final, l’échec n’est pas fatal : c’est le courage de continuer qui compte.",
        "N’abandonne jamais, les grandes choses prennent du temps.",
        "Tomber sept fois, se relever huit."
    ],
    "Amour": [
        "Aimer, ce n’est pas se regarder l’un l’autre, c’est regarder ensemble dans la même direction.",
        "L’amour est la poésie des sens.",
        "Là où il y a de l’amour, il y a de la vie."
    ],
    "Discipline": [
        "La discipline est le pont entre les objectifs et les accomplissements.",
        "Fais ce qui doit être fait, même quand tu n’en as pas envie.",
        "La motivation te fait commencer, la discipline te fait continuer."
    ]
}

print("Voici les thèmes :\n")
for theme in citations:
    print("-", theme)

choix = input("\nChoisissez un thème : ")

if choix in citations:
    citation = random.choice(citations[choix])
    print("\nCitation :")
    print(citation)
else:
    print("Thème invalide")