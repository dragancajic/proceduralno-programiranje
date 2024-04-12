# Napisati program koji ispisuje sve karaktere rečenice
# koja se unosi sa tastature.

recenica = input("Unesite recenicu sa tastature: ")

print("For petlja:")
for i in range(len(recenica)):
    print(recenica[i])
print("-" * 15)

print("For each:")
for slovo in recenica:
    print(slovo)
print("-" * 15)

print("While petlja:")
i = 0
while i < len(recenica):
    print(recenica[i])
    i += 1
print("-" * 15)

print("Ispis karaktera unazad (for petlja):")
for i in range(len(recenica) - 1, -1, -1):
    print(recenica[i])
print("-" * 15)

print("Ispis karaktera unazad (while petlja):")
i = len(recenica) - 1
while i >= 0:
    print(recenica[i])
    i -= 1
