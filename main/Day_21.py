from collections import defaultdict
from functools import cachel

lien_fichier = 'Input_Data/Day_21.txt'

with open(lien_fichier, 'r') as file:
    lignes = file.readlines()

codes_clavier = [ligne.strip() for ligne in lignes]

# Partie 1

def parse_moves(clavier):
        def obtenir_position_touche(clavier):
            position = {}
            for ligne, rangee in enumerate(clavier):
                for colonne, touche in enumerate(rangee):
                    position[touche] = (ligne, colonne)
            return position

        position = obtenir_position_touche(clavier)
        touches = sorted(position.keys())

        mouvements = defaultdict(list)
        for touche1 in touches:
            for touche2 in touches:
                if touche1 == "#" or touche2 == "#" or touche1 == touche2:
                    continue
                p1 = position[touche1]
                p2 = position[touche2]

                if p1[0] == p2[0]:
                    d = ">" if p2[1] > p1[1] else "<"
                    mouvements[(touche1, touche2)].append(d * (abs(p2[1] - p1[1])) + "A")
                elif p1[1] == p2[1]:
                    d = "v" if p2[0] > p1[0] else "^"
                    mouvements[(touche1, touche2)].append(d * (abs(p2[0] - p1[0])) + "A")
                else:
                    if p1[0] != position["#"][0] or p2[1] != position["#"][1]:
                        d1 = ">" if p2[1] > p1[1] else "<"
                        d2 = "v" if p2[0] > p1[0] else "^"
                        mouvements[(touche1, touche2)].append(d1 * (abs(p2[1] - p1[1])) + d2 * (abs(p2[0] - p1[0])) + "A")
                    if p1[1] != position["#"][1] or p2[0] != position["#"][0]:
                        d1 = "v" if p2[0] > p1[0] else "^"
                        d2 = ">" if p2[1] > p1[1] else "<"
                        mouvements[(touche1, touche2)].append(d1 * (abs(p2[0] - p1[0])) + d2 * (abs(p2[1] - p1[1])) + "A")
        return mouvements

def construire_combinaisons(tableaux, actuel=[], index=0):
        if index == len(tableaux):
            return [actuel]
        resultats = []
        for valeur in tableaux[index]:
            nouveaux_resultats = construire_combinaisons(tableaux, actuel + [valeur], index + 1)
            resultats.extend(nouveaux_resultats)
        return resultats

@cache
def traduire(code, profondeur):
        if code[0].isnumeric():
            mouvements = traduire_clavier_numerique(code)
        else:
            mouvements = traduire_clavier_directionnel(code)

        if profondeur == 0:
            return min([sum(map(len, mouvement)) for mouvement in mouvements])
        else:
            return min([sum(traduire(code_actuel, profondeur - 1) for code_actuel in mouvement) for mouvement in mouvements])

def traduire_clavier_numerique(code):
        code = "A" + code
        mouvements = parse_moves(clavier)
        mouvements = [mouvements(a, b)] for a, b in zip(code, code[1:])
        mouvements = construire_combinaisons(mouvements)
        return mouvements

def traduire_clavier_directionnel(code):
        code = "A" + code
        mouvements = [mouvements[(a, b)] if a != b else ["A"] for a, b in zip(code, code[1:])]
        mouvements = construire_combinaisons(mouvements)
        return mouvements

def partie1(donnees):
        clavier1 = ["789", "456", "123", "#0A"]
        clavier2 = ["#^A", "<v>"]


        complexites = 0

        for code in donnees:
            longueur_minimale = traduire(code, 2)
            complexites += longueur_minimale * int(code[:-1])

        return complexites

resulta = partie1(codes_clavier)
print(resulta)

# Partie 2


