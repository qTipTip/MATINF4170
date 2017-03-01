import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style
matplotlib.style.use("ggplot")
from index_finder import IndexNaive as index
from bsplines import BasisSpline


def SplineEvaluation(x, p, knots, coefficients, mu=None):
    """
    Given a polynomial degree p, a list of n + p + 1 knots, a list of n
    coefficients, and a parameter x. If no index mu is supplied, find the
    appropriate one using a method.

    Returns:
        The value the spline function f with given coefficients at the
        parameter x.
    """
    if mu is None:
        mu = index(x, knots)
    knots = np.array(knots, dtype=np.float64)
    c = np.array(coefficients[mu - (p):mu + 1], dtype=np.float64)
    for i in range(0, p):
        k = p - i
        t1 = knots[mu - k + 1:mu + 1]
        t2 = knots[mu + 1:mu + k + 1]
        omega = (x - t1) / (t2 - t1)
        c = (1 - omega) * c[:-1] + omega * c[1:]
    return c

def f(x):
    return np.sin(x)

def demo():
    n = 1000
    p = 3
    knots = [-1]*(p+1) + list(range(n  - p - 2)) + [5]*(p+1)
    variation_dim_points = [(knots[j+1] + knots[j+2]) / 2.0 for j in range(1, n+1)]
    coefficients = [f(x) for x in variation_dim_points]
    
    eps = 1.0e-14
    x_values = np.linspace(knots[0], knots[-1]-eps, 1000)
    f_values = f(x_values)
    
    spline_values = np.zeros(len(x_values))
    for i, x in enumerate(x_values):
        spline_values[i] = SplineEvaluation(x, p, knots, coefficients)
    plt.plot(x_values, f_values, label='$\\sin(x)$')
    plt.plot(x_values, spline_values, label='$Q[\\sin(x)]$')
    plt.xlim(-1.1, 5.1)
    plt.ylim(-1.1, 1.1)
    plt.grid('off')
    plt.legend()
    plt.savefig('variation_diminishing_spline_approximation.pdf', bbox_inches='tight')
    plt.show()


def test():
    c = [-1, 1, -1, 1, -1, 1, -1, 1, -1]
    p = 3
    t = [-1, -1, -1, -1, 0, 1, 2, 3, 4, 5, 5, 5, 5]
    eps = 1.0e-14
    x_values = np.linspace(t[0], t[-1]-eps, 100)
    result = np.zeros(100)
    for i, x in enumerate(x_values):
        result[i] = SplineEvaluation(x, p, t, c)
    plt.plot(x_values, result)
    plt.grid('off')
    plt.savefig('example_spline.pdf', bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    demo()
    test()
