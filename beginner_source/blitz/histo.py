

#Histogram for c 1 and 6 size random 0 or 1 bias

import numpy as np
import matplotlib.pyplot as plt

alphab = ['0', '0.1','0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0', '', '', '', '', '','']
frequencies = [  0,169630336.,   7041086.,   6404428.,   5833380.,
           5305149.,   4789672.,   4276549.,   3841539.,   3480439.,   3302671.,
           2740319.,   2152036.,   1850439.,   1604309.,   1395980.,   1220403.,]

pos = np.arange(len(alphab))
width = 1.0     # gives histogram aspect to the bar diagram

ax = plt.axes()
ax.set_xticks(pos + (width / 2))
ax.set_xticklabels(alphab)

plt.bar(pos, frequencies, width, color='r')
plt.show()