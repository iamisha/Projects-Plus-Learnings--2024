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