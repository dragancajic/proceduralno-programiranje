#Pronalazenje n-tog Fibonacijevog broja - tabuliranje
import time

def FibonacciDP(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    else:
        tabela = [0] * (n+1)
        tabela[1] = 1

        for i in range(2, n+1):
            tabela[i] = tabela[i-1] + tabela[i-2]

        return tabela[n]
    
def FibonacciRekurzivno(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return FibonacciRekurzivno(n-1) + FibonacciRekurzivno(n-2)

n = 40
print(f"Pronalazenje {n}. Fibonacijevog broja:")

start = time.time()
broj = FibonacciRekurzivno(n)
end = time.time()

print("\tRekurzivni pristup:")
print(f"\t\tRezultat: {broj}.\n\t\tPotrebno vrijeme:{end - start}")

start = time.time()
broj = FibonacciDP(n)
end = time.time()

print("\tDinamicko programiranje:")
print(f"\t\tRezultat: {broj}.\n\t\tPotrebno vrijeme:{end - start}")