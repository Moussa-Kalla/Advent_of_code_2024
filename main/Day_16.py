import heapq
import os

lien_fichier = 'Input_Data/Day_16.txt'

with open(lien_fichier, 'r') as f:
    labyrinthe = [ligne.strip() for ligne in f]
    
# Part 1

def trouver_positions(labyrinthe):
    depart, fin = None, None
    for y, ligne in enumerate(labyrinthe):
        for x, case in enumerate(ligne):
            if case == 'S':
                depart = (x, y)
            elif case == 'E':
                fin = (x, y)
    return depart, fin

def est_valide(labyrinthe, x, y):
    return 0 <= y < len(labyrinthe) and 0 <= x < len(labyrinthe[0]) and labyrinthe[y][x] != '#'

def cal_chemin_min(labyrinthe):
    depart, fin = trouver_positions(labyrinthe)

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = [(0, 0, *depart, 0)] 
    visites = set()

    while queue:
        score, rotations, x, y, direction = heapq.heappop(queue)

        if (x, y) == fin:
            return score

        if (x, y, direction) in visites:
            continue

        visites.add((x, y, direction))

        for new_direction, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if est_valide(labyrinthe, nx, ny):
                nouveau_score = score + 1
                if new_direction != direction:
                    nouveau_score += 1000
                heapq.heappush(queue, (nouveau_score, rotations + (new_direction != direction), nx, ny, new_direction))

    return float('inf')  

resulta = cal_chemin_min(labyrinthe)
print(resulta)

# Part 2

import heapq

def trouver_positions(labyrinthe):
    depart, fin = None, None
    for y, ligne in enumerate(labyrinthe):
        for x, case in enumerate(ligne):
            if case == 'S':
                depart = (x, y)
            elif case == 'E':
                fin = (x, y)
    return depart, fin

def est_valide(labyrinthe, x, y):
    return 0 <= y < len(labyrinthe) and 0 <= x < len(labyrinthe[0]) and labyrinthe[y][x] != '#'

def trouver_routes(labyrinthe):
    grille = []
    depart, fin = trouver_positions(labyrinthe)

    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    routes = []
    visites = {}

    queue = [(depart, [depart], 0, 0)] 
    while queue:
        (x, y), historique, score_actuel, direction_actuelle = queue.pop(0)

        if (x, y) == fin:
            routes.append((historique, score_actuel))
            continue

        if ((x, y), direction_actuelle) in visites and visites[((x, y), direction_actuelle)] < score_actuel:
            continue

        visites[((x, y), direction_actuelle)] = score_actuel

        for nouvelle_direction, (dx, dy) in enumerate(directions):
            if (direction_actuelle + 2) % 4 == nouvelle_direction:
                continue

            nx, ny = x + dx, y + dy
            if est_valide(labyrinthe, nx, ny) and (nx, ny) not in historique:
                if nouvelle_direction == direction_actuelle:
                    queue.append(((nx, ny), historique + [(nx, ny)], score_actuel + 1, nouvelle_direction))
                else:
                    queue.append(((x, y), historique, score_actuel + 1000, nouvelle_direction))

    return routes

def compter_cases_optimales(labyrinthe):
    routes_possibles = trouver_routes(labyrinthe)
    score_minimal = min(route[1] for route in routes_possibles)
    meilleures_routes = [route for route in routes_possibles if route[1] == score_minimal]
    cases_optimales = {case for route in meilleures_routes for case in route[0]}
    return len(cases_optimales)

resulta = compter_cases_optimales(labyrinthe)
print(resulta)
