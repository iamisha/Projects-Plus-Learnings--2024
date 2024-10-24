# Print Function
print("My name is Tommy and my age is", 22)

# PYTHON VARIABLES

## Without using Variable
# print('Dolly is a girl')
# print('Dolly is 18')
# print('Dolly is humble')

## Using Python Variable
name = 'Dolly'
age = 18
print(name + ' is a girl')
# print(name + ' is '+ age), this gives error because string can not be concatenated with integer
# to handle error, we can convert integer to string as: 
# print(name + ' is '+ str(age))
print(name + ' is ', age)
print(name,' is ', age)
print(name + ' is humble')

# STRINGS IN PYTHON
print("Hi.\nHow are you?")
#  The backslash (\) is used as an escape character in Python. It allows you to include special characters in a string
print("Hi.\'A QUESTION\' How are you?")
print(name[0])
print(name.upper())
print(name.lower())
print(name.lower().islower())
print(len(name))
print(name.index('D'))
print(name.replace('D', 'K'))

# NUMBERS IN PYTHON
print(22)
number = 23
print(number)
number2 = str(23)
print(22 + 23)
print(22 - 23)
print(22 * 23)
print(22/23)
print(22 % 23)
print(type(number))
print(type(number2))

# print('Number is ' + number) gives error cause string can't be concatenated with number
print('Number is ' + number2)

print(-5)
print(abs(-5))
print(max(2, 4))
print(min(2, 4, 0))

print(min(2.2, 3.2))

print(round(3.2))
print(round(3.5))

print(bin(3))
print(bin(4))

from math import *
print(sqrt(25))

# GETTING USER'S INPUT
# name1 = input('Please, Enter Your Name: ')
# age1 = int(input('Please, Enter Your Age: '))

# print('Your name is ' + name1 + ' and your age is ', age1, ' year old.')


# BUILDING A SIMPLE WORD REPLACE PROGRAM
sentence = input('Enter your sentence: ')
print(sentence)
word1 = input('Enter the word to replace: ')
word2 = input('Enter the word to replace it with: ')
print(sentence.replace(word1, word2))
