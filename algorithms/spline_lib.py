import numpy as np

"""
This python-file contains implementations of all the algorithms in the
compendium.
"""

def index(t, x):
    assert t[0] <= x < t[-1]
    for i in range(len(t)-1):
        if t[i] <= x < t[i+1]:
            return i

def algorithm_1_1(p, c, t, x):
    assert len(c) == p + 1
    assert len(t) == p + 1

    c = np.array(c, dtype=np.float64)

    for k in range(1, p + 1):
        for j in range(p - k + 1):
            c[j] = (t[j + k] - x) / (t[j + k] - t[j]) * c[j] + (x - t[j]) / (
                t[j + k] - t[j]) * c[j + 1]
    return c[0]

def algorithm_1_2(p, c, x):
    assert len(c) == p+1
    assert 0 <= x <= 1

    c = np.array(c, dtype=np.float64) 
    for k in range(1, p+1):
        for j in range(0, p- k + 1):
            c[j] = (1 - x)*c[j] + x * c[j+1]
    return c[0]


def algorithm_4_9(p, tau, t):
    assert t[0 : p + 1] == tau[0 : p + 1]
    assert t[-(p + 1) : -1] == tau[-(p+1) : -1]
    
    m = len(t) - (p + 1)
    n = len(tau) - (p + 1)
    A = np.zeros(shape=(m, n))
    
    t = np.array(t, dtype=np.float64)
    tau = np.array(tau, dtype=np.float64)

    for i in range(m):
        mu = index(tau, t[i])
        b  = 1
        for k in range(1, p + 1):
            tau1 = tau[mu - k + 1 : mu +1]
            tau2 = tau[mu + 1 : mu + k +1]
            omega = (t[i + k] - tau1) / (tau2 - tau1)
            b = np.append((1 - omega) * b, 0) + np.insert((omega * b), 0, 0)
        A[i,mu - p : mu + 1] = b
    
    return A
if __name__ == "__main__":
    p = 2
    c = [(1, 2), (3, 1), (2, 1)]
    tau = [-1, -1, -1, 0, 1, 1, 1]
    t = [-1, -1, -1, -0.5, 0, 0.5, 1, 1, 1]
    
    algorithm_4_9(p, tau, t)
