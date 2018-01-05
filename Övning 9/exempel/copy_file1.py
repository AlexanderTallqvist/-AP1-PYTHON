#-*- coding: cp1252 -*-
'''
copy_file1.py
Linda Mannila, 2007
Kopierar en fil givet att den finns i samma katalog som detta program.
'''

try:
    file1 = raw_input('Which file do you want to copy? ')
    file2 = raw_input('What should be the name of the copied file? ')

    input = open(file1, 'r')
    output = open(file2, 'w')

    for line in input:
        output.write(line)
    
    input.close()
    output.close()

    print 'The file %s now contains a copy of the file %s' % (file2, file1)

except IOError:
    print "The file %s doesn't exist." % file1
