'''
wordcounter.py
Linda Mannila 2007
Läser in en fil och skriver ut antalet ord som den innehåller.
'''

import string

def numwords(s):
    ''' Returns the number of words in a long string'''
    # Splits the string at each blank
    list = string.split(s) 
    return len(list)


def open_file():
    ''' Reads in a filename from the user and opens it'''
    while True:
        try:
            fil = raw_input("Filnamn? ")
            infil = open(fil, "r")
            break
        except IOError:
            print "Filen existerar inte."
    return infil

def process_file(f):
    ''' Goes through the file, line by line, keeping track of the total
    number of words'''
    words = 0
    for line in f:
        words += numwords(line)
    f.close()
    return words


def main():
    ''' Main function that runs the program '''
    infile = open_file()
    count = process_file(infile)
    print "The file contains %d words." % count


