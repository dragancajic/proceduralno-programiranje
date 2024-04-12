#                           ---Petlje---

# Petlje koristima kada u nekom programu jednu ili više naredbi
# trebamo izvršiti nekoliko puta.

# Primjer: Napisati program koji na ekran 100 puta ispisuje poruku
# "Programski jezik Python".

# for petlja
for i in range(100):
    print("Programski jezik Python")

print("-" * 20)

# while petlja
i = 0
while i < 100:
    print("Programski jezik Python")
    i += 1
