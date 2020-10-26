# Generates a random insult from a pre-determined
# selection of words and phrases.
# Current number of possible combinations: 1,320.
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
    "hollow-skulled ",
    "braindead ",
    "bone-headed ",
    "gelatinous ",
    "mindless ",
    "thoughtless ",
    "idiotic "]

noun = [
    "pile ",
    "lump ",
    "piece ",
    "tub ",
    "truckload ",
    "bottle ",
    "sphere ",
    "heap "]

thing = [
    "excrement",
    "liquid rotten eggs",
    "foul ooze",
    "dead brain cells",
    "rotten flesh",
    "lard",
    "Satan's semen",
    "pubic hair",
    "yesterday's lunch",
    "trash",
    "fossilized dung"]
    
insult = random.choice(adj) + random.choice(noun) + "of " + random.choice(thing)
print "Here's your insult, you " + insult + "."
