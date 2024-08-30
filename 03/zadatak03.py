'''
Napisati program koji na ekranu iscrtava pravogli trougao.
Dužina katete pravouglog trougla je prirodan broj koji
se unosi sa tastature.
'''

a = int(input("Unesite duzinu katete: "))

for i in range(a):
    for j in range(a):
        if j == 0:
            print("*", end="")
        elif i == a-1:
            print("*", end="")
        elif i == j:
            print("*", end="")
        else:
            print(" ", end= "")
    print()

# Zadaća: Uraditi isto koristeći while petlju.
