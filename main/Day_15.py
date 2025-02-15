lien_fichier = 'Input_Data/Day_15.txt'

def lire_entree(nom_fichier):
    with open(nom_fichier, "r", encoding="utf-8") as fichier:
        return [ligne.rstrip("\n") for ligne in fichier]
entree = lire_entree(lien_fichier)


directions = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}

def obtenir_position_robot(grille):
    for i, ligne in enumerate(grille):
        for j, case in enumerate(ligne):
            if case == "@":
                return (i, j)

def deplacer(grille, position, mouvements, partie):
    for mouvement in mouvements:
        ny = position[0] + directions[mouvement][0]
        nx = position[1] + directions[mouvement][1]

        if grille[ny][nx] == ".":
            position = (ny, nx)
        elif grille[ny][nx] == "#":
            continue
        else:
            bords, adjacents = obtenir_adjacents_et_bords(grille, position, mouvement, partie)
            bloque = 0
            dy, dx = directions[mouvement]
            for boite in bords:
                ny, nx = (boite[0] + dy, boite[1] + dx)
                if grille[ny][nx] == "#":
                    bloque += 1
            if bloque == 0:
                grille = mettre_a_jour_grille(grille, adjacents, mouvement)
                position = (position[0] + dy, position[1] + dx)
    return grille

def obtenir_adjacents_et_bords(grille, position, mouvement, partie=1):
    y, x = position
    dy, dx = directions[mouvement]

    adjacents = set()
    if partie == 1 or mouvement in "<>":
        while True:
            ny, nx = y + dy, x + dx
            if grille[ny][nx] in ".#":
                return [(ny - dy, nx - dx)], adjacents
            y = ny
            x = nx
            adjacents.add((y, x))
    else:
        bords = []
        file = [(y, x)]
        while file:
            y, x = file.pop(0)
            if (y, x) in adjacents:
                continue
            adjacents.add((y, x))
            ny, nx = y + dy, x + dx
            if grille[ny][nx] in ".#":
                bords.append((y, x))
            elif grille[ny][nx] == "[":
                file.append((ny, nx))
                file.append((ny, nx + 1))
            elif grille[ny][nx] == "]":
                file.append((ny, nx))
                file.append((ny, nx - 1))

        return bords, adjacents - {(position[0], position[1])}

def mettre_a_jour_grille(grille, adjacents, mouvement):
    coordonnees_tries = []

    match mouvement:
        case "^":
            coordonnees_tries = sorted(adjacents, key=lambda x: x[0])
        case "v":
            coordonnees_tries = sorted(adjacents, key=lambda x: x[0], reverse=True)
        case "<":
            coordonnees_tries = sorted(adjacents, key=lambda x: x[1])
        case ">":
            coordonnees_tries = sorted(adjacents, key=lambda x: x[1], reverse=True)

    dy, dx = directions[mouvement]
    for coord in coordonnees_tries:
        y, x = coord
        ny, nx = y + dy, x + dx
        grille[ny][nx] = grille[y][x]
        grille[y][x] = "."

    return grille

def calculer_somme_coordonnees(grille, partie=1):
    boite = "[" if partie == 2 else "O"
    return sum(100 * y + x for y, ligne in enumerate(grille) for x, case in enumerate(ligne) if case == boite)

def redimensionner_grille(grille):
    correspondances = {
        "#": "##",
        "O": "[]",
        ".": "..",
        "@": "@.",
    }
    return [list("".join(correspondances[c] for c in ligne)) for ligne in grille]


def partie1(entree):
    partie = 1
    grille, mouvements = "\n".join(entree).split("\n\n")
    grille = [list(ligne) for ligne in grille.split("\n")]
    mouvements = list("".join(mouvements.split("\n")))

    position = obtenir_position_robot(grille)
    grille[position[0]][position[1]] = "."

    grille = deplacer(grille, position, mouvements, partie)
    return calculer_somme_coordonnees(grille, partie)

resulta = partie1(entree)
print(resulta)

def partie2(entree):
    partie = 2
    grille, mouvements = "\n".join(entree).split("\n\n")
    grille = [list(ligne) for ligne in grille.split("\n")]
    mouvements = list("".join(mouvements.split("\n")))

    grille = redimensionner_grille(grille)

    position = obtenir_position_robot(grille)
    grille[position[0]][position[1]] = "."

    grille = deplacer(grille, position, mouvements, partie)
    return calculer_somme_coordonnees(grille, partie)

resulta = partie2(entree)
print(resulta)