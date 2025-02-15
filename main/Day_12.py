from collections import deque

lien_fichier = 'Input_Data/Day_12.txt'

with open(lien_fichier, 'r') as fichier:
    carte = [ligne.strip() for ligne in fichier.readlines()]
    
# Part1

from collections import deque

def cal_cout_total(carte_jardin):
    lignes, cols = len(carte_jardin), len(carte_jardin[0])
    visites = [[False for _ in range(cols)] for _ in range(lignes)]
    directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cout_total = 0

    for ligne in range(lignes):
        for col in range(cols):
            if not visites[ligne][col]:
                type_plante = carte_jardin[ligne][col]
                file = deque([(ligne, col)])
                visites[ligne][col] = True
                aire = 0
                perimetre = 0

                while file:
                    x, y = file.popleft()
                    aire += 1

                    for dx, dy in directs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < lignes and 0 <= ny < cols:
                            if carte_jardin[nx][ny] == type_plante and not visites[nx][ny]:
                                visites[nx][ny] = True
                                file.append((nx, ny))
                            elif carte_jardin[nx][ny] != type_plante:
                                perimetre += 1
                        else:
                            perimetre += 1

                cout_total += aire * perimetre

    return cout_total

resulta = cal_cout_total(carte)
print(resulta)

# Part2

def calculer_cout_avec_cotes(carte_jardin):
    def obtenir_cotes_du_groupe(groupe):
        min_y = min(groupe, key=lambda x: x[0])[0]
        max_y = max(groupe, key=lambda x: x[0])[0]
        min_x = min(groupe, key=lambda x: x[1])[1]
        max_x = max(groupe, key=lambda x: x[1])[1]
        lignes = max_y - min_y + 1
        colonnes = max_x - min_x + 1
        nouveau_groupe = [(y - min_y, x - min_x) for y, x in groupe]

        grille = [[" " for _ in range(colonnes + 2)] for _ in range(lignes + 2)]
        for y, x in nouveau_groupe:
            grille[y + 1][x + 1] = "X"

        cotes = 0

        for _ in range(2):
            for y in range(1, lignes + 1):
                cotes += len("".join(["X" if actuel != dessus and actuel == "X" else " " for actuel, dessus in zip(grille[y], grille[y - 1])]).split())

                cotes += len("".join(["X" if actuel != dessous and actuel == "X" else " " for actuel, dessous in zip(grille[y], grille[y + 1])]).split())

            grille = list(zip(*grille[::-1]))
            lignes, colonnes = colonnes, lignes

        return cotes

    lignes, colonnes = len(carte_jardin), len(carte_jardin[0])
    visites = [[False for _ in range(colonnes)] for _ in range(lignes)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cout_total = 0

    for ligne in range(lignes):
        for colonne in range(colonnes):
            if not visites[ligne][colonne]:
                type_plante = carte_jardin[ligne][colonne]
                file = deque([(ligne, colonne)])
                visites[ligne][colonne] = True
                groupe = set()

                while file:
                    x, y = file.popleft()
                    groupe.add((x, y))

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < lignes and 0 <= ny < colonnes and not visites[nx][ny] and carte_jardin[nx][ny] == type_plante:
                            visites[nx][ny] = True
                            file.append((nx, ny))

                cotes = obtenir_cotes_du_groupe(groupe)
                cout_total += len(groupe) * cotes

    return cout_total

resulta = calculer_cout_avec_cotes(carte)
print(resulta)
