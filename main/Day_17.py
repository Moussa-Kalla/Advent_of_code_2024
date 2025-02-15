# fichier texte d'entree
registre_a = 66752888
registre_b = 0
registre_c = 0
programme = [2, 4, 1, 7, 7, 5, 1, 7, 0, 3, 4, 1, 5, 5, 3, 0]

# Partie 1

def obtenir_valeur_combo(operande, registre_a, registre_b, registre_c):
    if operande < 4:
        return operande
    elif operande == 4:
        return registre_a
    elif operande == 5:
        return registre_b
    elif operande == 6:
        return registre_c
    return None

def executer_programme(registre_a, registre_b, registre_c, programme):
    pointeur = 0
    sortie = []

    while pointeur < len(programme):
        opcode = programme[pointeur]
        operande = programme[pointeur + 1]

        if opcode == 0:  # adv
            denominateur = 2 ** obtenir_valeur_combo(operande, registre_a, registre_b, registre_c)
            registre_a //= denominateur
        elif opcode == 1:  # bxl
            registre_b ^= operande
        elif opcode == 2:  # bst
            registre_b = obtenir_valeur_combo(operande, registre_a, registre_b, registre_c) % 8
        elif opcode == 3:  # jnz
            if registre_a != 0:
                pointeur = operande
                continue
        elif opcode == 4:  # bxc
            registre_b ^= registre_c
        elif opcode == 5:  # out
            sortie.append(obtenir_valeur_combo(operande, registre_a, registre_b, registre_c) % 8)
        elif opcode == 6:  # bdv
            denominateur = 2 ** obtenir_valeur_combo(operande, registre_a, registre_b, registre_c)
            registre_b = registre_a // denominateur
        elif opcode == 7:  # cdv
            denominateur = 2 ** obtenir_valeur_combo(operande, registre_a, registre_b, registre_c)
            registre_c = registre_a // denominateur

        pointeur += 2

    return sortie

def trouver_valeur_initiale(programme):
    A = sum(7 * 8**i for i in range(len(programme) - 1)) + 1

    while True:
        registre_a = A
        registre_b = 0
        registre_c = 0
        sortie = executer_programme(registre_a, registre_b, registre_c, programme)

        if len(sortie) > len(programme):
            raise ValueError("La sortie est trop longue")

        if sortie == programme:
            return A

        ajout = 0
        for i in range(len(sortie) - 1, -1, -1):
            if sortie[i] != programme[i]:
                ajout = 8**i
                A += ajout
                break

resulta = executer_programme(registre_a, registre_b, registre_c, programme)
print(resulta)

# Partie 2

resulta = trouver_valeur_initiale(programme)
print(resulta)
