# a = 2
# b = 3

# if a>b:
#     print(str(a)+ ' is greater than ' + str(b))
# elif a<b:
#     print(str(a)+ ' is less than ' + str(b))
# elif a=='hello':
#     print('ahbaiaga')
# else:
#     print('Nothing...')

# girl = True
# long_hair = False

# if girl == True and long_hair == True:
#     print('The person is a girl and she has the long hair')
# else:
#     print('Person might be girl or boy')

value = int(input('Enter a value'))

if type(value) == str:
    print('The data is a string datatype')
elif type(value) == int:
    print('The data is an integer datatype')
elif type(value) == bool:
    print('The data is a boolean datatype')
else:
    print('No datatype...')

sentence = input('Write a sentence')

if len(sentence)<10:
    print('Sentence\'s less than 10 in lenght')
else:
    print('Sentence\'s greater than 10 in lenght')




