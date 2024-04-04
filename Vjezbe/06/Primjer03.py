# Čitanje sadržaja datoteke - liniju po liniju

file = open("ulaz.txt", "r")

while(True):
    line = file.readline()

    if(line == ""):
        break

    print(line, end="")

file.close()
