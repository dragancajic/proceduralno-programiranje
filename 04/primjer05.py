'''
                    ---Lista listi (matrica)---
'''

matrica = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
          ]

# ispis elemenata matrice

# prvi način
for i in range(len(matrica)):
    for j in range(len(matrica[i])):
        print(matrica[i][j], end=" ")
    print()

print("-" * 5)

# drugi način
for vrsta in matrica:
    for broj in vrsta:
        print(broj, end=" ")
    print()
