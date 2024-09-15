import sys
import re
import getopt


if __name__ == "__main__":
    ulazniFajl = ""
    izlazniFajl = ""
    zadatak = ""

    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "h:i:o:z:")
    except getopt.GetoptError:
        print("Nekorektan poziv!\n")
        exit(1)

    print(opts)
    print(args)

    for o, a in opts:
        if o == "-h":
            print("Ovo je help, provjerite poziv")
            sys.exit()
        elif o in ['-i']:
            ulazniFajl = a
        elif o in ['-o']:
            izlazniFajl = a
        elif o in ['-z']:
            zadatak = a
        else:
            print("Neispravna opcija.")
            sys.exit()

    try:
        f = open(ulazniFajl, 'r')
        f.close()
    except IOError:
        print("Nije moguce otvoriti ulazni fajl")

    regExp = r'^[A-Z][a-z]+,+\s+[A-Z][a-z]+\s+\d+:+\s+\d{4}|\d{5}|\d{6}$'
    zad1_luksuzni = set()
    marke = dict()

    with open(ulazniFajl, 'r') as file:
        line = file.readline()
        i = 0
        while line != '':
            if re.match(regExp, line):
                res = (line.replace(',', ' ')).split()
                print(res)
                if res[1] not in marke:
                    marke[i] = res[1]
                    i += 1

                if int(res[-1]) > 50000:
                    zad1_luksuzni.add(res[0])
                elif 10000 <= int(res[-1]) <= 20000:
                    for i in marke:
                        if res[2] == marke[i]:
                            marke[i] += res[2]

            line = file.readline()

    print(zad1_luksuzni)
    print(marke)

    if zadatak == '1':
        with open(izlazniFajl, "w") as w:
            for i in zad1_luksuzni:
                w.write(i + '\n')

    #elif zadatak == '2':

