'''
Napisati program koji sa tastature učitava dužinu u centimetrima i na ekran
ispisuje dužinu u metrima i centimetrima.
'''

duzina = int(input("Unesite duzinu u centimetrima: "))

metri = duzina // 100
centimetri = duzina % 100

print(f"Duzina {duzina} cm = {metri} m i {centimetri} cm.")
