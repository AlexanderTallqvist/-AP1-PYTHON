# coding=utf-8
# Övning 5 | Uppg. 1, 2, 3, 4, 5, 6, 7
# Alexander Tallqvist


# Uppg. 1

# tal = 10
#
# while tal >= 0:
#     print tal
#     tal = tal - 1
#
# print "Pang!"


# Uppg. 2

# while True:
#
#     nummer = input("Ange ett tal mellan 0 och 100: ")
#
#     if nummer >= 0 and nummer <= 100:
#         print "Tack."
#         break
#     else:
#         continue;


# Uppg. 3

# tot = 0
#
# while True:
#
#     nummer = input("Ange ett tal (du ska upp till 100): ")
#     tot += nummer
#
#     if tot >= 100:
#         print "Du kom over 100. Du kom till", tot
#         break
#     else:
#         print "Du ar nu vid", tot
#         continue;


# Uppg. 4

# def compare(a, b):
#     if a > b :
#         return 1
#     if a == b:
#         return 0
#     else:
#         return -1
#
# svar = compare(20, 20)
# print svar


# Uppg. 5 och 6

# def isEven(x):
#     return x % 2 == 0
#
# svar = isEven(11)
# print svar
#
# def isOdd(x, func):
#     return not(func(x))
#
# svar = isOdd(11, isEven)
# print svar


# Uppg. 7

# def c2f(param):
#     fahr = (9/5.0) * param + 32
#     return fahr
#
# def f2c(param):
#     cels = (5/9.0) * (param - 32)
#     return cels
#
# while True:
#
#     temp = raw_input("Valj C for att ange graderna i celsius.\nValj F for att ange graderna i fahrenheit: ")
#
#     if temp == "c" or temp == "C":
#         cels = input("Ange graderna i celcius: ")
#         fahrenheit = c2f(cels)
#         print "Blir", fahrenheit, "grader fahrenheit."
#         break;
#
#     elif temp == "f" or temp == "F":
#         fahr = input("Ange graderna i fahrenheit: ")
#         celsius = f2c(fahr)
#         print "Blir", celsius, "grader celsius."
#         break;
#     else:
#         print "Du maste ange C eller F"
#         continue
