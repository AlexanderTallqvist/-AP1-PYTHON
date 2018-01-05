'''
anvandarnamn.py
Linda Mannila, 2007
Program som l�ser in namn fr�n en fil, skapar anv�ndarnamn av
dessa och lagrar dem i en fil. Programmet genererar ett fel om filen
namn.txt inte existerar.
'''
import string

def processa_fil():
    infil = open("namn.txt", "r")
    utfil = open("anv_namn.txt", "w")

    for line in infil.readlines():
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
    processa_fil()
    print "Anv�ndarnamn... OK"
    print "Lagrade i filen anv_namn.txt."

main()
