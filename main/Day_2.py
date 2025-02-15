class Day_2:
    def __init__(self, fichier):
        self.fichier = fichier
        self.rapports = self._charger_donnees()

    def _charger_donnees(self):
        with open(self.fichier, 'r') as fichier:
            return [[int(nbr) for nbr in ligne.strip().split()] for ligne in fichier]

    def est_rapport_sur(self, rapport):
        direction = None 
        for i in range(1, len(rapport)):
            difference = rapport[i] - rapport[i - 1]
            if direction is None:
                direction = "croissante" if difference > 0 else "décroissante"
            if (direction == "croissante" and not 1 <= difference <= 3) or \
               (direction == "décroissante" and not -3 <= difference <= -1):
                return False
        return True

    def partie_1(self):
        return sum(1 for rapport in self.rapports if self.est_rapport_sur(rapport))

    def peut_devenir_sur(self, rapport):
        for i in range(len(rapport)):
            nouveau_rapport = rapport[:i] + rapport[i+1:]
            if self.est_rapport_sur(nouveau_rapport):
                return True
        return False

    def partie_2(self):
        return sum(1 for rapport in self.rapports if self.est_rapport_sur(rapport) or self.peut_devenir_sur(rapport))

if __name__ == "__main__":
    lien_fichier = "Input_Data/Day_2.txt"
    calculateur = Day_2(lien_fichier)
    
    print(calculateur.partie_1())
    print(calculateur.partie_2())