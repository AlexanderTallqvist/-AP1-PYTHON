'''
anvandarnamn2.py
Linda Mannila, 2007
Program som l�ser in namn fr�n en fil, skapar anv�ndarnamn av
dessa och lagrar dem i en fil. Programmet genererar ett fel om filen
namn.txt inte existerar.
Utvidgad version som �ven kontrollerar att filen namn.txt existerar.
'''
import string

def oppna_filer():
    while True:
        try:
            filnamn = raw_input("Mata in ett filnamn: ")
            infil = open(filnamn, "r")
            utfil = open("anvnamn.txt", "w")
            break
        except IOError:
            print "Filen existerar inte."
    return infil, utfil

def processa_fil(infil, utfil):

    for line in infil:
        # Delar upp str�ngen i tv� delar vid blanktecknet
        forN, efterN = string.split(line)
        # Skapar en ny str�ng som best�r av den f�rsta bokstaven i f�rnamnet
        # och de sju f�rsta bokst�verna i efternamnet
        anvN = (forN[0] + efterN[:7]) 
        # G�r alla bokst�ver i str�ngen sm�
        anvN = string.lower(anvN) 
        utfil.write(anvN + "\n")

    # St�nger filerna
    infil.close()
    utfil.close()
            

def main():
    infil, utfil = oppna_filer()
    processa_fil(infil, utfil)
    print "Anv�ndarnamn... OK"
    print "Lagrade i filen anv_namn.txt."


main()
