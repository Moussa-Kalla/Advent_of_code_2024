class Day_1:
    def __init__(self, fichier):
        self.fichier = fichier
        self.liste1 = []
        self.liste2 = []
        self._charger_donnees()

    def _charger_donnees(self):
        with open(self.fichier, 'r') as f:
            for ligne in f:
                num1, num2 = map(int, ligne.split())
                self.liste1.append(num1)
                self.liste2.append(num2)

    def partie_1(self):
        liste1_triee = sorted(self.liste1)
        liste2_triee = sorted(self.liste2)
        
        distance = sum(abs(num1 - num2) for num1, num2 in zip(liste1_triee, liste2_triee))
        return distance

    def partie_2(self):
        return sum(num * self.liste2.count(num) for num in self.liste1)

if __name__ == "__main__":
    lien_fichier = "Input_Data/Day_1.txt"
    calculateur = Day_1(lien_fichier)
    
    print(calculateur.partie_1())
    print(calculateur.partie_2())