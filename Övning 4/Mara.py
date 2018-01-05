# coding=utf-8
# Inlämning 2 | Uppg. 1, 2, 3
# Alexander Tallqvist

produkt = input("Vilken typ a produkt? 1 = DVD, 2 = bok ")
pris = input("Vad är beställningens slutvärde? (inkl. postkostnader) ")
if (produkt == 1):
    tull = 0.035 * pris
    moms = 0.24 * pris
    if (tull <= 10) and (moms <= 10):
        print tull, "(uppbärs inte)"
        print moms, "(uppbärs inte)"
    elif (tull >= 10) and (moms >= 10):
        print "Tull:", tull, "(uppbärs)"
        print "Moms:", moms, "(uppbärs)"
    elif (tull <= 10) and (moms >= 10):
        print "Tull:", tull, "(uppbärs inte)"
        print "Moms:", moms, "(uppbärs)"

elif (produkt == 2):
    tull = 0.0
    moms = 0.10 * pris
    if (moms <= 10):
        print tull, "(uppbärs inte)"
        print moms, "(uppbärs inte)"
    elif (moms >= 10):
         print "Tull:", tull, "(uppbärs inte)"
         print "Moms:", moms, "(uppbärs)"
