#this follows pg 21 of the text (building ml with python 2nd ed) then i swapped over to 3rd edition due to a few bugs in the provided code
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

#apparently sp is getting several functions deprecated in newer versions, so you are supposed to use np for this section instead...

#added in the straight line section
# CURIOUS is error an abstract function required for np.plotfit(x value, y value, # of orders the ploted line will have)?
# or is this just utilized outside of plotfit() to help determine other important values?
# ANSWER NOPE its independent, i think this was just here to show what might be going on within scipy's functions to produce a basic error value
# yes i think this is very similar to polyfit's functional structure as seen below:
# error -> np.sum((f(x)-y)**2) VS POLYFIT as detailed further below.
def error(f, x, y):
    return np.sum((f(x)-y)**2)

data = np.genfromtxt("ch1_data/web_traffic.tsv", delimiter="\t")

print(data[:10])
print(data.shape)



x = data[:,0]           #hours
y = data[:,1]           #website hits in an hour

np.sum(np.isnan(y))     #checking how many invalid data entries are present in the "website hits"

#removing invalid data from both the x and y data columns
x = x[~np.isnan(y)]
y = y[~np.isnan(y)]


# NOTE NEW PART  coming from after pg 22, TODO
# can't use d= 1, its too simple
# can't use d=10 to d=53 (forcefully reduced by the alg from d=100) because its OVERFITTED 
# can't use d=2 or d=3 because they somewhat match the data, but extrapolation at both borders reveals they go berserk
# can't use a more complex class because you dont have enough arguments that could fit to make it work.
# WHAT DO WE DO? Take a step back, to go forward. We didn't fully understand our data the first time!
inflection = int(3.5*7*24)              # calculate the inflection point in hours, (3.5 because thats approx how many weeks 
                                        # in where the graph starts showing major changes, if there was a significant change
                                        # around 2.3 weeks in then you would use that value instead)
                                        # 7 is the number of days in the week, and 24 is how many hrs per day.

xa = x[:inflection]                     # data before the inflection point (which is in hours btw)
ya = y[:inflection]
xb = x[inflection:]                     # data after inflection point (again, inflection point is in hrs)
yb = y[inflection:]
# int()'s encapsulation of 3.5*7*24 was added only in 3rd edition, not 2nd edition

fa = np.poly1d(np.polyfit(xa, ya,1))
# LEARN
# np.POLYFIT(xa, ya, 1) -- finds the model function that minimizes the error function (which was defined earlier) -- https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html
# from numpy site: "Fit a polynomial p(x) = p[0] * x**deg + ... + p[deg] of degree deg to points (x, y).
# Returns a vector of coefficients p that minimises the squared error in the order deg, deg-1, … 0."
# fa = np.POLY1D(np.polyfit(xa, ya,1)) -- creates a model function from the model parameters
# https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html
# poly1d is a one dimensional polynomial class
# "A convenience class, used to encapsulate “natural” operations on polynomials so that said
# operations may take on their customary form in code (see Examples).""

fb = np.poly1d(np.polyfit(xb, yb, 1))

fa_error = error(fa, xa, ya)
fb_error = error(fb, xb, yb)

print("Error inflection= %f" %(fa_error + fb_error))   # adding the two errors because we want the total error for the graph, and we split it into two smaller subunits just a few lines above

# ------------------------------------------------------------------------------

'''
fp1, residuals, rank, sv, rcond = np.polyfit(x, y, 1, full = True)

print("Model parameters: %s" % fp1)
print("residuals: %s " % residuals)

print(fp1)

f1 = np.poly1d(fp1)
'''
fx = np.linspace(0, x[-1], 1000)        # generate xvalues for plotting


plt.scatter(x,y, s=10)
plt.title("Web Traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/Hour")
plt.xticks([w*7*24 for w in range(10)], ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)
#draw a slightly opaque, dashed grid
plt.grid(True, linestyle='-', color = '0.75')

#use the fa and fb made above
plt.plot(fx, fa(fx), linewidth = 2, color = 'green', label = "d=%i" %fa.order)          # dont forget to put the colors in damn quotation marks NOTE: I added the "label" portion here

'''
#added this part when we hit pg 19/20 of the text
f2p = np.polyfit(x,y,2)
f2 = np.poly1d(f2p)
plt.plot(fx, f2(fx), linewidth = 2, color= 'orange', label = "d=%i" %f2.order)          # NOTE: I added the "label" portion here
plt.legend(loc = "upper left")
#plt.legend(["d=%i\nd=%i" %(f1.order, f2.order)], loc="upper left")    #LEARN: USEFUL TO KNOW -- to pass in multiple formatting elements via % ...you need to utilize a tuple ie (,) using comma delineation per item
'''

plt.plot(fx, fb(fx), linewidth = 2, color = 'red', label = "d=%i" %fb.order)
plt.legend(loc = "upper left")


plt.show()
