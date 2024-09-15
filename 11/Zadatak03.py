'''
Problem pokrivanja skupa:
Dat je skup X i familija njegovih podskupova F.
Potrebno je pronaci najmanji broj podskupova iz F takvih da pokrivaju
citav skup X.
'''

def brojNovihPokrivanja(X, trenutnoPokriveni, kandidat):
    return len((X.difference(trenutnoPokriveni)).intersection(kandidat))
    

def pokrivanjeSkupa(X, F):  
    #X predstavlja skup koji se treba "pokriti"
    #F predstavlja familuju skupova sa kojom se "pokriva" skup X

    trenutnoPokriveni = set()  
    rjesenje = []

    while(trenutnoPokriveni != X):
        najviseNovihPokrivanja = 0
        najboljiKandidat = None
        for kandidat in F:
            if kandidat not in rjesenje:
                novaPokrivanja = brojNovihPokrivanja(X, trenutnoPokriveni, kandidat)
                if novaPokrivanja > najviseNovihPokrivanja:
                    najviseNovihPokrivanja = novaPokrivanja
                    najboljiKandidat = kandidat

        if najviseNovihPokrivanja == 0:
            return None
        
        trenutnoPokriveni = trenutnoPokriveni.union(najboljiKandidat)
        rjesenje.append(najboljiKandidat)


    return rjesenje

X = {1, 2, 3, 4, 5}
F = [{1, 2, 3}, {2, 4, 5}, {2, 3}, {4, 5}, {1, 5}, {1, 4}]

#X = {1, 2, 3, 4, 5, 6}
#F = [{1, 2}, {3, 4}, {4, 5}, {3, 6}, {5}, {6}]

pokrivanje = pokrivanjeSkupa(X, F)
if pokrivanje:
    print(f"Skup {X} se moze pokriti podksupovima {pokrivanje}.")
else:
    print(f"Skup {X} nije moguce pokriti familijom podskupova {F}.")