from collections import deque

lien_fichier = 'Input_Data/Day_20.txt'

fichier = open(lien_fichier, "r")
carte = fichier.read().split("\n")
fichier.close()

hauteur = len(carte)
largeur = len(carte[0])

pos_depart = None
pos_arrivee = None
for y in range(hauteur):
    for x in range(largeur):
        if carte[y][x] == 'S':
            pos_depart = (x, y)
        elif carte[y][x] == 'E':
            pos_arrivee = (x, y)
            
# Partie 1

def est_libre(x, y):
    if 0 <= x < largeur and 0 <= y < hauteur:
        return carte[y][x] != '#'
    return False

def bfs_distance(depart, arrivee):
    file = deque()
    file.append((depart[0], depart[1], 0))
    visite = set()
    visite.add((depart[0], depart[1]))
    while file:
        x, y, d = file.popleft()
        if (x, y) == arrivee:
            return d
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if est_libre(nx, ny) and (nx, ny) not in visite:
                visite.add((nx, ny))
                file.append((nx, ny, d+1))
    return None

dist_sans_triche = bfs_distance(pos_depart, pos_arrivee)

def bfs_distances(arrivee):
    dist = [[None]*largeur for _ in range(hauteur)]
    file = deque()
    file.append((arrivee[0], arrivee[1], 0))
    dist[arrivee[1]][arrivee[0]] = 0
    while file:
        x, y, d = file.popleft()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < largeur and 0 <= ny < hauteur:
                if carte[ny][nx] != '#' and dist[ny][nx] is None:
                    dist[ny][nx] = d+1
                    file.append((nx, ny, d+1))
    return dist

dist_arrivee = bfs_distances(pos_arrivee)
dist_depart = bfs_distances(pos_depart)

def voisins_triche(x, y, murs):
    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < largeur and 0 <= ny < hauteur:
            c = carte[ny][nx]
            if c == '#' and murs > 0:
                yield nx, ny, murs-1
            elif c != '#':
                yield nx, ny, murs

resulta = 0
deja_vu = set()

for y in range(hauteur):
    for x in range(largeur):
        if dist_depart[y][x] is not None:
            etat_initial = (x, y, 2, 0)
            file = deque([etat_initial])
            visite = set([etat_initial])
            while file:
                cx, cy, m, d = file.popleft()
                if d > 2:
                    continue
                if d > 0 and carte[cy][cx] != '#':
                    if dist_arrivee[cy][cx] is not None:
                        temps_total = dist_depart[y][x] + d + dist_arrivee[cy][cx]
                        economie = dist_sans_triche - temps_total
                        if economie >= 100:
                            if ((x,y),(cx,cy)) not in deja_vu:
                                deja_vu.add(((x,y),(cx,cy)))
                                resulta += 1
                if d < 2:
                    for nx, ny, nm in voisins_triche(cx, cy, m):
                        etat = (nx, ny, nm, d+1)
                        if etat not in visite:
                            visite.add(etat)
                            file.append(etat)

print(resulta)

# Partie 2

def est_libre(x, y):
    if 0 <= x < largeur and 0 <= y < hauteur:
        return carte[y][x] != '#'
    return False

def bfs_distance(depart, arrivee):
    file = deque()
    file.append((depart[0], depart[1], 0))
    visite = set()
    visite.add((depart[0], depart[1]))
    while file:
        x, y, d = file.popleft()
        if (x, y) == arrivee:
            return d
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if est_libre(nx, ny) and (nx, ny) not in visite:
                visite.add((nx, ny))
                file.append((nx, ny, d+1))
    return None

dist_sans_triche = bfs_distance(pos_depart, pos_arrivee)

def bfs_distances(arrivee):
    dist = [[None]*largeur for _ in range(hauteur)]
    file = deque()
    file.append((arrivee[0], arrivee[1], 0))
    dist[arrivee[1]][arrivee[0]] = 0
    while file:
        x, y, d = file.popleft()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < largeur and 0 <= ny < hauteur:
                if carte[ny][nx] != '#' and dist[ny][nx] is None:
                    dist[ny][nx] = d+1
                    file.append((nx, ny, d+1))
    return dist

dist_arrivee = bfs_distances(pos_arrivee)
dist_depart = bfs_distances(pos_depart)

resulta = 0
deja_vu = set()

valides = []
for y in range(hauteur):
    for x in range(largeur):
        if dist_depart[y][x] is not None and dist_arrivee[y][x] is not None:
            valides.append((x,y))

for (sx, sy) in valides:
    d_dep = dist_depart[sy][sx]
    file = deque()
    visite = set()
    file.append((sx, sy, 0)) 
    visite.add((sx, sy, 0))
    while file:
        cx, cy, d_triche = file.popleft()
        if d_triche > 0 and carte[cy][cx] != '#':
            if dist_arrivee[cy][cx] is not None:
                temps_total = d_dep + d_triche + dist_arrivee[cy][cx]
                economie = dist_sans_triche - temps_total
                if economie >= 100:
                    if ((sx,sy),(cx,cy)) not in deja_vu:
                        deja_vu.add(((sx,sy),(cx,cy)))
                        resulta += 1
        if d_triche < 20:
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = cx+dx, cy+dy
                if 0 <= nx < largeur and 0 <= ny < hauteur:
                    etat = (nx, ny, d_triche+1)
                    if etat not in visite:
                        visite.add(etat)
                        file.append(etat)

print(resulta)
