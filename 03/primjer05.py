'''
Promenljive koje se definišu unutar neke funkcije nisu vidljive
izvan te funkcije.
'''

def ispisi():
    """
    `ispisi` vrijednost lokalne promjenljive (unutar funkcije)
    """
    x = 10
    print("Ispis u funkciji.\nx =", x)

ispisi()
# print("Ispis van funkcije:", x)  # <-- greska
# NameError: name 'x' is not defined
