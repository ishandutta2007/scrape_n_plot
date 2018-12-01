import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from numpy import genfromtxt
import pylab
from scipy import polyval, polyfit

per_data=genfromtxt('table_data1.csv',delimiter=';')
per_data = per_data[slice(4,25)]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
line, = ax.plot(per_data[:,0], per_data[:,1], color='blue', lw=2)

ax.set_yscale('symlog')
ax.grid(True)

pylab.show()
