#Napisati program koji ispisuje sve podliste date liste

def podlistePomoc(lista, trenutnaPodlista, start, podliste):
    podliste.append(trenutnaPodlista.copy())
    for i in range(start, len(lista)):
        trenutnaPodlista.append(lista[i])

        podlistePomoc(lista, trenutnaPodlista, i + 1, podliste)

        #backtracking
        trenutnaPodlista.pop()
 
def svePodliste(lista):
    trenutnaPodlista = []
    podliste = []
    start = 0
    podlistePomoc(lista, trenutnaPodlista, start, podliste)

    return podliste   

L = [0, 1, 2, 3]
podliste = svePodliste(L)

print(f"Lista {L} ima {len(podliste)} podlisti. Te podliste su\n  {podliste}.")