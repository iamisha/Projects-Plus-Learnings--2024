from time import *
import random as r # for multiple strings

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
    
def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)

if __name__ == '__main__':
    while True:
        choice = input("          Enter y/yes for continue or n/no for stop: ")    
        print()
        if choice in ["y","yes"]:
            text = ["A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.",
            "My name is Priya Singh Thakur",
            "He is such a handsome man"
            ]

            text1 = r.choice(text)
            print("          ==========> Typing Speed <==========")
            print(text1)
            print()
            print()
            time_1 = time()
            textinput = input("          Enter :  ")
            time_2 = time()

            print('          Speed : ',speed_time(time_1, time_2, textinput), "w/sec")
            print("          Error : ", mistake(text1, textinput))
            
        elif choice in ["n", "no"]:
            print("          Thank you so much for having us, Have a good day!")
            break
        else:
            print("          Wrong input!")
        