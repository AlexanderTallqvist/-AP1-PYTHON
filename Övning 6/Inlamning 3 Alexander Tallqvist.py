# coding=utf-8
# Inlämning 3 | Uppg. 1, 2, 3, 4
# Alexander Tallqvist


# Uppg. 1

def wow(amount):
    if amount <=0:
        print "Dont be a spoilsport!"
    elif amount == 1:
        print "WoW"
    else:
        print "WoW"
        wow(amount - 1);


antal_wow = input("Hur manga 'WoW' vill du se? ")
wow(antal_wow)


# Uppg. 2

def sos(amount):
    if amount <=0:
        return "Dont be a spoilsport!"
    elif amount == 1:
        return "SOS!"
    else:
        return "SOS!" + sos(amount - 1)


antal_sos = input("Hur manga 'SOS!' vill du ropa? ")
print sos(antal_sos)


# Uppg. 3

def summa(n):
    if n == 1:
        return 1
    else:
        return (1.0 / n) + summa(n - 1);

print summa(2)


# Uppg. 4

def antalet_burkar(n):
    if n == 1:
        return 1
    else:
        return n * n + antalet_burkar(n - 1);

lager = input("Hur manga antal lager? ")
print antalet_burkar(lager)
