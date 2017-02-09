from decasteljau import deCasteljau
    
import numpy as np
import matplotlib.pyplot as plt

N = [3, 7, 11, 15]
res = 100

for i, n in enumerate(N):
    x_values = np.linspace(0, np.pi, n)
    y_values = [(np.cos(x), np.sin(x)) for x in x_values]
    f_values = []
    t_values = np.linspace(0, 1, res)
    for t in t_values:
        f_values.append(deCasteljau(t, y_values))
    plt.subplot(2, 2, i+1)
    plt.axis('off')
    plt.plot(*zip(*f_values), alpha=0.8, label='$N = %d$' % n)
    plt.scatter(*zip(*y_values), c='black', zorder=100) 
    plt.legend(loc='best')
plt.savefig('bezier.pdf')
plt.show()
