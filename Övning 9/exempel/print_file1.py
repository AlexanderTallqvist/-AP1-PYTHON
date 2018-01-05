#-*- coding: cp1252 -*-
'''
print_file1.py
Linda Mannila, 2007
Demonstrates reading a file and printing its contents on the screen.
'''

filnamn = raw_input("Ge in ett filnamn: ")
infil = open(filnamn,'r')
for rad in infil.readlines():
   print rad,

infil.close()

