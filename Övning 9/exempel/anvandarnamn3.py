'''
anvandarnamn3.py
Linda Mannila, 2007; �ke Gustavson 2011
Program som l�ser in namn fr�n en fil, skapar anv�ndarnamn av
dessa och lagrar dem i en fil. Programmet genererar ett fel om filen
namn.txt inte existerar.

Modifiering av anvandarnamn.py, s� att man anv�nder myFiles
och f�r d�rmed felhantering direkt
'''
import myFiles
import string

def processa_fil(namn,anv_namn):
    anvN = []

    for line in myFiles.filList(namn):
        # Delar upp str�ngen i tv� delar vid blanktecknet
        [forN,efterN] = line.split(' ')
        # Skapar en ny str�ng som best�r av den f�rsta bokstaven i f�rnamnet
        # och de sju f�rsta bokst�verna i efternamnet,
        # g�r alla bokst�ver i str�ngen sm� och s�tter i lista
        anvN.append(string.lower(forN[0] + efterN[:7])) 

    # Skiver filen om det fanns n�got att skriva
    if anvN :
        myFiles.filCreate(anv_namn,string.join(anvN,'\n'))
        print "Anv�ndarnamn... OK"
        print "Lagrade i filen", anv_namn


processa_fil("namn.txt","anv_namn.txt")

