# To check the Python version
import sys
import itertools

print("Python Rules")
print("")
import this

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Python version number: {}".format(sys.version))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# To return multiple values at once
def Coding():
    a = 1
    b = 2
    return a, b

x, y = Coding()
print(x, y)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# To concatenate multiple strings
myProfile = ['Follow - ', 'coding.', 'aryan']
print('Hola '.join(myProfile))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# To allow negative indices
myProfile = ['Follow - ', 'coding.', 'aryan']
print(''.join(myProfile[-1]))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# To swap the values of two objects
x = 1
y = 2
print('before')
print(x, y)

x, y = y, x
print('after')
print(x, y)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Transpose a matrix
m = [[1, 2, 3], [4, 5, 6]]
transposed_matrix = list(zip(*m))
print(transposed_matrix)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Unpack a list into separate variables
l = [1, 2, 3]
print('original list')
print(l)
x, y, z = l
print('unpacked list')
print(x)
print(y)
print(z)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Flatten multiple lists into one
l = [[1, 2], [3, 4], [5, 6]]
print(list(itertools.chain.from_iterable(l)))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# No idea what this does
subtract = lambda x, y: x - y
print(subtract(3, 9))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Method for summing many numbers
def get_sum(*args):  # The asterisk indicates that there can be as many args as you want to pass
    result = 0
    for i in args:
        result += i
    return result
print(get_sum(1, 2, 3))
print(get_sum(1, 2, 3, 4, 5, 5, 6, 7, 9, 10))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Class example
class Engineer:
    def __init__(self, name):
        self.name = name
        self.__starting_salary__ = 62000

dain = Engineer('Dain')
print(dain.name, dain.__starting_salary__)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Functions with comparisons
def get_element_with_comparison(lst):
    if len(lst) > 0:
        return lst[0]

def get_first_element(lst):
    if len(lst):
        return lst[0]

elements = [1, 2, 3, 4]
first = get_element_with_comparison(elements)
second = get_first_element(elements)

print(first == second)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Bitwise operation example
def f(x, k):
    return x ^ k ^ k
print(f(100, 16))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Bitwise right shift example
def f(x, k):
    return x >> k
print(f(100, 4))
