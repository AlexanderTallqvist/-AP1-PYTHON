# coding=utf-8
# Övning 2 | Uppg. 1, 2, 3, 4, 5, 6, 7, 8
# Alexander Tallqvist


# Uppg. 1

def medelvitsord(studnamn, tent1, tent2, tent3):
    medel = (tent1 + tent2 + tent3) / 3.0
    print "Medelvitsordet för " + studnamn + " blir", medel


print "Ange studerandes namn, och tre tentvitsord."

namn = raw_input("Ange namn: ")
res1 = input("Tent 1 resultat: ")
res2 = input("Tent 2 resultat: ")
res3 = input("Tent 3 resultat: ")

medelvitsord(namn, res1, res2, res3)


# Uppg. 2

def skriv_stjarnor():
    print("*****\n" * 4)

skriv_stjarnor()


# Uppg. 3

def skriv_tecken(tecken):
    utskrivning = tecken * 5
    print((utskrivning + "\n") * 4)

skriv_tecken("A")

# OBS1 = Vi skriver inte ut parametern x, utan strängen "xxxxx".
# OBS2 = Vi skriver inte ut parametern x, utan parameterne / eller variabeln xxxxx (som inte existerar).


# Uppg. 4

def annualSalary(monthlySalary):
    print(monthlySalary * 12)

salary = 4000
annualSalary(salary)


# Uppg. 5

def hejssan(namn, efternamn):
    print "Hej", namn, efternamn

fornamn = raw_input("Vad är dit förnamn? ")
efternamn = raw_input("Vad är dit efternamn? ")

hejssan(fornamn, efternamn)


# Uppg. 6

def new_line():
  print

def three_lines():
  new_line()
  new_line()
  new_line()

def nine_lines():
  three_lines()
  three_lines()
  three_lines()

def clear_screen():
  nine_lines()
  nine_lines()
  three_lines()
  three_lines()
  new_line()

print "First Line."
three_lines()
print "Second Line."
nine_lines()
clear_screen()
print "Last line."


# Uppg. 7

# Funktionerna måste definieras före de kan användas.
# (NameError: 'clear_screen is not defiend')
clear_screen()

def new_line():
  print

def three_lines():
  new_line()
  new_line()
  new_line()

def nine_lines():
  three_lines()
  three_lines()
  three_lines()

def clear_screen():
  nine_lines()
  nine_lines()
  three_lines()
  three_lines()
  new_line()

print "First Line."
three_lines()
print "Second Line."
nine_lines()
clear_screen()
print "Last line."


# Uppg. 8

# Flyttning 1: Python har noterat att funktionen new_line() existerar
# och kan vid behov "hoppa" till den, och exekvera funktionen.
def three_lines():
  new_line()
  new_line()
  new_line()

def new_line():
  print

def nine_lines():
  three_lines()
  three_lines()
  three_lines()

def clear_screen():
  nine_lines()
  nine_lines()
  three_lines()
  three_lines()
  new_line()

print "First Line."
three_lines()
print "Second Line."
nine_lines()
clear_screen()
print "Last line."


# Flyttning 2: Python har INTE noterat att funktionen new_line() existerar,
# eftersom att inläsningen av koden har "pausat" då three_lines() kallades,
# och tolken "hoppade" tillbaka till funktionen.
def three_lines():
  new_line()
  new_line()
  new_line()

def nine_lines():
  three_lines()
  three_lines()
  three_lines()

def clear_screen():
  nine_lines()
  nine_lines()
  three_lines()
  three_lines()
  new_line()

print "First Line."
three_lines()

def new_line():
  print

print "Second Line."
nine_lines()
clear_screen()
print "Last line."
