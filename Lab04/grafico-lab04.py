%matplotlib inline
from pylab import *
import numpy as np
import matplotlib.ticker as tkr
import matplotlib.pyplot as plt

def func(x, pos): # changes format to dot to comma
    s = str(x)
    ind = s.index('.')
    return s[:ind] + ',' + s[ind+1:] + '0'

ax = plt.subplot()

x = np.arange(0, 1, 0.001)

pX = [0.145, 0.096, 0.057, 0.097, 0.017]
pY = [0.068, 0.048, 0.030, 0.049, 0.010]

errorX = [0, 0, 0, 0, 0]
errorY = [0.0003, 0.0003, 0.0003, 0.0003, 0.0003]

xFormatter = FormatStrFormatter('%.3f')
yFormatter = FormatStrFormatter('%.3f')

cFormatter = tkr.FuncFormatter(func)

line, = plt.plot(x, 0.459 * x + 3.056 * 10**(-3), label=r"$y$ $=$ $0,459x + 3,056 \cdot 10^{-3}$", color="green")

ax.legend(loc=2) # upper left corner
ax.set_xlabel(r'$\frac{1}{t^2}$ $(\frac{1}{s^2})$', fontsize=18)
ax.set_ylabel(r'$\Delta m$ $(Kg)$', fontsize=12)

plt.plot(pX, pY, 'bo', markersize = 3)

plt.errorbar(pX, pY, yerr=0.0003, xerr=0, fmt='none', capsize=1)

plt.xlim(0,0.160)
plt.ylim(0,0.080)

plt.xticks(np.arange(0.04, 0.161, 0.04))
plt.yticks(np.arange(0.02, 0.081, 0.02))

ax.xaxis.set_major_formatter(xFormatter)
ax.yaxis.set_major_formatter(yFormatter)

ax.xaxis.set_major_formatter(cFormatter)
ax.yaxis.set_major_formatter(cFormatter)

plt.show()
