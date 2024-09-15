#Napisati rekurzivnu funkciju koja broj iz dekadnog zapisa prebacuje u binarni

def dekadniUBinarni(n):
    if n == 0:
        return 0
    
    return n % 2 + 10 * dekadniUBinarni(n // 2)

n = int(input("Unesite prirodan broj:"))

if(n < 1):
    print("n mora biti prirodan broj.")

print(f"({n})\u2081\u2080 = ({dekadniUBinarni(n)})\u2082")