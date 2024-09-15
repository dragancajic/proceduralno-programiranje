#Pronalazenje n-tog Fibonacijevog broja - memoizacija
import time

def FibonacciDP(n, cache = {}):
    if n in cache:
        return cache[n]
    
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:
        cache[n] = FibonacciDP(n-1) + FibonacciDP(n-2)
        return cache[n]
    
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