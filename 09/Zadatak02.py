#Napisati rekurzivnu funkciju koja racuna n-ti Fibonacijev broj.

def fibonaci(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return fibonaci(n-1) + fibonaci(n-2)

n = int(input("Unesite prirodan broj:"))

if(n < 1):
    print("n mora biti prirodan broj.")

print(f"{n}. Fibonacijev broj je {fibonaci(n)}")