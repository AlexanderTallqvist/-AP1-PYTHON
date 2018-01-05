# -*- coding: cp1252 -*-
'''
copy_file2.py
Linda Mannila, 2007
Kopierar en fil f�rutsatt att den finns i samma katalog som programmet sj�lvt.
Anv�nder metoden readlines() f�r att l�sa in inneh�llet ur filen.
'''

try:
    file1 = raw_input('Which file do you want to copy? ')
    file2 = raw_input('What should be the name of the copied file? ')

    input = open(file1, 'r')
    lines = input.readlines()
    input.close()

    output = open(file2, 'w')
    output.writelines(lines)
    output.close()

    print 'The file %s now contains a copy of the file %s' % (file2, file1)

except IOError:
    print "The file %s doesn't exist." % file1

