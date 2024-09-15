#U datoteci brojevi.txt se u svakoj liniji nalaze nalaze brojevi razdvojeni zarezom.
#Na ekran ispisati samo one linije u kojima se nalazi n ili vise prostih brojeva (broj n se unosi sa tastature).

def prost(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

n = int(input("Unesite prirodan broj n:"))

if(n < 1):
    exit("n mora biti prirodan broj.")

print(f"Linije u kojima se nalazi vise od {n} prostih brojeva:")
with open("brojevi.txt", "r") as ulaznaDatoteka:
    for line in ulaznaDatoteka:
        brojevi = line.split(", ")
        brojevi = list(map(lambda x: int(x), brojevi))
        prostiBrojevi = list(filter(lambda x: prost(x), brojevi))
        
        if(len(prostiBrojevi) >= n):
            print("\t", line, end="")