import numpy as np
import scipy as sci

a = np.array([0,1,2,3,4,5])

print(a)
print(a.ndim)   # how many dimensions
print(a.shape)  # shape of matrix

b = a.reshape((3,2))

print(b)
print(b.ndim)
print(b.shape)

# numpy is efficent. so any changes you make to 'b' values are applied to 'a' as well. (shape of matricies are still unique)
# if you want to make them two independent matricies you need to use .copy()
print(a)

b[1][0] = 77
print(b)
print(a)

c = a.reshape((3,2)).copy()
print(c)

c[0][0] = -99
print(a)
print(c)
print(a*3)  #multiply whole matrix by 3
print(c**2) #sqrt

#numpy vs regular python list
pyList = [1,2,3,4]
numpyList = np.array([1,2,3,4])

print(pyList*2)     #see how it takes the list and repeats it
print(numpyList*2)  #while numpy actually multiplies by the factor of 2

#lets try pyList again
print(pyList*4)


#Indexing
print (a[np.array([2,3,4])])    # you can use arrays themselves as indicies

print(a>4)          #which elements are greater than 4
print(a[a>4])       #returns a list of the elements greater than 4

a[a>4] = 4          #you can even use numpy to trim outliers: thats to say, in this case... anything greater than 4 in the array will be set to 4
print(a)

#as the former is a highly used scenario, there is a built in function that lets you clip values at both ends of an interval with just 1 function call
a = np.array([0, 1, 77, 3, 4, 5])
print("After remaking the list with outliers, this is the result of .clip(0,4)", a.clip(0,4))
