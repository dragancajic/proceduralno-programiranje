'''
~ Primjer 4 ~

for петља <-- Čitanje sadržaja datoteke - LINIJU PO LINIJU
'''

file = open("ulaz.txt", "r", encoding='utf-8')

#print(file)
# <_io.TextIOWrapper name='ulaz.txt' mode='r' encoding='UTF-8'>

for line in file:
    print(line, end="")

file.close()
