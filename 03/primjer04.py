'''
                ---Prosljeđivanje argumenata funkciji---
'''

def uvecaj(n):
    """
    Funkcija `uvecaj`/inkrementuj.
    """
    n += 1
    print("Vrijednost unutar funkcije:", n)

N = 5
uvecaj(N)  # 6
print("Vrijednost nakon izvrsavanja funkcije:", N)  # 5
