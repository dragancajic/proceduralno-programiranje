'''
Rasporediti miševe u rupe. 
Dato je n miševa i n rupa koje su smještene na pravoj liniji.
U svaku rupu može se smjestiti samo jedan miš. 
Miš može stajati na svojoj poziciji
i može se pomjerati korak po korak ulijevo i udesno po x osi.
Svako pomjeranje traje jedan minut. 
Odrediti najmanje potrebno vrijeme da se svi misevi rasporede u rupe. 
'''

def rasporediMiseve(pozicijeMiseva, pozicijeRupa):
    brojMiseva = len(pozicijeMiseva)
    brojRupa = len(pozicijeRupa)

    if brojMiseva != brojRupa:
        exit("Brojevi miseva i brojevi rupa moraju da se podudaraju.")

    pozicijeMiseva.sort()
    pozicijeRupa.sort()

    maksimalnoVrijeme = 0
    for i in range(brojMiseva):
        if abs(pozicijeMiseva[i] - pozicijeRupa[i]) > maksimalnoVrijeme:
            maksimalnoVrijeme = abs(pozicijeMiseva[i] - pozicijeRupa[i])

    return maksimalnoVrijeme

pozicijeMiseva = [-10, -79, -79, 67, 93, -85, -28, -94]
pozicijeRupa = [-2, 9, 69, 25, -31, 23, 50, 78]

#pozicijeMiseva =  [4, -4, 2]
#pozicijeRupa = [4, 0, 5]

potrebnoVrijeme = rasporediMiseve(pozicijeMiseva, pozicijeRupa)
print(f"Posljednji mis ce uci u rupu za {potrebnoVrijeme} minute.")