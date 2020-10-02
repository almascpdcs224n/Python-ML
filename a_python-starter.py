# initial configurations locally
# !wget -c https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh
# !chmod +x Anaconda3-5.1.0-Linux-x86_64.sh
# !bash ./Anaconda3-5.1.0-Linux-x86_64.sh -b -f -p /usr/local
# !conda install -q -y --prefix /usr/local -c pytorch -c tensorcomp tensor_comprehensions

# import sys
# sys.path.append('/usr/local/lib/python3.6/site-packages/')

# scipy
print ('Working with numpy/panda/matplot libraries') 
import scipy
import numpy
import matplotlib
print('scipy: %s' % scipy.__version__); print('numpy: %s' % numpy.__version__); print('matplotlib: %s' % matplotlib.__version__)
import pandas
print('pandas: %s' % pandas.__version__)


# scikit-learn
import sklearn
print('sklearn: %s' % sklearn.__version__)

print('_________________________________________________')

# matplot lib basic  
import matplotlib.pyplot as plt
import numpy
myarray = numpy.array([1, 2, 3])
#plt.plot(myarray); plt.xlabel('some x axis'); plt.ylabel('some y axis'); plt.show()

print(' matplot basic')
# basic scatter plot
import matplotlib.pyplot as plt
import numpy
x = numpy.array([1, 2, 3]); y = numpy.array([2, 4, 6])
print ("x", x); print ("y", y)
#plt.scatter(x,y); plt.xlabel('some x axis'); plt.ylabel('some y axis'); plt.show()
print('_________________________________________________')


# series
print ('series, dataframes')
import numpy
import pandas
myarray = numpy.array([1, 2, 3])
rownames = ['a', 'b', 'c']
myseries = pandas.Series(myarray, index=rownames)
print(myseries)
print(myseries[0]); print(myseries['a'])

# dataframe
import numpy
import pandas
myarray = numpy.array([[1, 2, 3], [4, 5, 6]])
rownames = ['a', 'b']; colnames = ['one', 'two', 'three']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)
print("one column: %s" % mydataframe['one'])
print("one column: %s" % mydataframe.one)
print('_________________________________________________')


# Python Crash Course
print('Python Crash Course') 
# Strings - Numbers - Boolean - Multiple Assignment - No value
data = 'hello world'; print(data[0]); print(len(data)); print(data)
value = 123.1; print(value); value = 10; print(value)
a = True; b = False; print(a, b)
a, b, c = 1, 2, 3; print(a, b, c)
a = None; print(a)

print('Python Data Structure')  
# Data Structures
# ===============

# Tuple (cannot change)
a = (1, 2, 3); print(a)

# Lists
mylist = [1, 2, 3]; print("Zeroth Value: %d" % mylist[0])
mylist.append(4);   print("List Length: %d" % len(mylist))
for value in mylist:
	print(value)

# Dictionaries

mydict = {'a': 1, 'b': 2, 'c': 3};  print("A value: %d" % mydict['a'])
mydict['a'] = 11;                   print("A value: %d" % mydict['a'])
print("Keys: %s" % mydict.keys());  print("Values: %s" % mydict.values())
for key in mydict.keys():
	print(mydict[key])

#Read Files
from pandas import read_csv
filename = "mydata.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
types = data.dtypes
print(types)
print('_________________________________________________')

#Project Template
