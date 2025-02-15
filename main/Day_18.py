lien_fichier = 'Input_Data/Day_18.txt'

taille = 71
espace = [[True for _ in range(taille)] for _ in range(taille)]
coordonnee_depart = (0, 0)
coordonnee_arrivee = (70, 70)

fichier = open(lien_fichier, "r")
donnees = fichier.read().strip().split("\n")
fichier.close()


# Part 1

for i in range(min(1024, len(donnees))):
    ligne = donnees[i].strip()
    if ligne == "":
        continue
    x, y = ligne.split(",")
    x, y = int(x), int(y)
    if 0 <= x < taille and 0 <= y < taille:
        espace[y][x] = False

from collections import deque

file = deque()
file.append((coordonnee_depart, 0))
visite = set()
visite.add(coordonnee_depart)

directions = [(1,0),(-1,0),(0,1),(0,-1)]
pas_min = None

while file:
    (cx, cy), dist = file.popleft()
    if (cx, cy) == coordonnee_arrivee:
        pas_min = dist
        break
    for dx, dy in directions:
        nx, ny = cx+dx, cy+dy
        if 0 <= nx < taille and 0 <= ny < taille:
            if (nx, ny) not in visite and espace[ny][nx]:
                visite.add((nx, ny))
                file.append(((nx, ny), dist+1))

print(pas_min if pas_min is not None else "Aucun chemin")

# Part 2


def est_chemin_possible():
    from collections import deque
    file = deque()
    file.append(coordonnee_depart)
    visite = set()
    visite.add(coordonnee_depart)
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    while file:
        cx, cy = file.popleft()
        if (cx, cy) == coordonnee_arrivee:
            return True
        for dx, dy in directions:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < taille and 0 <= ny < taille:
                if (nx, ny) not in visite and espace[ny][nx]:
                    visite.add((nx, ny))
                    file.append((nx, ny))
    return False

fichier = open(lien_fichier, "r")
donnees = fichier.read().strip().split("\n")
fichier.close()

for i in range(len(donnees)):
    ligne = donnees[i].strip()
    if ligne == "":
        continue
    x, y = ligne.split(",")
    x, y = int(x), int(y)
    if 0 <= x < taille and 0 <= y < taille:
        espace[y][x] = False
    if not est_chemin_possible():
        print(str(x)+","+str(y))
        break
