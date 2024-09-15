#Rekurzija je metod rješavanja problema koji podrazumijeva razbijanje problema 
#na manje subprobleme dok se ne dođe do baznog slučaja (problema koji se može trivijalno riješiti).
#Rekurzija omogućava pisanje elegantnih rješenja za veoma komplikovane probleme.

#Svaki rekurzivni algoritam mora da ispuni tri uslova.
    #1. Rekurzivni algoritam mora da ima bazni slučaj
    #2. Rekurzivni algoritam mora da poziva sam sebe
    #3. Rekurzivni algoritam mora da mijenja svoje stanje i da se "pomjera" ka baznom slučaju

#Napisati rekurzivnu funkciju koja racuna faktorijel broja.

def faktorijel(n):
    if n == 1:
        return 1
    
    return n * faktorijel(n-1)


n = int(input("Unesite prirodan broj:"))

if(n < 1):
    print("n mora biti prirodan broj.")

print(f"{n}! = {faktorijel(n)}")