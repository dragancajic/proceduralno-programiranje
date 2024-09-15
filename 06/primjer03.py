'''
~ Primjer 3 ~

file.readline() <-- Čitanje sadržaja datoteke - LINIJU PO LINIJU
'''

file = open("ulaz.txt", "r", encoding='utf-8')

while True:
    line = file.readline()

    if line == "":
        break

    print(line, end="")

file.close()
