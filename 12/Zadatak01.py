'''
Napisati funkciju koja za argumente uzima parametre n i k,
a kao rezultat vraća vrijednost binomnog koeficijenta n nad k. 
'''

def binomniKoeficijent(n, k):
    #kreiramo tabelu binomnih koeficijenta C
    #na pocetku je tabela C popunjena nulama 
    C = [[0 for _ in range(k + 1)] for _ in range(n + 1)] 
    
    #popunjavamo tabelu C tako da je 
    #C[i][j] binomni koeficijent i nad j
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            #bazni slucaj
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                #neka je C(n, k) binomni koeficijent
                #vrijedi da je C(n, k) = C(n-1, k-1) + C(n-1, k)
                C[i][j] = C[i-1][j-1] + C[i-1][j]

    return C[n][k]

n = int(input("Unesite n:"))
k = int(input("Unesite k:"))

if n <= 0 and k < 0:
    exit("Nekorektan unos brojeva n i k.")

print(f"{n} nad {k}: {binomniKoeficijent(n, k)}.")    