# LIST IN PYTHON

countries = ['United Kingdom', 'Ghana', 'Nigeria', 'Australia', 'New Zealand']
# print(countries)
# print(countries[0])
# print(countries[2])
# print(countries[2][0])
# # Get everything from index number 1
# print(countries[1: ])
# print(countries[1:4])

print(type(countries))

countries[0] = 'United States'
countries[3] = 'Canada'
print(countries)

# get the last element of the list
print(countries[4])

# also
print(countries[-1])
print(countries[-2])

# We can mix different datatypes in a list
countries = ['United Kingdom', 2, 'Nigeria', True, 'New Zealand']
print(type(countries[3]))

# Instead of just using [], we can use list to create list in python
languages = list(('c','c++','java'))
print(languages)

# LIST METHODS
list1 = [5,2,3,4,1]
list2 = ['banana', 'apples', 'mangoe', 'oranges']

# # print the two lists together
# list1.extend(list2)
# print(list1)

# add new atom in list
# list2.append('grapes')

# list2.insert(5, 'cherry')

# # remove an element from the list
# list2.remove('mangoe')
# # remove all the element from the list
# list2.clear()

print((list2.index('mangoe')))

# how many times an element appear in the list
print((list2.count('mangoe')))

# print the elements in ascending order
list1.sort()
print(list1)


# list2.reverse()
print(list2)

# copy the value of one list to a new variable
list3 = list2.copy()
# remove the last value in the entire list
list3.pop()
list3.pop(1)
del list3[0]

# delete the complete list3 varaible 
del list3
print(list3) # it gives error list3 not found, cause it has beend deleted.