'''
Dat je štap dužine n metara i lista cijena svakog komada štapa. 
Odrediti maksimalnu cijenu koja se može dobiti prodajom n metara stapa.
Npr. ako je dužina štapa 8 i vrijednosti različitih dijelova su date na sljedeći način:

dužina    | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8  
--------------------------------------------
cijena    | 1 | 5 | 8 | 9 |10 |17 |17 |20

Onda je maksimalna vrijednost koja se može dobiti prodajom 
8 metara stapa 22 (presjecanjem na dva komada dužine 2 i 6).
Maksimalna vrijednost koja se moze dobiti prodajom 4 metra stapa je
10 (presjecanjem na dva komada dužine po 2 metra).
'''

def podijeliStap(cijene, n):
    #na pocetku je tabela popunjena nulama
    tabela = [0 for _ in range(n+1)] 
    podjele = [None for _ in range(n+1)]  #pratimo pozicije na kojima sijecemo stap
    
    #potrebno je kreirati tabelu tako da je tabela[i] najveca zarada koju je moguce ostvariti
    #prodajom i metara stapa
    for i in range(1, n + 1):
        maksimalnaVrijednosti = -float("inf")
        pozicijaPodjele = None
        for j in range(i):
            if cijene[j] + tabela[i-j-1] > maksimalnaVrijednosti:
                maksimalnaVrijednosti = cijene[j] + tabela[i-j-1]
                pozicijaPodjele = j
        tabela[i] = maksimalnaVrijednosti
        podjele[i] = pozicijaPodjele + 1
     
    #kreiranje niza podjela
    rezultat = []
    duzina = n
    while duzina > 0:
        rezultat.append(podjele[duzina])
        duzina -= podjele[duzina]
    
    #print(tabela)
    #print(podjele)
    return tabela[n], rezultat

cijene = [1, 5, 8, 9, 10, 17, 17, 20]
#cijene = [2, 5, 9, 10, 12, 13, 15, 16]
n = 8

maksimalnaVrijednost, podjele = podijeliStap(cijene, n)
print(f"Maksimalna vrijednost stapa je: {maksimalnaVrijednost}.")
print("  Stap je rezan na pozicijama:", podjele)