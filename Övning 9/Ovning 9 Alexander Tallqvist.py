# -*- coding: cp1252 -*-
# Övning 9 | Uppg. 1, 2, 3, 4
# Alexander Tallqvist


# Uppg. 1

infil = open("mall.txt", "r")

for line in infil.readlines():
    print line

infil.close()


# Uppg. 2

infil = open("siffror.txt", "r")
lista = []

for line in infil.readlines():
    nmbr = int(line)
    lista.append(nmbr)


infil.close()

max_value = max(lista)
min_value = min(lista)

print "Det storsta vardet ar", max_value
print "Det minsta vardet ar", min_value


# Uppg. 3

infil = open("siffror2.txt", "r")
lista = []
new_content = ""

for line in infil.readlines():
    nmbr = int(line) + 1
    lista.append(nmbr)
    new_content += str(nmbr) + "\n"

infil.close()

infil_new = open("siffror2.txt", "w")
infil_new.write(new_content)
infil_new.close()

max_value = max(lista)
min_value = min(lista)

print "Det storsta vardet ar", max_value
print "Det minsta vardet ar", min_value


# Uppg. 4

import webbrowser

infil = open("links.txt", "r")
meny = []

for line in infil.readlines():
    meny.append(line)

def skriv_meny():
    print "Mina favoritlänkar"
    print "------------------"

    nummer = 1

    for url in meny:
        print nummer, url
        nummer += 1

    val = input("\nVilken sida vill du oppna? ")
    return meny[val-1]

webbrowser.open(skriv_meny())
