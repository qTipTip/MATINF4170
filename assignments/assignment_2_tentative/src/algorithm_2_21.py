import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style
matplotlib.style.use("fivethirtyeight")

from index_finder import IndexBinary as index

def BSplineEvaluation(x, p, knots):
    """
    Evaluate the p+1 active B-splines at the point x.
    Given x, find the index mu such that knots[mu] <= x < knots[mu+1].
    We only need the knots knots[mu - p + 1] to knots[mu + p].
    """ 
    knots = np.array(knots, dtype=np.float64)
    mu = index(x, knots)
    b = 1
    for k in range(1, p+1):
        # extract relevant knots
        t1 = knots[mu - k + 1 : mu+1]
        t2 = knots[mu+1 : mu + k+1]
        # append 0 to end of first term, and insert 0 to start of first term
        omega = (x - t1) / (t2 - t1)
        b = np.append((1 - omega)*b, 0)  + np.insert((omega * b), 0, 0)
    return b

def demo():

    n = 10 # number of splines we can define
    p = 3  # B-spline degree
    j = 4  # B_jp
    t = range(n + p + 1) # knot vector, uniform
    
    splines = []
    eps = 1.0e-14
    x_values = np.linspace(t[j], t[j+1]-eps, 1000)
    for x in x_values:
        splines.append(BSplineEvaluation(x, p, t))
    plt.plot(x_values, splines) 
    plt.scatter(*zip(*[(k, 0) for k in t[j-1:j+3]]), s=100, zorder=100)
    plt.legend(labels=['$B_{1, 3}(x)$', '$B_{2, 3}(x)$', '$B_{3, 3}(x)$', '$B_{4, 3}(x)$'])
    plt.savefig('active_b_splines.pdf')
    plt.show()


if __name__ == "__main__":
    demo()