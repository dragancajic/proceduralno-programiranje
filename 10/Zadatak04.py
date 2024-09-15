#Napisati fukciju koja rjesava problem trgovackog putnika (Traveling salesman problem)

def TSPPomoc(graf, start, posjecen, trenutnaPozicija, n, brojac, trenutnaDuzina, trenutrniPut, sviPutevi):
    #provjeravamo da li smo dosli do posljednjeg cvora i da li je on povezan sa posljednjim
    if brojac == n and graf[trenutnaPozicija][start]:
        sviPutevi.append((trenutnaDuzina + graf[trenutnaPozicija][start], trenutrniPut.copy() + [start]))
        return
 
    for i in range(n):
        if not posjecen[i] and graf[trenutnaPozicija][i]:
            posjecen[i] = True
            trenutrniPut.append(i)
            TSPPomoc(graf, start, posjecen, i, n, brojac + 1, 
                trenutnaDuzina + graf[trenutnaPozicija][i], trenutrniPut, sviPutevi)
            
            #backtracking
            posjecen[i] = False
            trenutrniPut.pop()

def TSP(graf, start):
    n = len(graf)
    posjecen = [False] * n
    posjecen[start] = True
    sviPutevi = []

    TSPPomoc(graf, start, posjecen, start, n, 1, 0, [start], sviPutevi)

    return sviPutevi

graf = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

putevi = TSP(graf, 0)
print("Svi putevi:")
for put in putevi:
    print("  ", put)

print()

puteviSortirano = sorted(putevi, key=lambda x:x[0])
print("Najkraci put:", ' - '.join(str(x) for x in puteviSortirano[0][1]))
print("Duzina puta :", puteviSortirano[0][0])