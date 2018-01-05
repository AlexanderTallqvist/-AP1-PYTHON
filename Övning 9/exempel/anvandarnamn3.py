'''
anvandarnamn3.py
Linda Mannila, 2007; Åke Gustavson 2011
Program som läser in namn från en fil, skapar användarnamn av
dessa och lagrar dem i en fil. Programmet genererar ett fel om filen
namn.txt inte existerar.

Modifiering av anvandarnamn.py, så att man använder myFiles
och får därmed felhantering direkt
'''
import myFiles
import string

def processa_fil(namn,anv_namn):
    anvN = []

    for line in myFiles.filList(namn):
        # Delar upp strängen i två delar vid blanktecknet
        [forN,efterN] = line.split(' ')
        # Skapar en ny sträng som består av den första bokstaven i förnamnet
        # och de sju första bokstäverna i efternamnet,
        # gör alla bokstäver i strängen små och sätter i lista
        anvN.append(string.lower(forN[0] + efterN[:7])) 

    # Skiver filen om det fanns något att skriva
    if anvN :
        myFiles.filCreate(anv_namn,string.join(anvN,'\n'))
        print "Användarnamn... OK"
        print "Lagrade i filen", anv_namn


processa_fil("namn.txt","anv_namn.txt")

