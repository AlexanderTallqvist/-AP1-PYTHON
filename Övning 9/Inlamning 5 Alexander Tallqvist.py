# -*- coding: cp1252 -*-
# Inlämning 5 | Uppg. 1, 2, 3
# Alexander Tallqvist


# Uppg. 1 A

summa = input("Ange summan pengar (t.ex. 100, 1000 eller 10000): ")
tid   = input("Ange antalet ar som pengarna ska sparas (t.ex. 3, 5 eller 10): ")
prcnt = input("Ange ranteprocenten (t.ex. 3, 5 eller 10): ")

prcnt_varde = (prcnt / 100.0) + 1
sparade_pengar = 0;
spara_tid = tid

while tid > 0:
    if sparade_pengar == 0:
        sparade_pengar = (summa * prcnt_varde)
        tid-= 1
    else:
        sparade_pengar = (sparade_pengar * prcnt_varde)
        tid-= 1

print "Med en investering pa", summa, "och efter en tid pa", spara_tid, "ar, kommer du tillsammans att ha", format(sparade_pengar, '.2f')


# Uppg. 2

import string

infil = open("medbyten.txt", "r")
new_content = ""

for line in infil.readlines():
    new_content += line.replace("\n", " ")

infil.close()

infil_new = open("noNewLines.txt", "w")
infil_new.write(new_content)
infil_new.close()

print "Filen ar fardig."


# Uppg. 3

import string

# Kryptera/dekryptera med förskjutningschiffer
def get_message(key, message):
    # At the beginning, the encrypted message is empty
    encrypted_message = ""

    # Encrypt each character in the message separately
    for character in message:
        old_ascii = ord(character)

        if character in string.uppercase:
            new_ascii = (old_ascii + key - 65) % 26 + 65
            new_char  = chr(new_ascii)
            encrypted_message += new_char

        elif character in string.lowercase:
            new_ascii = (old_ascii + key - 97) % 26 + 97
            new_char  = chr(new_ascii)
            encrypted_message += new_char

        else:
            encrypted_message += character

    # Output the encrypted message
    return encrypted_message


# Bryt kryptering med förskjutningschiffer
def break_crypt(message):
    break_list = []

    for key in range(0, 26):
        encrypted_message = ""

        for character in message:
            old_ascii = ord(character)

            if character in string.uppercase:
                new_ascii = (old_ascii - key - 65) % 26 + 65
                new_char  = chr(new_ascii)
                encrypted_message += new_char

            elif character in string.lowercase:
                new_ascii = (old_ascii - key - 97) % 26 + 97
                new_char  = chr(new_ascii)
                encrypted_message += new_char

            else:
                encrypted_message += character

        break_list.append(encrypted_message + " The key is: " + str(key))

    return break_list


# Function that saves files
def save_file(message):
    file_save_name = raw_input("Name of the new file (with extension): ")
    save_to_file = open(file_save_name, "w")

    if type(message) is str:
        save_to_file.write(message)
        save_to_file.close()

    else:
        message_to_save = ""
        for line in message:
            message_to_save += line + "\n"

        save_to_file.write(message_to_save)
        save_to_file.close()

    print "=" * 40, "\n"
    print "File saved"

# Function that starts the program
def main():
    method     = raw_input("Do you want to encrypt, decrypt or break a message? (Type: ENC, DEC or BRK): ")
    file_read  = input("Should the message be read from a file? (1 = YES, 0 = NO): ")
    file_save  = input("Should the new message be saved to a file? (1 = YES, 0 = NO): ")

    # Get the message from the correct source
    if file_read == 0:
        message = raw_input("Input the message: ")

    if file_read == 1:
        file_read_name = raw_input("Name of the file that should be read (with extension): ")
        opened_file = open(file_read_name, "r")
        message = ""

        for line in opened_file.readlines():
            message += line

        opened_file.close()


    # Call correct function with parameters
    if method == "ENC" or method == "enc":
        key = input("Input the key (an integer value): ")
        key = key * 1
        new_message = get_message(key, message)

        if file_save == 1:
            save_file(new_message)
        else:
            print "=" * 40, "\n"
            print new_message


    elif method == "DEC" or method == "dec":
        key = input("Input the key (an integer value): ")
        key = key * -1
        new_message = get_message(key, message)

        if file_save == 1:
            save_file(new_message)

        else:
            print "=" * 40, "\n"
            print new_message

    elif method == "BRK" or method == "brk":
        new_message = break_crypt(message)

        if file_save == 1:
            save_file(new_message)

        else:
            print "=" * 40, "\n"
            for line in new_message:
                print line

    else:
        print "=" * 40, "\n"
        print "Wrong type of method."

main()
