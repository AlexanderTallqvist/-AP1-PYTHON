'''
textanalys.py
Linda Mannila, 2007
Tema: Filer, funktioner, felhantering och string-modulen
Skriver ut antalet ord, rader och tecken som finns i en fil. Demonstrerar
funktioner, filhantering och stränghantering med hjälp av modulen string.
'''

import string

def start():
    '''Skriver ut en rubrik'''
    print '---------------------------------'
    print
    print '         Textanalys              '
    print
    print '---------------------------------'
    print

def antal_ord(s):
    '''Beräknar antalet ord i en sträng'''
    list = string.split(s)
    return len(list)

def oppna_fil():
    '''Öppnar den fil användaren vill använda'''
    while True:
        try:
            fil = raw_input("Filnamn? ")
            infil = open(fil, "r")
            return infil
        except IOError:
            print "Filen finns inte."

def processa(infil):
    '''Går igenom filen och skriver ut information om den'''
    ord_total = 0
    rader = 0
    tecken = 0

    for rad in infil:
        ord_total += antal_ord(rad)
        rader += 1
        tecken += len(rad)
    
    print "Filen innehåller %d ord, %d rader och %d tecken." % (ord_total, rader, tecken)
    infil.close()

#-------- Huvudprogram
start()
fil = oppna_fil()
processa(fil)
