'''
anvandarnamn2.py
Linda Mannila, 2007
Program som läser in namn från en fil, skapar användarnamn av
dessa och lagrar dem i en fil. Programmet genererar ett fel om filen
namn.txt inte existerar.
Utvidgad version som även kontrollerar att filen namn.txt existerar.
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
        # Delar upp strängen i två delar vid blanktecknet
        forN, efterN = string.split(line)
        # Skapar en ny sträng som består av den första bokstaven i förnamnet
        # och de sju första bokstäverna i efternamnet
        anvN = (forN[0] + efterN[:7]) 
        # Gör alla bokstäver i strängen små
        anvN = string.lower(anvN) 
        utfil.write(anvN + "\n")

    # Stänger filerna
    infil.close()
    utfil.close()
            

def main():
    infil, utfil = oppna_filer()
    processa_fil(infil, utfil)
    print "Användarnamn... OK"
    print "Lagrade i filen anv_namn.txt."


main()
