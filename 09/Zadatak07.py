#Napisati rekurzivnu funkciju koja pronalazi najmanji element liste.

def najmanjiElement(lista):
    if len(lista) == 1:
        return lista[0]
    
    return min(lista[0], najmanjiElement(lista[1:]))


L = [5, -2, 3, -4, 15, 21, -11]

print(f"Najmanji elemenata liste {L} je : {najmanjiElement(L)}")