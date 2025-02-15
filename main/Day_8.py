from math import gcd


lien_fichier = 'Input_Data/Day_8.txt'
with open(lien_fichier, 'r', encoding='utf-8') as f:
    lgns_crt = [ligne.rstrip('\n') for ligne in f]
    
# Part1

def cal_ant_noeuds_part1(lgns_crt):
    htr = len(lgns_crt)
    lgr = len(lgns_crt[0]) if htr > 0 else 0

    freqs = {}
    for y, ligne in enumerate(lgns_crt):
        for x, caract in enumerate(ligne):
            if caract != '.':
                if caract not in freqs:
                    freqs[caract] = []
                freqs[caract].append((x, y))

    ant_noeuds = set()

    for freq, poss in freqs.items():
        n = len(poss)
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = poss[i]
                x2, y2 = poss[j]

                q1x, q1y = 2*x2 - x1, 2*y2 - y1
                q2x, q2y = 2*x1 - x2, 2*y1 - y2

                if 0 <= q1x < lgr and 0 <= q1y < htr:
                    ant_noeuds.add((q1x, q1y))
                if 0 <= q2x < lgr and 0 <= q2y < htr:
                    ant_noeuds.add((q2x, q2y))

    return len(ant_noeuds)

resulta = cal_ant_noeuds_part1(lgns_crt)
print(resulta)

# Part2

def cal_ant_noeuds_part2(lgns_crt):
    htr = len(lgns_crt)
    lgr = len(lgns_crt[0]) if htr > 0 else 0

    freqs = {} 
    for y, ligne in enumerate(lgns_crt):
        for x, caract in enumerate(ligne):
            if caract != '.':
                if caract not in freqs:
                    freqs[caract] = []
                freqs[caract].append((x, y))

    ant_noeuds = set()

    for freq, poss in freqs.items():
        if len(poss) < 2:
            continue

        n = len(poss)
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = poss[i]
                x2, y2 = poss[j]

                dx = x2 - x1
                dy = y2 - y1
                g = gcd(dx, dy) 
                dxp = dx // g
                dyp = dy // g
                k = 0
                while True:
                    xk = x1 + k * dxp
                    yk = y1 + k * dyp
                    if 0 <= xk < lgr and 0 <= yk < htr:
                        ant_noeuds.add((xk, yk))
                        k += 1
                    else:
                        break
                k = -1
                while True:
                    xk = x1 + k * dxp
                    yk = y1 + k * dyp
                    if 0 <= xk < lgr and 0 <= yk < htr:
                        ant_noeuds.add((xk, yk))
                        k -= 1
                    else:
                        break
    return len(ant_noeuds)

resulta = cal_ant_noeuds_part2(lgns_crt)
print(resulta)