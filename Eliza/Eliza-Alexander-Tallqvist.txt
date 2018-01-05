# -*- coding: cp1252 -*-
# Tutorial 2 | Eliza
# Alexander Tallqvist


import string
import random
import logging
import time;


#--- define the log file name ---
logName = "eliza"
logFileName = logName+'.log'
localtime = time.asctime( time.localtime(time.time()) )

#--- create a logging object called logger ---
logger = logging.getLogger(logName)
hdlr = logging.FileHandler(logFileName)

#--- set the format to be just the message ---
#formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
formatter = logging.Formatter('%(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)

#--- log all levels above and including info messages ---
logger.setLevel(logging.INFO)

#--- clear the log file when starting ---
logFile = open( logFileName, "w" )
logFile.write(localtime + "\n")
logFile.close()

#--- the main log function. Appends the string s to the log ---
def log( s ):
     logger.info( s )


# Positive responses
positiva = [
"Beratta mer",
"Jag forstar...",
"Ahaa...",
"Du har sa ratt",
"Jag lyssnar..."
]

# Negative responses
negativa = [
"Varfor ar du pa sa daligt humor?",
"Ar allting okej?",
"Ar du helt saker?",
"Ar det sant?",
"Varfor inte?"
]

# Family related responses
family = [
"Ar din bror likadan?",
"Ar din syster likadan?"
]

# Trigger words for ending the conversation
end_convo = [
"hejs svejs",
"tack och god natt",
"ok, that does it!",
"Sluta!"
]

# First perspective dictionary
dictionary_forsta = {
'jag':  'du',
'min':  'din',
'mig':  'dig',
'mitt': 'ditt',
'mina': 'dina'
}

# Second perspective dictionary
dictionary_andra = {
'du':  'jag',
'din':  'min',
'dig':  'mig',
'ditt': 'mitt',
'dina': 'mina'
}

# Various trigger words
negative_words = ["nej", "aldrig"]
family_words = ["mamma", "pappa", "familj"]
special_characters  = ["!", ".", "?", ","]


def main():

    print "**************************************************"
    print
    print "      Valkommen till Elizas mottagning            "
    print
    print "**************************************************"
    print
    print '(Du kan sluta nar som helst genom att svara "Hejs svejs | tack och god natt | ok, that does it! | sluta")'
    print
    print 'Beratta for mig om dina problem...'

    while True:

        text = raw_input("\n> ")
        log(text)
        saved_message = text

        # End conversation if needed
        if text in end_convo:
            tack = 'Tack for besoket.'
            print tack
            log(tack)
            break

        else:
            text_lower = string.lower(text)
            text_without_specials = remove_specials(text_lower)
            answer = call_elize(string.split(text_without_specials))

            if answer:
                get_message(answer, string.lower(saved_message))


# Function for removing special characters from a string
def remove_specials(user_text):
    message = user_text
    for char in special_characters:
        message = message.replace(char, "")

    return message


# Function for print out a reponse that has had its structure
# altered by removing special characters, or uses either the first
# or second perspective dictionary
def get_message(message_string, old_message):
    new_message = ""
    i = 0

    # Temporary make the sentences equal in length by making
    # "Me" and "You" equal in length
    if "du" in old_message:
        message_string = message_string.replace("jag ", "ja ")

    if "jag" in old_message:
        message_string =  message_string.replace("du ", "duu ")

    # Loop for adding back special characters at the correct position
    for index, character in enumerate(old_message):
        if character not in special_characters:
            new_message += message_string[index - i]
        else:
            new_message += character
            i += 1

    # Replace last item with "?" if needed
    if(new_message[-1:] == "." or new_message[-1:] == "!"):
        new_message = new_message[:-1] + "?"

    # Add back the original words for "Me" and "You"
    if "duu" in new_message:
        new_message = new_message.replace("duu", "du")

    if "ja" in new_message:
        new_message =  new_message.replace("ja ", "jag ")

    print new_message
    log(new_message)


# Function that checks the words in the user message
# against different dictionaries and trigger words
def call_elize(urspr_ord):

    check = False
    negative_check = False
    family_check = False

    nya_ord = urspr_ord[ : ]

    for i in range(len(urspr_ord)):

      # Check for negative words, break if found
      if urspr_ord[i] in negative_words:
          negative_check = True
          break

      # Check for family related words, break if found
      if urspr_ord[i] in family_words:
          family_check = True
          break

      # Check for words in second perspective, set check to True
      if urspr_ord[i] in dictionary_andra:
            nya_ord[i] = dictionary_andra[urspr_ord[i]]
            check = True

      # Check for words in first perspective, set check to True
      elif urspr_ord[i] in dictionary_forsta:
            nya_ord[i] = dictionary_forsta[urspr_ord[i]]
            check = True

    # The default answers if no flags were raised
    if check == False and negative_check == False and family_check == False:
        svar = random.choice(positiva)
        print svar
        log(svar)
        return False

    elif negative_check == True:
        svar = random.choice(negativa)
        print svar
        log(svar)
        return False

    elif family_check == True:
        svar = random.choice(family)
        print svar
        log(svar)
        return False

    else:
        svar = string.join(nya_ord)
        return  svar


main()
