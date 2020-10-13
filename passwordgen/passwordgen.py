# Generates a random password that's 8-32 characters in length.
# Written in Notepad++, tested with Python 2.7.16 running
# through the Windows command line.

# Santtu "MFG38" Pesonen, 2020-07-24

import random
import string

chars = string.ascii_letters + string.digits

minLength = 8
maxLength = 33      # 32 + 1, just so that max length doesn't cap at 31.

def genPassword(length):
    if length not in range(minLength,maxLength):
        print "Can't generate password: length is out of bounds!"
    else:
        generatedPW = ''.join((random.choice(chars) for i in range(length)))
        print "Your password is: " + generatedPW

passLength = int(raw_input("Enter desired length of password (8-32 characters): "))
genPassword(passLength)
