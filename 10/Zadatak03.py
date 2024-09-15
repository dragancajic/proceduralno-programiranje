#Data je lista pozitivnih cijelih brojeva i suma S.
#Potrebno je napisati program koji pronalazi sve kombinacije brojeva
#iz liste kojima je suma jednaka S. Brojevi mogu biti izvučeni iz liste neograničen
#broj puta. Kombinacije elemenata moraju biti sortirane nerastuce po broju elemenata u kombinaciji.
#Elementi svake pojedniacne kombinacije moraju biti sortirani u nerastucem poretku.
#Ukoliko nema takvih kombinacija ispisati poruku o gresci.

def pronadjiKombinacije(lista, trenutnaKombinacija, trazenaSuma, kombinacije, start):
    if trazenaSuma == 0:
        kombinacije.append(trenutnaKombinacija.copy())
        return
    
    for i in range(start, len(lista)):
        if trazenaSuma - lista[i] >= 0:
            trenutnaKombinacija.append(lista[i])
            pronadjiKombinacije(lista, trenutnaKombinacija, trazenaSuma - lista[i], kombinacije, i)
            
            #backtracking
            trenutnaKombinacija.pop()

def sveKombinacije(lista, trazenaSuma):
    kombinacije = []
    trenutnaKombinacija = []
    lista = sorted(list(set(lista)))
    pronadjiKombinacije(lista, trenutnaKombinacija, trazenaSuma, kombinacije, 0)
    return kombinacije
            
L = [2, 4, 6, 8]
S = 8
kombinacije = sveKombinacije(L, S)

if kombinacije:
    print(f"Kombinacije koje daju sumu {S}:")
    for kombinacija in kombinacije:
        print("  ", kombinacija)
else:
    print(f"Nema kombinacija koje sumu {S}.")