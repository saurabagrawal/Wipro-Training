
'''
NumPy Arrays
Creating Arrays from Lists
'''

import numpy as np

# Creating a 1D array from a list
list_1d = [1, 2, 3, 4, 5]

array_1d = np.array(list_1d)
print("1D Array from list:", array_1d)

# # Creating a 2D array from a list of lists
list_2d = [[1, 2, 3], [4, 5, 6]]
array_2d = np.array(list_2d)
print("2D Array from list of lists:\n", array_2d)


'''
Array Attributes
Shape and Size: Get the shape and size of a NumPy array using the shape
 and size attributes.
Data Types: NumPy arrays have a single data type for all elements.
You can check the data type with the dtype attribute.
Specify the data type when creating an array.

'''

array = np.array([[1, 2, 3], [4, 5, 6]])
# # Shape of the array
print("Shape of array:", array.shape)
#
# # Size of the array
print("Size of array:", array.size)
#
# # Data type of the array
print("Data type of array:", array.dtype)

array_float = np.array([1, 2, 3], dtype=np.float16)
print("Array with specified data type:", array_float)
print("Data type of the array:", array_float.dtype)



'''
Built-in Functions
arange: Similar to Python's range() but returns a NumPy array.
linspace: Creates an array of evenly spaced values over a specified range.
ones: Creates an array filled with ones.
zeros: Creates an array filled with zeros.
'''

array_arange = np.arange(0.5, 10.75, 0.75)
print("Array with arange:", array_arange)

array_linspace = np.linspace(21, 51, 5)
print("Array with linspace:", array_linspace)

array_ones = np.ones((2, 3))
print("Array of ones:\n", array_ones)

array_zeros = np.zeros((2, 3))
print("Array of zeros:\n", array_zeros)


# '''
# Random Arrays
# rand: Creates an array of given shape with random values between 0 and 1.
# randn: Creates an array of given shape with random values from a
#                 standard normal distribution.
# randint: Creates an array with random integers within a specified range.
#
# '''

array_rand = np.random.rand(2, 3)
print("Random array with rand:\n", array_rand)

array_randn = np.random.randn(2, 3)
print("Random array with randn:\n", array_randn)

array_randint = np.random.randint(0, 10, (2, 3))
print("Random array with randint:\n", array_randint)



'''
Indexing and Slicing
Reshaping Arrays
Change the shape of an array without changing its data using the
 reshape() method.

'''

array = np.array([[1, 2, 3], [4, 5, 6]])

# Indexing
print("Element at [0, 1]:", array[0, 1])

# Slicing
print("First row:", array[0, :])
print("First column:", array[:, 0])
print("Sub-array:", array[0:2, 1:3])

array = np.arange(6)
print("Original array:", array)
print("Shape of array:", array.shape)

reshaped_array = array.reshape((2, 3))
print("Reshaped array:\n", reshaped_array)
# Array Operations
# Element-wise Operations :  NumPy supports element-wise operations,
# which apply operations to each element in the array individually.



import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Element-wise addition
print("Element-wise addition:", array1 + array2)

# Element-wise subtraction
print("Element-wise subtraction:", array1 - array2)

# Element-wise multiplication
print("Element-wise multiplication:", array1 * array2)

# Element-wise division
print("Element-wise division:", array1 / array2)

'''
Basic Arithmetic Operations
NumPy provides functions for basic arithmetic operations which also operate element-wise.

Aggregate Functions
NumPy provides aggregate functions that operate over the entire array 
or along a specific axis.

'''

# Adding a scalar to an array
print("Adding 10 to each element:", array1 + 10)

# Multiplying each element by a scalar
print("Multiplying each element by 2:", array1 * 2)

# Using numpy functions
print("Square of each element:", np.square(array1))
print("Square root of each element:", np.sqrt(array1))


array = np.array([[1, 2, 3], [4, 5, 6]])

# Sum of all elements
print("Sum of all elements:", np.sum(array))

# Mean of all elements
print("Mean of all elements:", np.mean(array))

# Minimum element
print("Minimum element:", np.min(array))

# Maximum element
print("Maximum element:", np.max(array))

# Sum along each column
print("Sum along each column:", np.sum(array, axis=0))

# Sum along each row
print("Sum along each row:", np.sum(array, axis=1))

# Basic Mathematical Functions
# Trigonometric Functions
# NumPy provides various trigonometric functions such as sine, cosine,
# tangent, etc.


import numpy as np

angles = np.array([0, np.pi/2, np.pi])
print(angles)
print("Sine of angles:", np.sin(angles))
print("Cosine of angles:", np.cos(angles))
print("Tangent of angles:", np.tan(angles))

# Inverse trigonometric functions
print("Arcsine of 1:", np.arcsin(1))
print("Arccosine of 0:", np.arccos(0))
print("Arctangent of 1:", np.arctan(1))

'''
Exponential and Logarithmic Functions
Rounding and Modulus Functions
'''

values = np.array([1, 2, 3])

print("Exponential of values:", np.exp(values))
print("Natural log of values:", np.log(values))
print("Base-10 log of values:", np.log10(values))

values = np.array([1.7, 2.3, 3.9])

print("Floor of values:", np.floor(values))
print("Ceil of values:", np.ceil(values))
print("Rounded values:", np.round(values))

print("Modulus of 5 and 2:", np.mod(5.5, -2.0))
print("Remainder of 5 divided by 2:", np.remainder(5.5, -2.0))

'''
Linear Algebra Functions
Dot Product and Matrix Multiplication
Determinants and Inverses
Eigenvalues and Eigenvectors

'''

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Dot product of A and B:", np.dot(A, B))
print("Matrix multiplication of A and B:", np.matmul(A, B))

print("Determinant of A:", np.linalg.det(A))
print("Inverse of A:\n", np.linalg.inv(A))

eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues of A:", eigenvalues)
print("Eigenvectors of A:\n", eigenvectors)