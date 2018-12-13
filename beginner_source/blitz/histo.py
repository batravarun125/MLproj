

#Histogram for c 1 and 6 size random 0 or 1 bias

import numpy as np
import matplotlib.pyplot as plt

alphab = ['0', '0.1','0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0', '', '', '', '', '','']
frequencies = [       0.,  2734293.,    54790.,    36974.,    30393.,
            28025.,    28160.,    31379.,    38365.,    58347., 40279888.,
          3719394.,        0.,        0.,        0.,        0.,        0.,
]

pos = np.arange(len(alphab))
width = 1.0     # gives histogram aspect to the bar diagram

ax = plt.axes()
ax.set_xticks(pos + (width / 2))
ax.set_xticklabels(alphab)

plt.bar(pos, frequencies, width, color='r')
plt.show()