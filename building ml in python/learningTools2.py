import numpy as np
import scipy as sci
from scipy import stats

c = np.array([1, 2, np.NAN, 3, 4])      # example scenario where a data value read in from a text file is invalid.
print(c)

print(np.isnan(c))                      # checks for nan values.
print( c[~np.isnan(c)] )                # excludes nan values
print( np.mean(c[~np.isnan(c)]) )       # takes the mean aka average of the values in the array.

q = np.array([0, 0, 15, 3, 4, 8, 9, 3, 1, 4, 12, 5, 4, 14, 7])
print( np.median(q) )                   # should return 4, because median is when you sort a list and look at the middle most number
# [0, 0, 15, 3, 4, 8, 9, 3, 1, 4, 12, 5, 4, 14, 7]
# [0, 0, 1, 3, 3, 4, 4, 4, 5, 7, 8, 9, 12, 14, 15]


# number that occurs most often, if there are no duplicates, then the mode does not exist
print( stats.mode(q) )                     # to utilize this you must first use this line: "from scipy import stats"
