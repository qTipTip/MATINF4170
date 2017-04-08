import SEAL
import glob
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.style
#  from mayavi import mlab
from mpl_toolkits.mplot3d import Axes3D
matplotlib.style.use('ggplot')

data = [np.loadtxt(filename) for filename in glob.glob('data/*.dat')]
# set up spline space and find least square approximations
p = 3
splines_and_parameter_endpoint = []
cmaps = ['viridis', 'magma', 'plasma']
for k, lmbda in enumerate([5, 10, 20]):
    fig = plt.figure(figsize=(10, 10), dpi=1)
    ax1 = fig.add_subplot(1, 1, 1, projection='3d')
    ax1.set_axis_off()
    #  ax2 = fig.add_subplot(2, 1, 2, projection='3d')

    for curve in data:
        curve = np.vstack((curve, curve[0]))
        u = SEAL.parametrize(curve, data_type='curve')
        n = int(lmbda*len(u) / 100.0)
        knots = SEAL.create_knots(u[0], u[-1] , p, n)
        s = SEAL.SplineSpace(p, knots)     
        f = SEAL.least_squares_spline_approximation(u, curve, s)
        splines_and_parameter_endpoint.append((f, u[-1]-1.0e-14))
        x = s.parameter_values(resolution=200)
        y = f(x)
        
        #  ax1.plot(*zip(*y))
    #  plt.savefig('curves_lambda_{l}.pdf'.format(l=lmbda), bbox_inches='tight', transparent=True)
    #  create gridded data and parametrize
    data_values = np.zeros(shape=(20, 9, 3))
    u = np.array([i / 19.0 for i in range(20)])
    v = np.array([j / 8.0 for j in range(9)])
    for i in range(20):
        for j in range(9):
            f, uj = splines_and_parameter_endpoint[j]
            data_values[i, j, :] = f(i * uj / 19.0)

    # knots
    x_knots = SEAL.create_knots(u[0], u[-1] , p, 11)
    y_knots = SEAL.create_knots(v[0], v[-1], p, 5)
    T = SEAL.TensorProductSplineSpace([p, p], [x_knots, y_knots])
    f = SEAL.least_squares_tensor_approximation([u, v], data_values, T)

    x, y = T.parameter_values(resolution=200)
    f_vals = f(x, y)
    c = f.control_mesh
    fig = plt.figure(figsize=(10, 10), dpi=1)
    ax2 = fig.add_subplot(1, 1, 1, projection='3d')
    ax2.set_axis_off()
    ax2.plot_surface(f_vals[:, :, 0], f_vals[:, :, 1], f_vals[:, :, 2], cmap=cmaps[k])
    plt.savefig('surfaces_lambda_{l}.pdf'.format(l=lmbda), bbox_inches='tight', transparent=True)

#  #  mlab.mesh(f_vals[:, :, 0], f_vals[:, :, 1], f_vals[:, :, 2])
#  #  mlab.savefig('heart.obj')
#  #  mlab.show()
