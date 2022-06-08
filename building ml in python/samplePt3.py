#this follows ~pg 82 of the PDF, 3rd edition
# these assholes didnt actually fucking check to see if the code worked
# now i have to go through myself and figure out why the graphs are all fucky
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt


def error(f, x, y):
    return np.sum((f(x)-y)**2)

data = np.genfromtxt("ch1_data/web_traffic_2.tsv", delimiter="\t")

print(data[:10])
print(data.shape)



x = data[:,0]           #hours
y = data[:,1]           #website hits in an hour

np.sum(np.isnan(y))     #checking how many invalid data entries are present in the "website hits"

#removing invalid data from both the x and y data columns
x = x[~np.isnan(y)]
y = y[~np.isnan(y)]


inflection = int(3.5*7*24)              # calculate the inflection point in hours, (3.5 because thats approx how many weeks 
                                        # in where the graph starts showing major changes, if there was a significant change
                                        # around 2.3 weeks in then you would use that value instead)
                                        # 7 is the number of days in the week, and 24 is how many hrs per day.

xa = x[:inflection]                     # data before the inflection point (which is in hours btw)
ya = y[:inflection]
xb = x[inflection:]                     # data after inflection point (again, inflection point is in hrs)
yb = y[inflection:]
# int()'s encapsulation of 3.5*7*24 was added only in 3rd edition, not 2nd edition

fa = np.poly1d(np.polyfit(xa, ya, 1))
fb = np.poly1d(np.polyfit(xb, yb, 1))

fa_error = error(fa, xa, ya)
fb_error = error(fb, xb, yb)

print("Error inflection= %f" %(fa_error + fb_error))   # adding the two errors because we want the total error for the graph, and we split it into two smaller subunits just a few lines above

# ------------------------------------------------------------------------------

def plot_web_traffic(x, y, models = None, mx = None, ymax = None):
    '''
    Had to pack the former block of code that built the graph into this

    NOTE
    plot the web traffic Y over time X.
    if models are given, it is expected to be a list of fitted models,
    which will be plotted as well (used below)
    '''
    plt.figure(figsize = (12,6))          # width and height of the plot in inches
    plt.scatter(x, y, s=10)
    plt.title("Web Traffic over the last month")

    plt.xlabel("Time")
    plt.ylabel("Hits/Hour")
    plt.xticks([w*7*24 for w in range(5)], ['week %i' % (w+1) for w in range(5)])

    if models:
        colors = ['g', 'k', 'b', 'm', 'r']
        linestyles = ['-', '-.', '--', ':', '-']

        #mx = np.linspace(0, x[-1], 1000)
        mx = np.linspace(0, 6*7*24, 100)
        ymax = 10000
        for model, style, color in zip(models, linestyles, colors):
            plt.plot(mx, model(mx), linestyle = style, linewidth = 2, c = color)

        plt.legend(["d=%i" %m.order for m in models], loc = "upper left")
    plt.autoscale(tight=True)
    plt.grid(True, linestyle = '-', color = '0.75')

'''
NOTE moved into plot_web_traffic
fx = np.linspace(0, x[-1], 1000)        # generate xvalues for plotting
plt.autoscale(tight=True)
#draw a slightly opaque, dashed grid
plt.grid(True, linestyle='-', color = '0.75')

#use the fa and fb made above
plt.plot(fx, fa(fx), linewidth = 2, color = 'green', label = "d=%i" %fa.order)          # dont forget to put the colors in damn quotation marks NOTE: I added the "label" portion here
plt.plot(fx, fb(fx), linewidth = 2, color = 'red', label = "d=%i" %fb.order)
plt.legend(loc = "upper left")
'''
#creating other higher degree (what i formerly called orders/dimensions) line plots
fb1 = np.poly1d(np.polyfit(xb, yb, 1))
fb2 = np.poly1d(np.polyfit(xb, yb, 2))
fb3 = np.poly1d(np.polyfit(xb, yb, 3))
fb10 = np.poly1d(np.polyfit(xb, yb, 10))
fb100 = np.poly1d(np.polyfit(xb, yb, 100))


print("Errors for only the time after inflection point")
for f in [fb1, fb2, fb3, fb10, fb100]:
    print("td=%i: %f" %(f.order, error(f,xb, yb)))

#print(x, ' x-value & then ', y, ' y-value')

plot_web_traffic(x, y, [fb1, fb2, fb3, fb10, fb100])
'''
plot_web_traffic(x, y, [fb1, fb2, fb3, fb10, fb100],
    mx = np.linspace(0, 6*7*24, 100),
    ymax= 10000)
'''



plt.show()
