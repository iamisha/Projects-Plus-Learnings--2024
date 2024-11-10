# python is an object oriented programming language, anything
# that deals with classes, objects

# class MyClass:
#     x = 5

# o1 = MyClass()
# print(o1.x)



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # o2 = Person('Kichu', 24)

# name = input('Enter your name: ')
# age = int(input('Enter your age: '))
# o2 = Person(name, age)
# print('Your name is '+o2.name + ' and your age is ',o2.age)



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

o2 = Person('Kichu', 24)

del o2.age

# gives an error 'object has no attribute age' as it has been deleted earlier

print(o2.age)
del o2.name


# let's understand the function of pass in python class

# without using pass it gives an error
# class Person:
#     pass # often used as a placeholder

