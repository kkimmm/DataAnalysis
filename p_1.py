import pylab
import numpy as np
import matplotlib.pyplot as plt
 
N = 5
ind = np.arange(N)
width = 0.35
menMeans = (20, 35, 30, 35, 27)
menStd = (2, 3, 4, 1, 2)
 
womenMeans = (25, 32, 34, 20, 25)
womenStd = (3, 5, 2, 3, 3)
 
plt.bar(ind, menMeans, width, color='r', yerr=menStd)
plt.bar(ind+width, womenMeans, width, color='y', yerr=womenStd)
plt.title('Men-Women')