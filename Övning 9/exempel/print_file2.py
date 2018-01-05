'''
print_file2.py
Linda Mannila, 2007
Demonstrates reading a file line by line and printing its contents on the
screen. Uses exception handling.'''

def print_file(infile):
    ''' Prints the contents of a file to the screen '''
    for line in infile.readlines():
        print line,
    infile.close()
    
def open_file():
    ''' Asks the user for a filename and opens the file'''
    while True:
        try:
            filename = raw_input('Which file do you want to print? ')
            infile = open(filename, 'r')
            return infile
        except IOError:
            print "The file doesn't exist."
  
def main():
    f = open_file()
    print_file(f)


main()
