lien_fichier = 'Input_Data/Day_22.txt'

with open(lien_fichier, 'r') as fichier:
    donnees = fichier.readlines()
    
# Partie 1

def partie1(donnees):
    resultats = []
    for secret in map(int, donnees):
        for _ in range(2000):
            secret = ((secret * 64) ^ secret) % 16777216
            secret = ((secret // 32) ^ secret) % 16777216
            secret = ((secret * 2048) ^ secret) % 16777216
        resultats.append(secret)
    return sum(resultats)

resulta = partie1(donnees)
print(resulta)

# Partie 2

from collections import defaultdict

def partie2(donnees):
    prix = []
    for secret in map(int, donnees):
        prix_individuel = []
        for _ in range(2000):
            secret = ((secret * 64) ^ secret) % 16777216
            secret = ((secret // 32) ^ secret) % 16777216
            secret = ((secret * 2048) ^ secret) % 16777216
            prix_individuel.append(secret % 10)
        prix.append(prix_individuel)

    changements = [[b - a for a, b in zip(p, p[1:])] for p in prix]

    montants = defaultdict(int)
    for acheteur_idx, changement in enumerate(changements):
        cles = set()
        for i in range(len(changement) - 3):
            cle = tuple(changement[i : i + 4])
            if cle in cles:
                continue
            montants[cle] += prix[acheteur_idx][i + 4]
            cles.add(cle)
    montant_maximal = max(montants.values())

    return montant_maximal

resulta = partie2(donnees)
print(resulta)