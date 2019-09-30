# Feed this script a number and it generates a random one
# in the range of 1 and the number you entered.
# Written in Notepad++, tested with Python 2.7.16 running
# through the Windows command line.

# Santtu "MFG38" Pesonen, 2019-09-30

import random

print "Insert a number and press Enter to receive a random"
print "number between 1 and the one you entered."
randomizer = raw_input("Your number: ")
randomizer = random.randint(1,int(randomizer))

print "And your lucky number is... " + str(randomizer)
