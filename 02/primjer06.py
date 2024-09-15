'''
Napisati program koji ispisuje sve karaktere rečenice
koja se unosi sa tastature.
'''

recenica = input("Unesite recenicu sa tastature: ")

print("For petlja (`range` i `len`):")
for i in range(len(recenica)):
    print(recenica[i], end='_')
print('\n', "-" * 15)

print("For petlja (`enumerate`):")
for i, slovo in enumerate(recenica):
    print('slovo:', recenica[i], 'indeks:', i)
print('\n', "-" * 15)

print("For each:")
for slovo in recenica:
    print(slovo, end='_')
print('\n', "-" * 25)

print("While petlja:")
i = 0
while i < len(recenica):
    print(recenica[i], end='_')
    i += 1
print('\n', "-" * 25)

print("Ispis karaktera unazad (for petlja):")
for i in range(len(recenica) - 1, -1, -1):
    print(recenica[i], end='_')
print('\n', "-" * 25)

print("Ispis karaktera unazad (while petlja):")
i = len(recenica) - 1
while i >= 0:
    print(recenica[i], end='_')
    i -= 1
print('\n', "-" * 25)
