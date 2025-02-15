from collections import Counter

lien_fichier = 'Input_Data/Day_11.txt'
with open(lien_fichier) as f:
    pierres_init = [int(x) for x in f.read().split()]
    
# Partie 1

def simul_clignotmnt(liste_pierres, clignotements):
    pierres = Counter(liste_pierres)
    for _ in range(clignotements):
        nouvelles_pierres = Counter()
        for num, compte in pierres.items():
            if num == 0:
                nouvelles_pierres[1] += compte
            elif len(str(num)) % 2 == 0:
                s = str(num)
                milieu = len(s) // 2
                gauche = s[:milieu].lstrip('0') or '0'
                droite = s[milieu:].lstrip('0') or '0'
                nouvelles_pierres[int(gauche)] += compte
                nouvelles_pierres[int(droite)] += compte
            else:
                nouveau_num = num * 2024
                nouvelles_pierres[nouveau_num] += compte
        pierres = nouvelles_pierres
    total_pierres = sum(pierres.values())
    return total_pierres

resultat = simul_clignotmnt(pierres_init, 25)
print(resultat)

# Part 2

resultat = simul_clignotmnt(pierres_init, 75)
print(resultat)
