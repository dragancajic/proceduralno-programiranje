'''
Na realnoj pravoj dat je interval [a, b].
Napisati program koji ispisuje dužinu podintervala koji se nalazi
na pozitivnom dijelu prave.
'''
import sys  # YES! √

a = float(input("Unesite a: "))
b = float(input("Unesite b: "))

if a >= b:
    #exit("Niste unijeli korektan interval")  # NameError: name 'exit' is not defined
    sys.exit("Niste unijeli korektan interval")

if b >= 0:
    if a >= 0:
        print(f"Duzina pozitivnog dijela intervala je {b-a}.")
    else:
        print(f"Duzina pozitivnog dijela intervala je {b}.")
else:
    print("Citav interval se nalazi na negativnom dijelu prave")
