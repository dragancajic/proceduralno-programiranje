def sumaListe(lista):
    if len(lista) == 0:
        return 0
    
    return lista[0] + sumaListe(lista[1:])

L = [1, 2, -3, 5, -10, 12]

print(f"Suma elemenata liste {L} je : {sumaListe(L)}")