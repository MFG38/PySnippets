# To become a DnD die roller (take 2).

from random import randint

# while True:
roll = 0
getValues = raw_input("Enter roll: ")

def doRoll(expression):
    numdice = getValues.split("d")[0]
    sides = int(getValues.split("d")[1])
    modifier = 0
        
    roll = ((numdice * int(randint(1,sides+1))) + modifier)
    return roll
    print roll

