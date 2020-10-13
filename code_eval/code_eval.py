# A simple prompt that asks how many lines of code you have and
# prints a comment based on your input. Mainly done for practice.
# Programmed in Notepad++, tested with Python 2.7.16 running
# through the Windows command line.

# Santtu "MFG38" Pesonen, 2019-09-29

print "How many lines does your code have?"
answer = int(raw_input("Insert number here: "))

if answer <= 200:
    code_evaluator = "? Eh, I've seen more complex code."
elif answer > 200 and answer <= 500:
    code_evaluator = "? Could be worse. A lot worse."
elif answer > 500 and answer <= 1000:
    code_evaluator = "? That's a lotta code, alright."
elif answer > 1000 and answer <= 2000:
    code_evaluator = "? You sure you can't do with any less?"
else:
    code_evaluator = "? Sweet Jesus, what have you done?!"
        
print str(answer) + code_evaluator
