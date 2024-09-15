import sys, getopt

def main(argv):

    ifile =""
    ofile=""
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile", "ofile" ])    
    except getopt.GetoptError:
        print("Forma na terminalu treba da bude vjezbe5.py -i <filename> -o <filename>")
        exit(1) 
    
    print(opts)
    print(args)

    for opt, val in opts:
        if opt == "-h":
            print("ovo je help ==> ", "Forma na terminalu treba da bude vjezbe5.py -i <filename> -o <filename>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            ifile = val
        elif opt in ("-o", "--ofile"):
            ofile = val
        
    print("parametri koji su prosljedjeni ====> \n")
    print("input file====> ", ifile)
    print("output file ===> ", ofile)

if __name__ == "__main__":

    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))

    main(sys.argv[1:])
    
 #cd putanja
#python vjezba5.py -i ulazniFajl.txt -o izlazniFajl.txt