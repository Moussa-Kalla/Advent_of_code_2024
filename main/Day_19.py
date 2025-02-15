lien_fichier = 'Input_Data/Day_19.txt'

fichier = open(lien_fichier, "r")
contenu = fichier.read().strip("\n")
fichier.close()

sections = contenu.split("\n\n")
patrons = sections[0].strip().split(", ")
designs = sections[1].strip().split("\n")

# Part 1

resulta = 0

for design in designs:
    longueur = len(design)
    dp = [False]*(longueur+1)
    dp[0] = True
    for i in range(longueur):
        if dp[i]:
            for p in patrons:
                plen = len(p)
                if i+plen <= longueur and design[i:i+plen] == p:
                    dp[i+plen] = True
    if dp[longueur]:
        resulta += 1

print(resulta)

# Part 2

resulta = 0

for design in designs:
    longueur = len(design)
    dp = [0]*(longueur+1)
    dp[0] = 1 
    for i in range(longueur):
        if dp[i] > 0:
            for p in patrons:
                plen = len(p)
                if i+plen <= longueur and design[i:i+plen] == p:
                    dp[i+plen] += dp[i]
    resulta += dp[longueur]

print(resulta)