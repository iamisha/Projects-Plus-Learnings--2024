
three_numbers = (1,2,3, 'Home', True)

# gives error as tuples are immutatble(can't change the value)
# three_numbers[1] = 23
print(three_numbers)
print(len(three_numbers))
print(type(three_numbers[3]))

# Allows various data types
strings = ('home', 'land', 'earth')

# tuple constructor
boo = tuple((True, False, True))
print(strings)
print(boo)
