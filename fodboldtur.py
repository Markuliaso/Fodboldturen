import pickle

filename = 'betalinger.pk'

fodboldtur ={}

def afslut():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()
    print("Programmet er afsluttet!")

def printliste():
    for item in fodboldtur.items():
        print(item) #Printer alle ting i dicten fodboldtur
    menu()



def printlistecounter():
    count = 0
    for gutter in fodboldtur.keys():
        print(count, gutter)
        count +=1 #for hver person i fodboldtur, tælles der fra 0 og op, så man kan se hvem man vælger
    menu()


def betal():
    person = int(input("vælg person"))
    x = int(input("indtast betalt beløb"))
    valgtdudekey = list(fodboldtur)[person] #fra inputet "person" bliver tilsvarende person valgt.
    print(valgtdudekey)
    fodboldtur[valgtdudekey] += x #den valgte person får sat x antal kr ind i betalt beløb
    printliste()

def menu():
    print("MENU")
    print("1: Print liste")
    print("2: Print personer")
    print("3: Betaling")
    print("4: Afslut program")
    valg = input("Indtast dit valg:")
    if (valg == '1'):
        printliste()
    if (valg == '2'):
        printlistecounter()
    if (valg =='3'):
        betal()
    if (valg == '4'):
        afslut()

infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()
menu()