import numpy as np

"""Creating 1D arrays from lists"""

python_list = [3,2,5,8,4,9,7,6,1]
array = np.array(python_list)
array

type(array)

"""Creating 2D arrays from lists"""

python_list_of_lists = [[3,2,5],
                        [9,7,1],
                        [4,3,6]]
np.array(python_list_of_lists)

"""**Why use arrays rather than lists**

*   Python lists can include many different datatypes
*   all of the elements in a NumPy array must be the same datatype
"""

python_list = ["beep", False, 56, .945, [3,2,5]]
python_list

"""**NumPy Arrays**



*   Can contain only a single data type
*   Use less space in memory


"""

numpy_boolean_array = [[True, False], [True, True], [False, False]]
numpy_float_array = [1.9, 5.4, 8.8, 3.6, 3.2]

"""**Creating arrays from scratch**

There are many NumPy functions used to create arrays from scratch, including


*   np.zeros():  Creates an arrays full of zeros

*   np.random.random(): The array will be made up of random floats between zero and one
*   np.arange(): Creates an array between the start number and stop number, includes start number but not stop number.



"""

np.zeros((5,3))

np.random.random((2,4))

np.arange(-3,4)

np.arange(4)

np.arange(-3,4,3) # if a third arguement is passed, it is interpreted as the step value

"""**np.arange** is particularly use in ploting"""

from matplotlib import pyplot as plt
plt.scatter(np.arange(0,7),
            np.arange(-3,4))

plt.show()

"""Exercise code 1. converting sudoku_list to an array"""

# Import NumPy
import numpy as np

# Convert sudoku_list into an array
sudoku_list = [
 [0, 0, 4, 3, 0, 0, 2, 0, 9],
 [0, 0, 5, 0, 0, 9, 0, 0, 1],
 [0, 7, 0, 0, 6, 0, 0, 4, 3],
 [0, 0, 6, 0, 0, 2, 0, 8, 7],
 [1, 9, 0, 0, 0, 7, 4, 0, 0],
 [0, 5, 0, 0, 8, 3, 0, 0, 0],
 [6, 0, 0, 0, 0, 0, 1, 0, 5],
 [0, 0, 3, 5, 0, 8, 6, 9, 0],
 [0, 4, 2, 9, 1, 0, 3, 0, 0]]
sudoku_array = np.array(sudoku_list)

# Print the type of sudoku_array
print(type(sudoku_array))

"""Exercise code 2. Creating arrays from scratch"""

doubling_array = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

# Create an array of integers from one to ten
one_to_ten = np.arange(1,11
                       )

# Create your scatterplot
plt.scatter(one_to_ten, doubling_array)
plt.show()

"""**3D arrays**"""

array_1_2D = np.array([[1,2],[5,7]])
array_2_2D = np.array([[8,9], [5,7]])
array_3_3D = np.array([[1,2], [5,7]])

array_3D = np.array([array_1_2D, array_2_2D, array_3_3D])

print(array_3D)

