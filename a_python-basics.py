# import libraries
import scipy
import numpy
import matplotlib

####################################
#functions - ex: polynomial function
def poly (x):
    print(3*x**2 - x + 2)

# test function
poly(0)


####################################
#Another example Prime numbers function
def primes_upto (n):
    i = 2
    while i < n:
        if is_prime(i):
            print(i, end = " ")
        i += 1

# 'is_prime' needed for 'primes_upto':
# (comment out to see error produced)
def is_prime (n):
    for d in range(2,n):
        if n % d == 0:
                return False
        d += 1
    return True

# test function
primes_upto(20)


# ###################################
# File I/O

# JSON - The JSON format is commonly used by modern applications
import json
json.dumps([1, 'simple', 'list'])
json.dumps({})

with open('mydata.csv', 'r') as f:
    print(f.read())


# Python Object Model
x = 1         # x is a reference to python object for 1
x = x + 1     # x is now a reference to python object for 2
print(id(x))  # we can look at the object id for 2 to check
print(id(2))

# Python Object Model
x = 42
y = 42
print(id(x))
print(id(y))

x = 1
y = 1
print("x == y: ", x == y)
print("x is y: ", x is y)

x = 2048
y = 2048
print("x == y: ", x == y)
print("x is y: ", x is y)

# ###################################
# Passing data to functions
def print_id(input_var):
    """prints the id of the object referred to by input_var"""
    print(id(input_var))

x = 67.3
print("outside of function:",id(x))
print_id(x)

my_list = [1, 2, "a short str"]
print("outside of function:",id(my_list))
print_id(my_list)

# Functions can modify their inputs 
def add_some_items(input_list):
    input_list.append("a")
    input_list.append("few")
    input_list.append("items")

a_list = [1,2,3]
add_some_items(a_list)
print(a_list)

# if we reassign a variable reference inside of a function, the original variable is not modified
def reassign(input_var):
    input_var = 2

a = 1
reassign(a)
print("a =", a)

# ###################################
# Copying a data structure
# Create a new copy of an existing object. 
# Assignment between variables copies the reference, not the data.
a = ["a", "simple", "list"]
b = a
b[1] = "basic"
print(a)


# Copying a data structure
# Copy a list using the list constructor (list()) or a complete slice (my_list[:])
a = ["a", "simple", "list"]
b = list(a)
c = a[:]
b[1] = "basic"
print(a)
print(c)


# A more generic method to copy data structures is to use the copy module. 
# This allows us to copy any data structure (dictionaries, sets, tuples, etc).
import copy
a = ["a", "simple", "list"]
b = copy.copy(a)
b[1] = "basic"
print(a)

# Copy example with dictionary
import copy
my_dict = {"apple":"fruit", "kale":"vegetable"}
other_dict = copy.copy(my_dict)
other_dict["orange"] = "fruit"
print(my_dict)

# Copying nested data structures
data = {
  "info": "distance",
  "units": "meter",
  "measurements": [3.5, 3.7, 3.9, 4.0]
}

# copy.copy() created a new top-level dictionary
# However, only references for nested objects were coped
# Use copy.deepcopy() to create a completely separate copy of a nested data structure
data = {
  "info": "distance",
  "units": "meter",
  "measurements": [3.5, 3.7, 3.9, 4.0]
}
import copy
data_dup = copy.deepcopy(data)
data_dup["collection_site"] = "big lake"
data_dup["measurements"].append(3.8)
print(data)

# (im)mutability
# Python tuples are immutable.
# my_tup = (1,4,6.6,"simple str")
# my_tup[1] = "new str"

# like Python variables, tuples are references to other Python objects. 
# Once a tuple is created, its elements may not be rebound to other objects. 
# But what happens when a mutable data structure (such as a list) is referenced by a tuple
# my_tup = (1, ["list", "in", "a", "tuple"], 55.5)
# my_tup[1][3] = "what???"
# print(my_tup)

# Data exploration with pandas and matplotlib
% matplotlib inline
from sklearn import datasets

# iris is loaded as a dict object; you can check the keys with iris.keys()
iris = datasets.load_iris() 

# initializes DataFrame with sepal/petal length/width variables
iris_df = pd.DataFrame(iris.data, columns=iris['feature_names']) 

# adds a 'type' column with the iris species
iris_df['type'] = iris['target_names'][iris.target]

# Examine the first few rows of the iris_df DataFrame we just constructed
iris_df.head()

# Call the DataFrame plot() method, which plots line graphs of each numeric variable
iris_df.plot()

# Explore the data

