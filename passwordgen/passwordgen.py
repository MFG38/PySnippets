# (UNFINISHED) Generates a random password that's 8-32 characters in length.

chars =
    # Upper-case letters
    ["A", "B", "C", "D", "E", "F", "G", "H", "I",
    "J", "K", "L", "M", "N", "O", "P", "Q", "R",
    "S", "T", "U", "V", "W", "X", "Y", "Z",
    # Lower-case letters
    "a", "b", "c", "d", "e", "f", "g", "h", "i",
    "j", "k", "l", "m", "n", "o", "p", "q", "r",
    "s", "t", "u", "v", "w", "x", "y", "z",
    # Numbers
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

minLength = 8
maxLength = 32
passLength = int(raw_input("Enter desired length of password (8-32 characters): "))

def genPassword(length):
    if length < minLength or length > maxLength:
        print "Can't generate password: length is out of bounds!"
    else:
        for n in length:
            c[n] = random.choice(chars)
        print "Your password is: "