import SEAL
import numpy as np

curve = np.loadtxt('data/hj1.dat')
u = SEAL.parametrize(curve, data_type='curve') 
p = 2
n = 8 
t = SEAL.create_knots(u[0], u[-1], p, n)
S = SEAL.SplineSpace(p, t)
f = SEAL.least_squares_spline_approximation(u, curve, S)
print(f.c[0], curve[0])
f.c[0] = curve[0]
f.c[-1] = curve[-1]
t_values = S.parameter_values(resolution=100)
f_values = f(t_values)
import matplotlib.pyplot as plt
import matplotlib.style
from mpl_toolkits.mplot3d import Axes3D

matplotlib.style.use('fivethirtyeight')
fig = plt.figure(figsize=(10, 10), dpi=1)
axs = Axes3D(fig)
axs.set_axis_off()
axs.plot(*zip(*f_values), lw=2, label='approximation')
axs.plot(*zip(*f.control_polygon), lw=1, alpha=0.5, color='black', label='control polygon')
axs.scatter(*zip(*f.control_polygon), alpha=0.2, color='black')
axs.scatter(*zip(*curve), alpha=0.2, label='original data')
plt.legend(loc='center', frameon=False)
plt.savefig('example.pdf', transparent=True, bbox_inches='tight')
