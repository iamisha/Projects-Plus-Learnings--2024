# file = open('django\python_basics\demo.txt', 'w')

# it create new file
file = open('django\python_basics\demo1.txt', 'w')
print(file.writable())

# file.write('This is the new text in file, it removes all existing texts!')
file.write('it has created the new file and this text has been written')
file.close()