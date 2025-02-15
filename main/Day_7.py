from itertools import product

lien_fichier = 'Input_Data/Day_7.txt'

def lire_fich_txt(lien_fichier):
    equ = []
    with open(lien_fichier, 'r') as fichier:
        for ligne in fichier:
            cible, nbrs = ligne.strip().split(":")
            cible = int(cible)
            nbrs = list(map(int, nbrs.strip().split()))
            equ.append((cible, nbrs))
    return equ

equ = lire_fich_txt(lien_fichier)

# Part1

def eval_exp(nbrs,ops):
    resul = nbrs[0]
    for i, op in enumerate(ops):
        if op == "+":
            resul = nbrs[i + 1]
        elif op == "*":
            resul *= nbrs[i + 1]
    return resul

def equ_valide(cible, nbrs):
    comb = product(["+", "*"], repeat=len(nbrs) - 1)
    for ops in comb:
        if eval_exp(nbrs, ops) == cible:
            return True
    return False

def cal_somme_equ_valides(equ):
    somme = 0
    for cible, nbrs in equ:
        if equ_valide(cible, nbrs):
            somme += cible
    return somme

resulta = cal_somme_equ_valides(equ)
print(resulta)

# Part2

from itertools import product


def eval_exp(nbrs, ops):
    resul = nbrs[0]
    for i, op in enumerate(ops):
        if op == "+":
            resul += nbrs[i + 1]
        elif op == "*":
            resul *= nbrs[i + 1]
        elif op == "||":
            resul = int(str(resul) + str(nbrs[i + 1]))
    return resul

def est_equ_valide(cible, nbrs):
    comb = product(["+", "*", "||"], repeat=len(nbrs) - 1)
    for ops in comb:
        if eval_exp(nbrs, ops) == cible:
            return True
    return False

def cal_somme_equ_valides(equ):
    somme = 0
    for cible, nbrs in equ:
        if est_equ_valide(cible, nbrs):
            somme += cible
    return somme

resulta = cal_somme_equ_valides(equ)
print(resulta)