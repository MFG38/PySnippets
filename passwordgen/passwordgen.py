# (UNFINISHED) Generates a random password that's 8-32 characters in length.

import random
#import itertools

chars = [
    # Upper-case letters
    "A", "B", "C", "D", "E", "F", "G", "H", "I",
    "J", "K", "L", "M", "N", "O", "P", "Q", "R",
    "S", "T", "U", "V", "W", "X", "Y", "Z",
    # Lower-case letters
    "a", "b", "c", "d", "e", "f", "g", "h", "i",
    "j", "k", "l", "m", "n", "o", "p", "q", "r",
    "s", "t", "u", "v", "w", "x", "y", "z",
    # Numbers
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

generatedList = []
generatedPW = ""

minLength = 8
maxLength = 32

def genPassword(length):
    if length not in range(minLength,maxLength):
        print "Can't generate password: length is out of bounds!"
    else:
        for i in xrange(length):
            generatedList.append(random.choice(chars))
        generatedPW = "".join(generatedList)
        return generatedPW

passLength = int(raw_input("Enter desired length of password (8-32 characters): "))
genPassword(passLength)
print "Your password is: " + generatedPW
