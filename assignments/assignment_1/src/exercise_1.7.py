import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style
matplotlib.style.use("fivethirtyeight")

def BasisSpline(p):
    """
    Given a degree p, returns a callable basis function object used for
    computing a spline curve.
    """
    if p == 0:
        def basis(j, t, knots):
            if knots[j] <= t < knots[j+1]:
                return 1.0
            else:
                return 0.0
    else:
        def basis(j, t, knots):
            d_one = (knots[j+p] - knots[j])
            d_two = (knots[j+1+p] - knots[j+1])
            if d_one == 0 or d_two == 0:
                return 0.0
            l_one = (t - knots[j]) / d_one
            l_two = (knots[j+1+p]  - t) / d_two
            B = BasisSpline(p-1)

            return l_one * B(j, t, knots) + l_two * B(j + 1, t, knots)

    # Storing the degree in the function object
    basis.p = p
    return basis

def demo():
    p = 3
    t_values = np.linspace(0, 10, 1000)
    knots = range(10)
    B = BasisSpline(p)
    Bb = BasisSpline(1)
    result = [] 
    resultB = []
    j = 3
    for t in t_values:
        result.append(B(j, t, knots))
        resultB.append(Bb(j, t, knots))
    plt.plot(t_values, result, label='$B_{%d, %d}(t)$' % (j, p), alpha=0.7)
    plt.plot(t_values, resultB, label='$B_{%d, %d}(t)$' % (j, 1), alpha=0.7)
    plt.ylim(-0.1, 1.1)
    plt.legend()
    plt.savefig('bsplines.pdf')
    plt.show()
if __name__ == '__main__':
    demo()
