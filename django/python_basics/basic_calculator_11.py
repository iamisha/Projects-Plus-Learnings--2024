# Building a basic calculator

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
op = input('Enter Operator: ')

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '/':
    print(num1/num2)
elif op == '*':
    print(num1*num2)
elif op == '%':
    print(num1%num2)
else:
    print('Please choose one operator')