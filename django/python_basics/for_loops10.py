# for letter in 'Hello':
#     print(letter)

# we can loop through list
# mylist = ['tata', 'lamborghini', 'c-cyan']

# for items in mylist:
#     print(items)

# we can also loop through dictionary
my_dict = {
    'name': 'Kichu',
    'nick-name': 'sonu',
    'age': 24,
    'salary': 'it\'s secret'
}
for key, val in my_dict.items():
    if key == 'age':
        break
    print(key,val)

# we can also loop through range
# for x in range(2,10):
#     if x == 7:
#         break
#     print(x)