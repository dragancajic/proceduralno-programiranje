'''
Napisati funkciju koja provjerava da li je broj paran.
Sa tastature se unose brojevi sve dok se ne unese nula.
Na ekranu ispisati informaciju o tome koliko je uneseno
parnih brojeva.
'''

def paran(n: int) -> bool:
    """
    Paran broj.
    """
    if n % 2 == 0:
        return True
    # else:  # <-- else je "višak"
    return False

BROJ_PARNIH = 0

while True:
    broj = int(input("Unesite broj: "))

    if broj == 0:
        break

    if paran(broj):
        BROJ_PARNIH += 1

print(f"Uneseno je {BROJ_PARNIH} parnih brojeva.")
