my_dict = {
    'name': 'Kichu',
    # duplication is not allowed
    # we can't have the values with same keys, for eg.
    # 'name': 'John', only gets the latest one that is John not Kichu
    'natinality': 'Europian',

    # we can have the same values, but not the same keys
    # 'natinality2': 'Europian',
    'qualification': 'Bachelor',

    # can add multiple datatype values
    'age': 22,
    'is_male': True,

    # can add lists in dictionary
    'friends': ['Tim','Tom', 'Jon']
}
print(len(my_dict))
print(my_dict)
print(my_dict['is_male'])
print(my_dict['friends'][1])

x = my_dict['name']
print(x)