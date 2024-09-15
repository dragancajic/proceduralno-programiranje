'''
Data je lista L sa sljedecom osobinom: 
	L[i] predstavlja broj skokva unaprijed koji se moze izvesti sa indeksa i.
Potrebno je pronaci minimalan broj skokova koje je potrebno izvesti da bi se doslo od 
prvog do posljednjeg indeksa liste. Ukoliko postoji vise rjesenja ispisati samo jedno.
Na primjer, ako je L = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9] potrebna su tri skoka
kako bi se doslo od prvog do posljednjeg indeksa liste.
Indeksi preko koji se prelazi su: 1, 4 i 10.
'''

#pomocna funkcija koja vraca minimalan broj skokova potreban da se dodje 
#od trenutnog do posljednjeg indeksa liste
def brojSkokova(lista, trenutniIndeks, posljednjiIndeks, cache, posjeceniIndeksi): 
	if trenutniIndeks == posljednjiIndeks:
		#dosli smo do posljednjeg indeksa liste
		return 0

	if cache[trenutniIndeks] != -1: 
		return cache[trenutniIndeks] 

	najmanjeSkokova = float("inf") 
	sljedeciIndeks = None
	#prolazimo kroz sve moguce kombinacije skokova od trenutnog indeksa do posljednjeg indeksa 
	#biramo opciju sa najmanjim brojem skokova 
	for j in range(lista[trenutniIndeks], 0, -1): 
		#provjeravamo da li smo "iskocili" iz liste 
		if trenutniIndeks + j <= posljednjiIndeks: 
			#skoci na poziciju indeks + j i nekon toga nastavi dalje sa skakanjem
			skokovaDoKraja = 1 + brojSkokova(lista, trenutniIndeks + j, posljednjiIndeks, cache, posjeceniIndeksi)
			if skokovaDoKraja < najmanjeSkokova:
				najmanjeSkokova = skokovaDoKraja
				sljedeciIndeks = trenutniIndeks + j

	cache[trenutniIndeks] = najmanjeSkokova 
	if sljedeciIndeks != None:
		posjeceniIndeksi[trenutniIndeks] = [sljedeciIndeks] + posjeceniIndeksi[sljedeciIndeks]
	return cache[trenutniIndeks] 


def najmanjiBrojSkokova(lista):
	cache = [-1 for _ in range(len(lista))]
	posjeceniIndeksi = [[] for _ in range(len(lista))]

	brojSkokova(lista, 0, len(lista) - 1, cache, posjeceniIndeksi)

	#print(cache)
	#print(posjeceniIndeksi)

	return cache[0], posjeceniIndeksi[0]


L = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
#L = [3, 2, 1, 2, 1, 1]
potrebanBrojSkokova, skokovi = najmanjiBrojSkokova(L)

print(f"Potrebno je najmanje {potrebanBrojSkokova} skoka da bi se doslo od pocetka do kraja liste.\n"
	  f"  Prelazi se preko sljedecih indeksa: {skokovi}")