
#Ispistati kvadrat svakog broja iz date liste zaokruzen na tri decimale
brojevi = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

kvadratiZaokruzeno = list(map(lambda x: round(x * x, 3), brojevi))
print(f"Kvadrati brojeva {brojevi} zaokruzeni na tri decimale: {kvadratiZaokruzeno}")