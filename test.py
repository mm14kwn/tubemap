#! python
import numpy as np
import matplotlib.pyplot as plt
from svgpathtools import svg2paths2
paths, attributes, svg_attributes = svg2paths2('lines.svg')
ll = []
for ind in range(0, len(paths)):
    pl = []
    for jnd in range(0, len(paths[ind])):
        # pl2 = []
        # for knd in range(0, len(paths[ind][jnd])):
        #     pl2.append(paths[ind][jnd][knd])
        # pl.append(np.asarray(pl2))
        p1 = paths[ind][jnd].point(0)
        p2 = paths[ind][jnd].point(-1)
        p1x = np.real(p1)
        p1y = np.imag(p1)
        p2x = np.real(p2)
        p2y = np.imag(p2)
        pl.append(np.asarray(((p1x, p1y), (p2x, p2y))))
    ll.append(np.asarray(pl))
ln = np.asarray(ll)
for ind in range(0, len(ll)):
    for jnd in range(0, ll[ind].shape[0]):
        plt.plot(ll[ind][jnd, :, 0], ll[ind][jnd, :, 1])
plt.show()
