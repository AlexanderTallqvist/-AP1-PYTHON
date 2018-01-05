# coding=utf-8
# Inlämning 2 | Uppg. 1, 2, 3
# Alexander Tallqvist


# Uppg. 1

# Högsta antalet poäng för varje vitsord
poang = [14,17,20,23,26,30]

def kursvitsord(vitsord):
    if vitsord <= max(poang):
        for index, number in enumerate(poang):
            if vitsord <= number:
                print "Kursvitsordet blir:", index
                break
    else:
        print "Tentresultatet maste vara mindre an", max(poang)


vitsord = input("Ange tentresultat: ")
kursvitsord(vitsord)


# Uppg. 2

artal = input("Ange ett artal: ")

if artal >= 1600:

    if (artal % 4 == 0) and not(artal % 100 == 0) or (artal % 400 == 0):
        print artal, "ar ett skottar!"
    else:
        print artal, "ar inte ett skottar!"

else:
    print "Artalet maste vara 1600 eller storre."


# Uppg. 3

# Beräkna tullen och momsen för produkten
def berakna_tull_moms(produkt, slutvarde):
    if produkt == 1:
        tull_tot = slutvarde * 0.035
        moms_tot = (tull_tot + slutvarde) * 0.24
        utskrift(tull_tot, moms_tot)
    else:
        tull_tot = 0
        moms_tot = (tull_tot + slutvarde) * 0.10
        utskrift(tull_tot, moms_tot)


# Skriv ut resultaten
def utskrift(tull, moms):
    tot_summa =  0 if tull < 10 else tull
    tot_summa += 0 if moms < 10 else moms

    tull_format  = formatera(tull)
    moms_format  = formatera(moms)
    total_format = formatera(tot_summa)

    tull_utsk = "Tull: " + tull_format + " (uppbars inte)" if tull < 10 else "Tull: " + tull_format + " (uppbars)"
    moms_utsk = "Moms: " + moms_format + " (uppbars inte)" if moms < 10 else "Moms: " + moms_format + " (uppbars)"

    print tull_utsk, "\n", moms_utsk, "\n", "-" * 20, "\nTotalt uppbars", total_format


# Formulera talen till rätt format t.ex.(12.20)
def formatera(tal):
    return format(tal, '.2f').zfill(5)


produkt   =  input("Vilken typ av produkt? 1 = DVD, 2 = bok: ")
slutvarde =  input("Vad ar bestallningens slutvarde? (inkl. postkostnader): ")
berakna_tull_moms(produkt, slutvarde)
