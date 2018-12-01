import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from numpy import genfromtxt
import pylab
from scipy import polyval, polyfit
from scipy.optimize import curve_fit
np.set_printoptions(formatter={'float': lambda x: "{0:0.1f}".format(x)})


def func(x, a, b, c):
    return a*np.exp(b*(x-1600)) + c

def f(x_cons, y_cons):
    popt, pcov = curve_fit(lambda t,a,b,c: a*np.exp(b*(t-1600)) + c,  x_cons,  np.log(y_cons),  p0=(0.2, 0.01, 4))
    x_ext = np.concatenate((np.arange(2100,2005,-5),x_cons), axis=0)
    ylog_ext = func(x_ext, *popt)
    return x_ext, ylog_ext

per_data=genfromtxt('table_data1.csv',delimiter=';')
per_data = per_data[slice(4,25)]

plt.plot(per_data[:,0], np.log(per_data[:,1]), '-ko',color='blue')

x_ext, ylog_ext = f(per_data[:,0], per_data[:,1])
plt.plot(x_ext, ylog_ext, 'r-', color='red')

plt.yticks(ylog_ext, np.around(np.exp(ylog_ext)/1000))

x_ext, ylog_ext = f(per_data[0:18,0], per_data[0:18,1])
plt.plot(x_ext, ylog_ext, '-kx', color='green')

x_ext, ylog_ext = f(per_data[0:16,0], per_data[0:16,1])
plt.plot(x_ext, ylog_ext, color='yellow')

x_ext, ylog_ext = f(per_data[0:14,0], per_data[0:14,1])
plt.plot(x_ext, ylog_ext, color='black')

plt.grid(True)
mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())
plt.show()
