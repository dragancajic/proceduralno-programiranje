def binarnaPretraga(lista, element, lijevi, desni):
    #bazni slucaj - element se ne nalazi u listi
    if lijevi > desni:
        return -1

    srednji = (lijevi + desni) // 2

    if lista[srednji] == element:
        return srednji #bazni slucaj - element je pronadjen u listi
    elif lista[srednji] < element:
        #pretraga desne polovine liste
        return binarnaPretraga(lista, element, srednji + 1, desni)
    else:
        #pretraga lijeve polovine liste
        return binarnaPretraga(lista, element, lijevi, srednji - 1)

L = [1, 2, 5, 6, 11, 12, 15, 21, 24, 27, 30]
e = 24

indeks = binarnaPretraga(L, e, 0, len(L) - 1)

if indeks != -1:
    print(f"Element {e} je pronadjen na indeksu {indeks}")
else:
    print(f"Element {e} nije pronadjen u listi")
