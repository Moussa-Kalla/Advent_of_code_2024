lien_fichier = 'Input_Data/Day_13.txt'

with open(lien_fichier, "r") as file:
    data = file.read().strip().split("\n\n") 


def partie1(data):
    coins = 0
    for machine in data:
        lignees = machine.split("\n")
        btn_a = [int(i[2:]) for i in lignees[0].split(": ")[1].split(", ")] 
        btn_b = [int(i[2:]) for i in lignees[1].split(": ")[1].split(", ")]
        prize = [int(i[2:]) for i in lignees[2].split(": ")[1].split(", ")] 

        denominator = btn_b[1] * btn_a[0] - btn_b[0] * btn_a[1]
        if denominator == 0:
            continue  

        times_b = (prize[1] * btn_a[0] - prize[0] * btn_a[1]) / denominator
        if not times_b.is_integer():
            continue  

        times_a = (prize[0] - btn_b[0] * times_b) / btn_a[0]
        if not times_a.is_integer() or times_a < 0 or times_b < 0 or times_a > 100 or times_b > 100:
            continue  

        coins += int(times_a) * 3 + int(times_b)

    return coins

resulta = partie1(data)
print(resulta)

def partie2(data):

    coins = 0

    for machine in data:
        lines = machine.split("\n")
        btn_a = [int(i[2:]) for i in lines[0].split(": ")[1].split(", ")] 
        btn_b = [int(i[2:]) for i in lines[1].split(": ")[1].split(", ")]
        prize = [int(i[2:]) + 10**13 for i in lines[2].split(": ")[1].split(", ")] 

        denominator = btn_b[1] * btn_a[0] - btn_b[0] * btn_a[1]
        if denominator == 0:
            continue 

        times_b = (prize[1] * btn_a[0] - prize[0] * btn_a[1]) / denominator
        if not times_b.is_integer():
            continue 

        times_a = (prize[0] - btn_b[0] * times_b) / btn_a[0]
        if not times_a.is_integer() or times_a < 0 or times_b < 0:
            continue  

        coins += int(times_a) * 3 + int(times_b)

    return coins


resulta = partie2(data)
print(resulta)

