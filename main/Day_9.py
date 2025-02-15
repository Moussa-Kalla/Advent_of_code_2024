lien_fichier = 'Input_Data/Day_9.txt'
texte = open(lien_fichier).read()
nbrs = [int(c) for c in texte.strip()]

# Part1

def cal_checksum(nbrs):
    disq = []
    id_fich = 0
    for i in range(0, len(nbrs)):
        if i % 2 == 0: 
            disq.extend([id_fich] * nbrs[i])
            id_fich += 1
        else: 
            disq.extend([-1] * nbrs[i]) 

    while True:
        pos_esp = -1
        for i in range(len(disq)):
            if disq[i] == -1:
                pos_esp = i
                break

        if pos_esp == -1: 
            break

        pos_fich = -1
        for i in range(len(disq)-1, pos_esp, -1):
            if disq[i] != -1:
                pos_fich = i
                break

        if pos_fich == -1: 
            break

        disq[pos_esp] = disq[pos_fich]
        disq[pos_fich] = -1

    checksum = 0
    for pos, block in enumerate(disq):
        if block != -1:
            checksum += pos * block
    return checksum

resulta = cal_checksum(nbrs)
print(resulta)

# Part2

def parse_disq(nbrs):
    disq = []
    id_fich = 0
    for i in range(len(nbrs)):
        if i % 2 == 0:
            disq.extend([id_fich] * nbrs[i])
            id_fich += 1
        else:
            disq.extend([-1] * nbrs[i])
    return disq, id_fich 

def find_files(disq, total_files):

    info_fich = []
    current_id_fich = None
    start_pos = None
    length = 0
    pos_pos = [None] * total_files

    for i, block in enumerate(disq):
        if block == -1:
            continue
        if pos_pos[block] is None:
            pos_pos[block] = [i, 1]
        else:
            pos_pos[block][1] += 1
    for fid in range(total_files):
        start, length = pos_pos[fid]
        info_fich.append((fid, start, length))

    return info_fich

def find_space_for_file(disq, file_start, file_length):
    free_count = 0
    free_start = -1
    best_start = -1

    for i in range(file_start):
        if disq[i] == -1:
            if free_count == 0:
                free_start = i
            free_count += 1
            if free_count >= file_length:
                best_start = free_start
                break
        else:
            free_count = 0
            free_start = -1
    
    return best_start

def move_file(disq, id_fich, start, length):
    new_start = find_space_for_file(disq, start, length)
    if new_start == -1:
        return
    pos_pos = [i for i in range(start, start+length)]
    for pos in pos_pos:
        disq[pos] = -1
    for i in range(length):
        disq[new_start + i] = id_fich

def compute_checksum(disq):
    checksum = 0
    for pos, block in enumerate(disq):
        if block != -1:
            checksum += pos * block
    return checksum


disq, total_files = parse_disq(nbrs)

info_fich = find_files(disq, total_files)
info_fich.sort(key=lambda x: x[0], reverse=True)
for id_fich, start, length in info_fich:
    move_file(disq, id_fich, start, length)

resulta = compute_checksum(disq)
print(resulta)

