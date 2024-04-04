# Čitanje sadržaja datoteke - liniju po liniju

file = open("ulaz.txt", "r")

#print(file)
# <_io.TextIOWrapper name='ulaz.txt' mode='r' encoding='UTF-8'>

for line in file:
    print(line, end="")

file.close()
