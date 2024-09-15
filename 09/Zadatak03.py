#Napisati rekurzivnu funkciju koja racuna sumu prvih n prirodnih brojeva

def sumaN(n):
    if n == 1:
        return 1
    
    return n + sumaN(n-1)

n = int(input("Unesite prirodan broj:"))

if(n < 1):
    print("n mora biti prirodan broj.")

print(f"Suma prvih {n} prirodnih brojeva je {sumaN(n)}")