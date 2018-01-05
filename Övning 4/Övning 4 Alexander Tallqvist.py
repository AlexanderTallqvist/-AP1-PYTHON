# coding=utf-8
# Övning 4 | Uppg. 1, 2, 3, 4, 5, 6, 7
# Alexander Tallqvist


# Uppg. 1

tal1 = input("Mata in det forsta talet: ")
tal2 = input("Mata in det andra talet: ")

if tal1 > tal2:
    print tal1, "ar storre an", tal2
elif tal1 < tal2:
    print tal2, "ar storre an", tal1
else:
    print "Talen ar lika stora"


# Uppg. 2

#a FALSE
#b TRUE
#c FALSE
#d TRUE
#e TRUE


# Uppg. 3

temp = raw_input("Valj C for att ange graderna i celsius.\nValj F for att ange graderna i fahrenheit: ")

def cels_to_fahr(param):
    fahr = (9/5.0) * param + 32
    print param, "grader celcius ar", fahr, "grader fahrenheit."

def fahr_to_cels(param):
    cels = (5/9.0) * (param - 32)
    print param, "fahrenheit ar", cels, "grader celsius."

if temp == "c" or temp == "C":
    cels = input("Ange graderna i celcius: ")
    cels_to_fahr(cels)
elif temp == "f" or temp == "F":
    fahr = input("Ange graderna i fahrenheit: ")
    fahr_to_cels(fahr)
else:
    print "Du maste ange C eller F"


# Uppg. 4

A = input("Give a boolean value for the variable A (True/False): ")
B = input("Give a boolean value for the variable B (True/False): ")
C = input("Give a boolean value for the variable C (True/False): ")

if A or B:
    print "TRUE"
elif not A and not B and not C:
    print "TRUE"
else:
    print "FALSE"


# Uppg. 5

minuter = input("Ange antal minuter: ")

timmar = minuter / 60
over   = minuter % 60

print "Det ar", timmar, "timmar och", over, "minuter."


# Uppg. 6

def faktura(namn, pris, leverans):
    if not leverans:
        print "\nFaktura"
        print "-" * 20
        print namn, "\t" , pris
        print "-" * 20
        print "Totalpris\t", pris
    else:
        leveransPris = berakna_leverans(pris)
        print "\nFaktura"
        print "-" * 20
        print namn, "\t" , pris
        print "Hemleverans\t", leveransPris
        print "-" * 20
        print "Totalpris\t", pris + leveransPris



def berakna_leverans(pris):
    if pris < 10:
        return 3
    else:
        return 2


namn = raw_input("Mata in produkt: ")
pris = input("Mata in pris ")
leverans = input("Hemleverans (0 = nej, 1 = ja)")

faktura(namn, pris, leverans)


# Uppg. 7

dagkonto = input("Mata in saldot pa dagskontot: ")
sparkonto = input("Mata in saldot pa Sparkonto: ")

kostnad = 0 if dagkonto > 1000 or sparkonto > 1500 else 0.15;
print "Serviceavgiften blir", kostnad, "euro"
