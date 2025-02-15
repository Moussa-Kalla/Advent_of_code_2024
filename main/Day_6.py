lien_fichier = 'Input_Data/Day_6.txt'

def lire_fich_txt(lien_fichier):
    with open(lien_fichier, 'r') as fichier:
        return [list(ligne.strip()) for ligne in fichier]
    
grille = lire_fich_txt(lien_fichier)


# Part1

def simul_chmin(grille):
    direct_os = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direct_o_actu = 0 
    poss_visitees = set() 

    lignes = len(grille)
    cols = len(grille[0])
    for ligne in range(lignes):
        for col in range(cols):
            if grille[ligne][col] in "^>v<":
                x, y = ligne, col
                if grille[ligne][col] == ">":
                    direct_o_actu = 1
                elif grille[ligne][col] == "v":
                    direct_o_actu = 2
                elif grille[ligne][col] == "<":
                    direct_o_actu = 3
                grille[ligne][col] = "." 

    while 0 <= x < lignes and 0 <= y < cols:
        poss_visitees.add((x, y)) 
        dx, dy = direct_os[direct_o_actu]
        nx, ny = x + dx, y + dy

        if 0 <= nx < lignes and 0 <= ny < cols and grille[nx][ny] == "#":
            direct_o_actu = (direct_o_actu + 1) % 4
        else:
            x, y = nx, ny
    return len(poss_visitees)

resulta = simul_chmin(grille)
print(resulta)



# Part2

def simul_chmin_bcl(grille, obst=None):
    direct_os = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direct_o_actu = 0 
    poss_visitees = set() 
    seq_visitee = [] 

    lignes = len(grille)
    cols = len(grille[0])
    for ligne in range(lignes):
        for col in range(cols):
            if grille[ligne][col] in "^>v<":
                x, y = ligne, col
                if grille[ligne][col] == ">":
                    direct_o_actu = 1
                elif grille[ligne][col] == "v":
                    direct_o_actu = 2
                elif grille[ligne][col] == "<":
                    direct_o_actu = 3
                grille[ligne][col] = "."
    if obst:
        grille[obst[0]][obst[1]] = "#"

    while 0 <= x < lignes and 0 <= y < cols:
        etat_act = (x, y, direct_o_actu)
        if etat_act in poss_visitees:
            return True
        
        poss_visitees.add(etat_act)
        seq_visitee.append(etat_act)

        dx, dy = direct_os[direct_o_actu]
        nx, ny = x + dx, y + dy

        if 0 <= nx < lignes and 0 <= ny < cols and grille[nx][ny] == "#":
            direct_o_actu = (direct_o_actu + 1) % 4
        else:
            x, y = nx, ny
    return False

def trouver_poss_obst(grille):
    lignes = len(grille)
    cols = len(grille[0])
    poss_possibles = []

    for ligne in range(lignes):
        for col in range(cols):
            if grille[ligne][col] == "#" or grille[ligne][col] in "^>v<":
                continue
            if simul_chmin_bcl([ligne[:] for ligne in grille], (ligne, col)):
                poss_possibles.append((ligne, col))

    return poss_possibles

grille = lire_fich_txt(lien_fichier)

resulta = len(trouver_poss_obst(grille))
print(resulta)

