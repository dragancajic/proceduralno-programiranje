'''
                    ---Funkcije---
'''
# U Pajtonu, pored ugrađenih funkcija možemo koristiti i funkcije
# koje smo sami kreirali.

# sintaksa
# def imeFunkcije(argumenti):
#     blok naredbi
#     ...
#
#     return rezultat  # <-- opciono

# Napisati funkciju koja za argumente uzima dva cijela broja, a
# kao rezultat vraća zbir ta dva broja.

def zbir_brojeva(a, b):
    """
    Zbir brojeva a i b.
    """
    zbir = a + b
    return zbir

# kraći oblik
# def zbir_brojeva(a, b):
#     return a + b

A = 6
B = 10
C = zbir_brojeva(A, B)
print("C =", C)
