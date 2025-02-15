from collections import deque
import numpy as np

lien_fichier = 'Input_Data/Day_10.txt'
with open(lien_fichier, 'r') as file:
    lgns = file.readlines()

map_topogr = np.array([list(map(int, lgn.strip())) for lgn in lgns])

# Part 1

def cal_score_dep(map_data):
    lignes, cols = map_data.shape
    directs = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    scores = []

    for r in range(lignes):
        for c in range(cols):
            if map_data[r, c] == 0:
                visit = set()
                queue = deque([(r, c, 0)]) 
                neuf_acces = set()

                while queue:
                    x, y, alt = queue.popleft()

                    if map_data[x, y] == 9:
                        neuf_acces.add((x, y))
                        continue

                    visit.add((x, y))

                    for dr, dc in directs:
                        nx, ny = x + dr, y + dc
                        if 0 <= nx < lignes and 0 <= ny < cols and (nx, ny) not in visit:
                            if map_data[nx, ny] == alt + 1:
                                queue.append((nx, ny, map_data[nx, ny]))

                scores.append(len(neuf_acces))
    return scores

resulta = sum(cal_score_dep(map_topogr))
print(resulta)

# Part 2

def cal_score_partie2(map_data):
    lignes, cols = map_data.shape
    directs = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    score = 0

    for r in range(lignes):
        for c in range(cols):
            if map_data[r, c] == 0: 
                vist = set()
                queue = deque([(r, c, 0)]) 
                traj = 0

                while queue:
                    x, y, alt = queue.popleft()

                    if map_data[x, y] == 9:
                        traj += 1
                        continue

                    vist.add((x, y))

                    for dr, dc in directs:
                        nx, ny = x + dr, y + dc
                        if 0 <= nx < lignes and 0 <= ny < cols and (nx, ny) not in vist:
                            if map_data[nx, ny] == alt + 1:
                                queue.append((nx, ny, map_data[nx, ny]))
                score += traj
    return score

scores = cal_score_partie2(map_topogr)
print(scores)

