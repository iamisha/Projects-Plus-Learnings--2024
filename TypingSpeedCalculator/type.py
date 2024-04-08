from time import *
import random as r # for multiple strings

print(time())

# fun to find the mistake between the text and textinput
def mistake(paratext, usertext):
    # mistake word count
    error = 0
    for i in range(len(paratext)):# len(paratext): to find the number of words in text
        try:
            if paratext[i]!=usertext[i]:
                error = error + 1
        except:
            error = error + 1
        return error
    


text = ["A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.",
"My name is Priya Singh Thakur",
"He is such a handsome man"
]

text1 = r.choice(text)
print("==========> Typing Speed <==========")
print(text1)

textinput = input("  Enter:  ")