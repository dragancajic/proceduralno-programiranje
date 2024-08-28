'''
Sa tastature se unose tri cijela broja.
Na ekranu ispisati najveći od unesenih brojeva.
'''

a = int(input("Unesite prvi broj:  "))
b = int(input("Unesite drugi broj: "))
c = int(input("Unesite treci broj: "))

if a >= b and a >= c:
    print("Najveci broj je", a)
elif b >= a and b >= c:
    print("Najveci broj je", b)
else:
    print("Najveci broj je", c)
