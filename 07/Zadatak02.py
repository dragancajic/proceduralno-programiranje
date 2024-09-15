#U datoteci brojevi.txt se u svakoj liniji nalaze nalaze brojevi razdvojeni zarezom.
#Za svaku liniju datoteke ispisati sumu parnih i neparnih brojeva u toj liniji.

from functools import reduce

def paran(n):
    return n % 2 == 0

with open("brojevi.txt", "r") as ulaznaDatoteka:
    for line in ulaznaDatoteka:
        brojevi = line.split(", ")
        brojevi = list(map(lambda x: int(x), brojevi))
        parniBrojevi = list(filter(lambda x: paran(x), brojevi))
        neparniBrojevi = list(filter(lambda x: not paran(x), brojevi))

        print("Linija:", line, end="")
        print("\tSuma parnih brojeva:", reduce(lambda a, b : a + b, parniBrojevi))
        print("\tSuma neparnih brojeva:", reduce(lambda a, b : a + b, neparniBrojevi))