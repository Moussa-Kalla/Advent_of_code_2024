import re

class Day_3:
    def __init__(self, fichier):
        self.fichier = fichier
        self.data = self._charger_donnees()

    def _charger_donnees(self):
        with open(self.fichier, 'r') as file:
            return file.read()

    def partie_1(self):
        pattern = r"mul\((\d+),(\d+)\)"
        corresp = re.findall(pattern, self.data)
        return sum(int(x) * int(y) for x, y in corresp)

    def partie_2(self):
        pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
        instructions = re.findall(pattern, self.data)
        
        enabled = True
        resulta = 0
        
        for inst in instructions:
            if inst[0] == "do()":
                enabled = True
            elif inst[0] == "don't()":
                enabled = False
            elif enabled and inst[0].startswith("mul"):
                resulta += int(inst[1]) * int(inst[2])

        return resulta

if __name__ == "__main__":
    lien_fichier = "Input_Data/Day_3.txt"
    calculateur = Day_3(lien_fichier)
    
    print(calculateur.partie_1())
    print(calculateur.partie_2())



