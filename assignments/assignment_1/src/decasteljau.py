import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style
matplotlib.style.use("fivethirtyeight")

def deCasteljau(T, c_points, interval_start=0, interval_stop=1):
    """
    The de Casteljau algorithm.
    Given p + 1 control points c_points, computes the point on the bezier curve
    at parameter value T.
    """
    T = (interval_stop - T) / float(interval_stop - interval_start)
    c = np.array(c_points, dtype=np.float64)
    p = len(c_points) - 1

    for k in range(1, p+1):
        for j in range(0, p - k + 1):
            c[j] = (1-T)*c[j] + T * c[j+1]

    return c[0]

def demo(): 
    c = [(i, np.random.randint(-10, 10)) for i in range(5)]

    result = []
    for T in np.linspace(0, 1, 1000):
        result.append(deCasteljau(T, c))

    plt.plot(*zip(*result))
    plt.plot(*zip(*c), alpha=0.3, c='grey')
    plt.scatter(*zip(*c), s=100, zorder=10)
    plt.show()

if __name__ == "__main__":
    demo()
