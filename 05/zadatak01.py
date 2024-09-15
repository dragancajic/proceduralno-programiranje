'''
Sa tastature se unosi cijeli broj n.
Na ekranu ispisati informaciju o tome koliko se različitih
cifara nalazi u zapisu broja n i koje su to cifre.
'''

def skup_razlicitih_cifara(n):
    '''broj razlicitih cifara broja'''
    if n < 0:
        n *= -1

    skup_cifara = set()
    while n != 0:
        cifra = n % 10
        skup_cifara.add(cifra)
        n //= 10

    return skup_cifara

N = int(input("Unesite cijeli broj n: "))

razlicite_cifre = skup_razlicitih_cifara(N)
BROJ_RAZLICITIH_CIFARA = len(razlicite_cifre)

print(f"U zapisu broja {N} se nalazi {BROJ_RAZLICITIH_CIFARA} razlicitih cifara.")
print("Te cifre su:", razlicite_cifre)
