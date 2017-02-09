import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style
matplotlib.style.use("fivethirtyeight")

def NevAit(T, c_points, t_points):
    """
    The Neville Aitkens Given p + 1 control points c_points and p+1
    strictly increasing parameter values t_points, computes the polynomial
    curve of degree p that interpolates the control points.
    """
    t = t_points
    c = np.array(c_points, dtype=np.float64)
    p = len(c) - 1
    eps = 1.0e-14
    for k in range(1, p + 1):
        for j in range(0, p - k + 1):
            denum = (t[j+k] - t[j]) 
            if abs(denum) <= eps:
                c[j] = 0
                continue
            l_one = (t[j+k] - T) / denum
            l_two = (T - t[j]) / denum
            c[j] = l_one*c[j] + l_two * c[j+1]
    return c[0]

def demo():
    c = [(i, np.random.randint(-10, 10)) for i in range(5)]
    t = [0.0]*(len(c))

    result = []
    for T in np.linspace(t[0], t[-1], 100):
        result.append(NevAit(T, c, t_points=t))

    plt.plot(*zip(*result))
    plt.plot(*zip(*c), alpha=0.3, c='grey')
    plt.scatter(*zip(*c), s=100, zorder=10)
    plt.show()

    
if __name__ == "__main__":
    demo()
