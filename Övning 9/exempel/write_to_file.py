#-*- coding: cp1252 -*-
'''
write_to_file.py
Linda Mannila, 2007
Demonstrates writing to a file.
'''

filename = raw_input("Enter the name for a file to write the information to: ")
output = open(filename,'w')

text = raw_input("Enter text to store in the file: ")
output.write(text)

print 'The text "%s" has been stored in the file %s' %(text, filename)

output.close()
