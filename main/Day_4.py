class Day_4:
    def __init__(self, fichier):
        self.fichier = fichier
        self.grille = self._charger_donnees()
        self.lgn = len(self.grille)
        self.col = len(self.grille[0]) if self.grille else 0

    def _charger_donnees(self):
        with open(self.fichier, 'r') as file:
            return [list(line.strip()) for line in file.readlines()]

    def partie_1(self, mot="XMAS"):
        word_length = len(mot)
        nbr = 0
        directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]

        def is_word_at(x, y, dx, dy):
            for i in range(word_length):
                nx, ny = x + i * dx, y + i * dy
                if nx < 0 or ny < 0 or nx >= self.lgn or ny >= self.col or self.grille[nx][ny] != mot[i]:
                    return False
            return True

        for i in range(self.lgn):
            for j in range(self.col):
                for dx, dy in directions:
                    if is_word_at(i, j, dx, dy):
                        nbr += 1
        return nbr

    def partie_2(self):
        nbr = 0
        lettres = {"M", "S"}
        
        for i in range(1, self.lgn - 1):
            for j in range(1, self.col - 1):
                if self.grille[i][j] == "A":
                    if {self.grille[i - 1][j - 1], self.grille[i + 1][j + 1]} == lettres and \
                       {self.grille[i - 1][j + 1], self.grille[i + 1][j - 1]} == lettres:
                        nbr += 1
        
        return nbr

if __name__ == "__main__":
    lien_fichier = "Input_Data/Day_4.txt"
    calculateur = Day_4(lien_fichier)
    
    print(calculateur.partie_1())
    print(calculateur.partie_2())
