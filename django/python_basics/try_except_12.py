try:
    x1 = int(input('Input first integer: '))
    x2 = int(input('Input second integer: '))
    print(x1/x2)
except ValueError: 
    print('Value not an integer!!!')
except ZeroDivisionError:
    print('hey!, you can\'t devide a number by 0')
else: 
    print('Nothing went wrong...')
# In Python, the finally block in a try-except structure is used to define code that will always execute, regardless of whether an exception occurred or not
finally:
    print('Try Except finished!')