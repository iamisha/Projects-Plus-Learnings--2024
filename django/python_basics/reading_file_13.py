file = open('django\python_basics\demo.txt', 'r')
print(file.readable())

# reads the first line
print(file.readline())

# reads the second line
print(file.readline())

# recommended  one 
print(file.readlines()[1])

# let's do it using for loop
# for lines in file.readlines():
#     print()
    
file.close()

