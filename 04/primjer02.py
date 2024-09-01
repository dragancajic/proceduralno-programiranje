'''
                    ---Metode listi---
'''

L = []
# lista.append(element) - dodaje element na kraj liste

L.append(5)
L.append(2.51)
print("Lista nakon dodavanja elemenata:", L)
# u listu je moguće dodati (i) drugu listu
L.append(["a", "b", "c"])
print(L)

print("-" * 60)

print("Duzina liste:", len(L))

print("-" * 60)

# dodavanje elementa na željenu poziciju: `lista.insert(pozicija, element)`
L.insert(0, True)
print("Lista nakon umetanja:", L)

print("-" * 60)

# pristup elementima liste ["a", "b", "c"] koja se nalazi u listi L
print("L[3][2]:", L[3][2])
# L[3] je lista ["a", "b", "c"], pa je onda L[3][2] treći element liste
# ["a", "b", "c"], tj. "c".

print("-" * 60)

# uklanjanje elemenata liste:
print("L prije uklanjanja:", L)
# `lista.remove(element)` - uklanja element iz liste
L.remove(5)
print("L nakon uklanjanja:", L)

print("-" * 60)

# lista.pop() izbacuje zasljednji element iz liste i kao rezultat
# vraća taj element!
x = L.pop()
print("Uklonjen je element:", x)
print("L nakon uklanjanja:", L)

print("-" * 60)

# lista.pop(index) - izbacuje element na zadatom indeksu i kao rezultat
# vraća taj element!
y = L.pop(0)
print("Uklonjen je element:", y)
print("L nakon uklanjanja:", L)

print("-" * 60)

# uklanjanje svih elemenata iz liste
L.append(1)
L.append(2)
print("Lista prije uklanjanja:", L)
L.clear()
print("Lista nakon uklanjanja:", L)

# više o metodama listi možete vidjeti na
# https://www.w3schools.com/python/python_ref_list.asp
