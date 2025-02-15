lien_fichier = 'Input_Data/Day_14.txt'
with open(lien_fichier) as f:
    data = f.read().strip().split("\n")
    
def partie1(d):
    L, H = 101, 103
    t = 100
    rx, ry, vx, vy = [], [], [], []
    for l in d:
        l = l.strip()
        p, v = l.split(" v=")
        p = p.split("p=")[1]
        px, py = p.split(",")
        px, py = int(px), int(py)
        vx_, vy_ = v.split(",")
        vx_, vy_ = int(vx_), int(vy_)
        rx.append(px)
        ry.append(py)
        vx.append(vx_)
        vy.append(vy_)

    for i in range(len(rx)):
        rx[i] = (rx[i] + vx[i]*t) % L
        ry[i] = (ry[i] + vy[i]*t) % H

    cx, cy = L//2, H//2
    q1 = q2 = q3 = q4 = 0
    for i in range(len(rx)):
        x, y = rx[i], ry[i]
        if x < cx and y < cy:
            q1 += 1
        elif x > cx and y < cy:
            q2 += 1
        elif x < cx and y > cy:
            q3 += 1
        elif x > cx and y > cy:
            q4 += 1

    return q1*q2*q3*q4
resulta = partie1(data)
print(resulta)

def part2(data):
    robots = []
    for ligne in data:
        a, b = ligne.split(" ")
        x, y = map(int, a[2:].split(","))
        vx, vy = map(int, b[2:].split(","))
        robots.append(((x, y), (vx, vy)))

    width = 101
    height = 103

    t = 0
    while True:
        t += 1
        pos = set()
        valid = True
        for (x, y), (vx, vy) in robots:
            nx = (x + t*(vx+width)) % width
            ny = (y + t*(vy+height)) % height
            if (nx, ny) in pos:
                valid = False
                break
            pos.add((nx, ny))
        if valid:
            return t


resulta = part2(data)
print(resulta)

