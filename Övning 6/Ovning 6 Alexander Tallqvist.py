# coding=utf-8
# Övning 6 | Uppg. 1, 2, 3, 4, 5, 6, 7, 8
# Alexander Tallqvist


# Uppg. 1

name = "Alexander"

for letter in name:
    print letter


# Uppg. 2

for number in range(99, -3, -3):
    print number
print "PANG!"


# Uppg. 3

words = ["mamma!", "pappa!", "python!"]

for word in words:
    print "Hej", word


# Uppg. 4

# 1. Ber användaren mata in antal tal hen vill summera
# 2. Ber användaren om dessa tal
# 3. Skriver ut summan av talen


# Uppg. 5

for number in range(3, 15, 3):
    print number

for number in range(-10, 320, 110):
    print number

for number in range(-1, -9, -2):
    print number


# Uppg. 6

antal = input("Antal stjarnor? ")

for stars in range(antal, 0, -1):
    print "*" * stars


# Uppg. 7

antal = input("Hur manga tal? ")
summa = 0.0

for i in range(antal):
    tal = input("Mata in ett tal: ")
    summa = summa+tal

print "Medeltal:", round(summa/antal, 2)


# Uppg. 8

grans = input("Mata in den over gransen? ")
kvadrat = 0
kuben   = 0

for number in range(1, grans + 1):
    kvadrat += number ** 2
    kuben   += number ** 3

print "Summan av kvadraterna:", kvadrat
print "Summan av kuberna:", kuben
