from neville_aitken import NevAit
import numpy as np
import matplotlib.pyplot as plt

N = [3, 7, 11, 15]
res = 100

np.random.seed(seed=1)
random_knots  = np.cumsum(np.random.randint(1, 3, size=N[-1]))
for i, n in enumerate(N):
    x_values = np.linspace(0, np.pi, n)
    y_values = [(np.cos(x), np.sin(x)) for x in x_values]
    #  knots = range(n) #
    knots = random_knots[:n]
    print(knots)
    f_values = []
    t_values = np.linspace(knots[0], knots[-1], res)
    for t in t_values:
        f_values.append(NevAit(t, y_values, knots))
    plt.subplot(2, 2, i+1)
    plt.axis('off')
    plt.xlim(-2, 2)
    plt.ylim(-0.5, 3)
    plt.plot(*zip(*f_values), alpha=0.8, label='$N = %d$' % n)
    plt.scatter(*zip(*y_values), c='black', zorder=100) 
    plt.legend(loc='best')
plt.savefig('random.pdf')
plt.show()
