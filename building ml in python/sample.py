# on page 14 of building machine learning in python 2nd edition
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

#apparently sp is getting several functions deprecated in newer versions, so you are supposed to use np for this section instead...

#added in the straight line section
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

'''
#plot the (x,y) points with dots of size 10
#temporarily here for the lower section until you get to the fx variable
plt.scatter(x,y, s=10)
plt.title("Web Traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/Hour")
plt.xticks([w*7*24 for w in range(10)], ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)
#draw a slightly opaque, dashed grid
plt.grid(True, linestyle='-', color = '0.75')
plt.show()
'''

#calculating and returning multiple values to determine the best place to generate a straight line (with an order of 1 [ONE]),
#in this case we really only care about fp1 and residuals (aka error b/t real data and the model)
#modify the 3rd value in polyfit() to control the order of the line ie how many dimensions () does it allow the line to span... unless im mistaken
fp1, residuals, rank, sv, rcond = np.polyfit(x, y, 1, full = True)

print("Model parameters: %s" % fp1)
print("residuals: %s " % residuals)

f1 = np.poly1d(fp1)
print("error of f1: %s" % error(f1, x, y))

fx = np.linspace(0, x[-1], 1000)        # generate xvalues for plotting

print("fx: %s" % fx)

plt.scatter(x,y, s=10)
plt.title("Web Traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/Hour")
plt.xticks([w*7*24 for w in range(10)], ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)
#draw a slightly opaque, dashed grid
plt.grid(True, linestyle='-', color = '0.75')

#had to put this section here otherwise the new straight line (order of 1) plot wouldn't show properly
plt.plot(fx, f1(fx), linewidth = 2, color = 'green', label = "d=%i" %f1.order)          # dont forget to put the colors in damn quotation marks NOTE: I added the "label" portion here
#plt.legend(["d=%i " % f1.order], loc="upper left")

#added this part when we hit pg 19/20 of the text
f2p = np.polyfit(x,y,2)
print(f2p)
f2 = np.poly1d(f2p)
print("error in f2: %s"  %error(f2, x, y))
#custom added, not in text for this same section
plt.plot(fx, f2(fx), linewidth = 2, color= 'orange', label = "d=%i" %f2.order)          # NOTE: I added the "label" portion here
plt.legend(loc = "upper left")
#plt.legend(["d=%i\nd=%i" %(f1.order, f2.order)], loc="upper left")    #USEFUL TO KNOW -- to pass in multiple formatting elements via % ...you need to utilize a tuple ie (,) using comma delineation per item


plt.show()

