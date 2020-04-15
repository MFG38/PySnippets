# Generates a random insult from a pre-determined
# selection of words and phrases.
# Current number of possible combinations: 432.
# Written in Notepad++, tested with Python 2.7.16
# running through the Windows command line.

# Santtu "MFG38" Pesonen, 2020-04-15

import random

adj = [
    "putrid ",
    "small-brained ",
    "bubbling ",
    "pulsating ",
    "hairy ",
    "juvenile ",
    "ball-shaped ",
    "incandescent ",
    "hollow-skulled "]

noun = [
    "pile ",
    "lump ",
    "piece ",
    "tub ",
    "truckload ",
    "bottle "]

thing = [
    "excrement",
    "liquid rotten eggs",
    "foul ooze",
    "dead brain cells",
    "rotten flesh",
    "lard",
    "Satan's semen",
    "pubic hair"]

#def geninsult():
adjindex = random.randint(0,len(adj)-1)
nounindex = random.randint(0,len(noun)-1)
thingindex = random.randint(0,len(thing)-1)
    
insult = str(adj[adjindex]) + str(noun[nounindex]) + "of " + str(thing[thingindex])
print "Here's your insult, you " + insult + "."
