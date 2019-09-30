# Unfinished.

import random.py

print "What do you wish to roll?"
print "Format: xdy+z (x = num. of dice, y = die type, z = modifier)"
print "x and +z may be omitted, in which case they'll default to"
print "1 and +0 respectively."
print ""
roll = raw_input("Enter expression: ")
roll = str(roll)

if roll[0] != "d":
    dicenum = int(roll[0])
elif roll[0] == "d":
    dicenum = 1
return int(dicenum)
