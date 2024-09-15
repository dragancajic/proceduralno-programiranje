'''
Sa tastature se unosi prirodan broj N, a nakon toga još n brojeva.
Na ekran ispisati unesene brojeve na sljedeći način:
prvo se ispisuju svi brojevi koji su palindromi, a nakon njih brojevi
koji nisu palindromi.
'''
import sys

def obrnuto(n):
    '''
    funkcija koja vraća broj dobijen obrtanjem cifara broja n
    npr., za n = 123, funkcija kao rezultat vraća broj 321
    '''
    n_obrnuto = 0

    while n != 0:
        cifra = n % 10
        n_obrnuto *= 10
        n_obrnuto += cifra
        n //= 10

    return n_obrnuto

def palindrom(n):
    '''
    funkcija koja provjerava da li je broj n palindrom
    '''
    return n == obrnuto(n)

def palindrom1(n):
    '''
    funkcija koja provjerava da li je broj n palindrom
    '''
    n_string = str(n)

    return n_string == n_string[::-1]


N = int(input("Unesite prirodan broj n: "))

if N <= 0:
    sys.exit("n mora biti prirodan broj.")

L = []
for i in range(N):
    broj = int(input("Unesite broj: "))

    if palindrom(broj):
        L.insert(0, broj)
    else:
        L.append(broj)

print("Ispis unesenih brojeva u trazenom poretku:")
for e in L:
    print(e, end= " ")
print()
