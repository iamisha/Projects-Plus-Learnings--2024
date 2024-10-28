# function is a bunch of code that performs a particular task

# creating our first function with argument name and age
def greetings_fun(name,age):
    print('Welcome,'+name+'!'+'Your age is ',age)


# passing the paremeters in runtime
name = input('Enter user name: ')
age = input('Enter user age: ')
# calling the function
greetings_fun(name, age)


# The *names syntax allows greet_fun to accept any number of positional arguments and store them as a tuple named names
# def greet_fun(*names):
#     print('Welcome '+names[0])

# greet_fun('Kichu', 'John','Tim')