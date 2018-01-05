# coding=utf-8
# Övning 2 | Uppg. 1, 2, 6, 7, 8, 9, 10
# Alexander Tallqvist



# Uppg 1.

# Variabeln namn är av typen "string".
namn = "Alexander"
print 'Hej', namn
print type(namn)



# Uppg 2.

# input() tar in värden eller uttryck, och strävar
# sedan efter att evaluera de inmatade värdena.
# 3.14 = int
x = input("We're using input(): ")
print type(x)

# raw_input() tar in exakt vad användaren matar in, och
# omformulerar det inmatade värdet till en "string".
# '3.14' = string
x = raw_input("We're using raw_input(): ")
print type(x)



# Uppg 6.

# a)
# Fel, variabelnamn kan inte ha mellanrum i sej.
#tre dussin = 37

# b)
# Rätt, variabeln pi tilldelas ett "float" värde.
pi = 3.1994

# c)
# Fel, "==" bör användas för att se om två värden är lika.
#3.1416 = pi

# d)
# Fel, variabelnamn kan inte börja med en siffra.
#6december = "Finlands nationaldag"



# Uppg 7.

celsius = input("Ange temperatur i Celcius: ")
fahrenheit = (9/5.0) * celsius + 32
print celsius, "grader Celsisu blir", fahrenheit, "grader Fahrenheit."



# Uppg 8.

# Siffror som matas in till raw_input() konverteras
# till "string" värden.
namn = raw_input('Vad heter du? ')
print 'Hej', namn
print type(namn)



# Uppg 9.

# Strängar som matas in till input() går inte att evalueras,
# och programmet kommer därför att köra fast.
age = input('How old are you? ')
print 'You are', age, "years old."
print type(age)



# Uppg 10.

print "Give me two numbers."
tal1 = input('Number 1: ')
tal2 = input('Number 2: ')

try:
    kvoten = tal1/(tal2 * 1.0)
    print tal1, "/", tal2, "=", kvoten

except:
    print "You can't divide by 0."

print "Thank you."
