import matplotlib.pyplot as plt
import random;
import numpy as np


colors = [[0,0,0,0.4],[0,0,0,0.5],[0,0,0,0.1],[0,0,0,0.2],[0,0,0,0.3]];
cmap = 'gray';
x = [0,0,0,0,0]; y = [1,2,3,4,5];

plt.scatter(y,x,s=130, c=colors, cmap=cmap,marker = "s")

plt.colorbar()
plt.show()

