#U datoteci izrazi.txt u svakoj liniji se nalaze dva broja i operacija. Potrebno je procitati
#svaku liniju datoteke i na ekran ispisati vrijednost izraza koji se dobije primjenom operacije u liniji.
#Napomene: Pretpostaviti da su u datoteci samo operacije +, -, * i /.

try:
    with open ("izrazi.txt", "r") as ulaznaDatoteka:
        for line in ulaznaDatoteka:
            izraz = line.split(" ")
            try:
                lijeviOperand = float(izraz[0])
                operacija = izraz[1]
                desniOperand = float(izraz[2])

                if operacija == "+":
                    print(f"{lijeviOperand} {operacija} {desniOperand} = {lijeviOperand + desniOperand}")
                elif operacija == "-":
                    print(f"{lijeviOperand} {operacija} {desniOperand} = {lijeviOperand - desniOperand}")
                elif operacija == "*":
                    print(f"{lijeviOperand} {operacija} {desniOperand} = {lijeviOperand * desniOperand}")
                else:
                    print(f"{lijeviOperand} {operacija} {desniOperand} = {lijeviOperand / desniOperand}")
            except ValueError:
                print("Nevalidni operandi u liniji:", line, end="")
            except ZeroDivisionError:
                print("Dijeljenje nulom u liniji  :", line, end="")
except FileNotFoundError:
    print("Nije moguce otvoriti datoteku.")
finally:
    print("Zavrsena obrada datoteke.")