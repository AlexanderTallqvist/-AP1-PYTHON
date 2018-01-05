# -*- coding: cp1252 -*-
# Övning 8 | Uppg. 1, 2, 3
# Alexander Tallqvist

import string

#### The Substitution Cipher ####


# Kryptera/dekryptera med förskjutningschiffer
def get_message(key, message):
    print "=" * 40, "\n"
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
    print "=" * 40, "\n"

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

        print encrypted_message, "The key is:", key



# Read info from user
method  = raw_input("Do you want to encrypt, decrypt or break a message? (Type: ENC, DEC or BRK): ")
message = raw_input("Input the message: ")

# Call correct function with parameters
if method == "ENC" or method == "enc":
    key     = input("Input the key (an integer value): ")
    key = key * 1
    print get_message(key, message)

elif method == "DEC" or method == "dec":
    key     = input("Input the key (an integer value): ")
    key = key * -1
    print get_message(key, message)

elif method == "BRK" or method == "brk":
    break_crypt(message)

else:
    print "Wrong type of method."




#### The Vigenere Cipher ####


# Function form making the cipher
def make_cipher():
    cipher = []
    i = 0
    j = 0
    # Choose the letters A-Z
    for char in string.uppercase[:26]:
        cipher.append(string.uppercase[i:26]+string.uppercase[:j])
        i += 1
        j += 1

    return cipher


# Function for repeating the key to the correct length
def repeat_to_length(string_to_expand, length):
   return (string_to_expand * ((length/len(string_to_expand))+1))[:length]


# Function for adding back spaces and special characters to the new string,
# and finally printing the result
def get_message(message_string, old_message):
    new_message = ""
    i = 0

    for index, character in enumerate(old_message):
        if character not in special_characters:
            new_message += message_string[index - i]
        else:
            new_message += character
            i += 1

    print "\nTHE MESSAGE IS\n", "=" * 40, "\n", new_message


# Function for encrypting the message
def encrypt(key, msg):
    encrypted_message = ""

    # For each letter in our key
    for index, character in enumerate(key):
        # Get correct string from cipher array (ROW)
        our_string   = cipher[alpabeth.find(character.upper())]
        # Get string letter position (COLUMN)
        our_position = alpabeth.find(msg[index].upper())
        # Get the correct letter from the string with the column value
        our_letter   = our_string[our_position:our_position + 1]
        # Add letter to message
        encrypted_message += our_letter

    # Return the encrypted message
    return encrypted_message


# Function for decrypting the message
def decrypt(key, msg):
    decrypted_message = ""

    # For each letter in our key
    for index, character in enumerate(key):
        # Get string letter position (COLUMN)
        our_position = alpabeth.find(character.upper())
        # Find the correct row and use the first letter in that row
        for row in cipher:
            if row[our_position] == msg[index].upper():
                decrypted_message += row[0]

    # Return the encrypted message
    return decrypted_message


# Get the message and key
method  = raw_input("Do you want to encrypt or decrypt the message? (Type: ENC, DEC): ")
message = raw_input("Enter the message: ")
key     = raw_input("Enter the key: ")


# Save the old message and setup a cipher
old_message = message
cipher      = make_cipher()


# Setup strings for the aplabeth and a special characters list
special_characters  = [" ", "!", ".", "?", ","]
alpabeth = string.uppercase


# Temporary remove unnessecary characters from our message and key strings
for char in special_characters:
    message = message.replace(char, "")
    key     = key.replace(char, "")


# Get the correct key for encryption
msg_length   = len(message)
key_repeated = repeat_to_length(key, msg_length)


# Call correct function with parameters
if method == "ENC" or method == "enc":
    string_without_specials = encrypt(key_repeated, message)
    # Use the results from the encrypt or decrypt function and put back the special cahracters
    get_message(string_without_specials, old_message)

elif method == "DEC" or method == "dec":
    string_without_specials = decrypt(key_repeated, message)
    # Use the results from the encrypt or decrypt function and put back the special cahracters
    get_message(string_without_specials, old_message)

else:
    print "Wrong type of method."
