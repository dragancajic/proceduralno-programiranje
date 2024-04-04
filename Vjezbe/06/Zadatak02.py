# Sličnost `s` između dva skupa `A` i `B` se definiše na sljedeći način:
# `s(A,B)=|A∩B|/|A∪B|`.
# U datoteci `skupovi.txt` u svakoj liniji zapisani su elementi nekog skupa
# razdvojeni zarezom. Na primjer, linija:
# 1, 2, 6, 7, 10
# predstavlja skup S = {1, 2, 6, 7, 10}.
# Napisati program koji u datoteci `skupovi.txt` pronalazi dva najsličnija
# skupa i ispisuje ih na ekran, kao i informaciju o tome kolika je sličnost
# između ta dva skupa.


def slicnostSkupova(A, B):
    unija = A.union(B)
    presjek = A.intersection(B)

    return len(presjek)/len(unija)

skupovi = []
with open ("skupovi.txt", "r") as ulaz:
    for linija in ulaz:
        info = linija.strip().split(", ")
        #print(info)
        skup = set(info)
        skupovi.append(skup)

#print(skupovi)

indeks1 = None
indeks2 = None
maxSlicnost = 0

for i in range(0, len(skupovi) - 1):
    for j in range (i + 1, len(skupovi)):
        trenutnaSlicnost = slicnostSkupova(skupovi[i], skupovi[j])
        #print(f"trenutna slicnost: {trenutnaSlicnost}, indeksi: {i}, {j}")
        if(trenutnaSlicnost > maxSlicnost):
            indeks1 = i
            indeks2 = j
            maxSlicnost = trenutnaSlicnost

print(f"\nSkupovi sa najvecom slicnosti su:\n{skupovi[indeks1]} i {skupovi[indeks2]}")
print("Slicnost izmedju njih je:", maxSlicnost)
