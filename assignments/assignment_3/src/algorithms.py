import numpy as np


def index(x, t):
    """
    Routine for determining the index mu such that t_mu <= x < t_mu+1.
    If x is larger than t[-1], then the last index is returned, for convenience sake.
    If x is smaller than t[0], then the first index is returned, for convenience sake.
    :param x: parameter value
    :param t: knot vector
    :return: mu
    """
    if x < t[0]:
        return 0

    for i in range(len(t) - 1):
        if t[i] <= x < t[i + 1]:
            return i

    return len(t) - 2


def algorithm_1_1(p, c, t, x):
    """
    Routine for computing the polynomial curve q of degree p
    that interpolates the points c.
    :param p: polynomial degree
    :param c: set of points
    :param t: set of strictly increasing parameter values
    :param x: parameter value
    :return: the polynomial q evaluated at x
    """

    q = np.array(c, dtype=np.float64)

    for k in range(1, p + 1):
        for j in range(0, p - k + 1):
            q[j] = (t[j + k] - x) / (t[j + k] - t[j]) * q[j] + (x - t[j]) / (
                t[j + k] - t[j]) * q[j + 1]
    return q[0]


def algorithm_1_2(p, c, x):
    """
    Routine for computing the Bezier curve q of degree p defined by the points
    c.
    :param p: The polynomial degree
    :param c: The set of points
    :param x: The parameter value, between 0 and 1
    :return: the Bezier curve q evaluated at x
    """

    q = np.array(c, dtype=np.float64)

    for k in range(1, p + 1):
        for j in range(0, p - k + 1):
            q[j] = (1 - x) * q[j] + x * q[j + 1]
    return q[0]


def algorithm_2_20(p, t, c, x):
    """
    Routine for computing a spline f of degree p at a point x.
    :param p: the polynomial degree
    :param t: the entire knot vector
    :param c: the entire coefficient vector
    :param x: the parameter value to evaluate at
    :return: the value f(x)
    """

    eps = 1e-14
    mu = index(x, t)
    c0 = np.array(c[mu - p:mu + 1], dtype=np.float64)
    c0 = c0[::-1]

    for k in range(p, 0, -1):
        for i, j in enumerate(range(mu, mu - k, -1)):
            denominator = float(t[j + k] - t[j])

            if abs(denominator) < eps:
                c0[i] = 0.0
                continue

            c0[i] = (t[j + k] - x) / denominator * c0[i + 1] + (
                x - t[j]) / denominator * c0[i]
    return c0[0]


def algorithm_2_20_vector(p, t, c, x):
    """
    Routine for computing a spline f of degree p at a point x.
    :param p: the polynomial degree
    :param t: the entire knot vector
    :param c: the entire coefficient vector
    :param x: the parameter value to evaluate at
    :return: the value f(x)
    """

    mu = index(x, t)
    t = np.array(t, dtype=np.float64)
    c = np.array(c[mu - p:mu + 1], dtype=np.float64)

    for i in range(0, p):
        k = p - i
        t1 = t[mu - k + 1:mu + 1]
        t2 = t[mu + 1:mu + k + 1]
        omega = np.divide((x - t1), (t2 - t1))
        c = (1 - omega) * c[:-1] + omega * c[1:]
    return c


def algorithm_2_21(p, t, x):
    """
       Routine for computing a the non-zero B-splines of degree p at a point x.
       :param p: the polynomial degree
       :param t: the entire knot vector
       :param x: the parameter value to evaluate at
       :return: the values of the non-zero B-splines [B_(mu-p), ..., B_mu] evaluated at x.
       """

    t = np.array(t, dtype=np.float64)
    b = 1
    mu = index(x, t)

    for k in range(1, p + 1):
        t1 = t[mu - k + 1:mu + 1]
        t2 = t[mu + 1:mu + k + 1]
        omega = np.divide(
            (x - t1), (t2 - t1), out=np.zeros_like(t1), where=((t2 - t1) != 0))
        b = np.append((1 - omega) * b, 0) + np.insert((omega * b), 0, 0)

    return b


def algorithm_3_17():
    pass


def algorithm_3_18():
    pass


def algorithm_4_9(p, tau, t):
    """
    Computes the knot insertion matrix that write coarse B-splines as linear combinations
    of finer B-splines.
    :param p: The degree
    :param tau: The coarse knot vector
    :param t: The fine knot vector
    :return: The knot insertion matrix A
    """
    m = len(t) - (p + 1)
    n = len(tau) - (p + 1)

    a = np.zeros(shape=(m, n))
    t = np.array(t, dtype=np.float64)
    tau = np.array(tau, dtype=np.float64)

    for i in range(m):
        mu = index(t[i], tau)
        b = 1
        for k in range(1, p + 1):
            tau1 = tau[mu - k + 1:mu + 1]
            tau2 = tau[mu + 1:mu + k + 1]
            omega = (t[i + k] - tau1) / (tau2 - tau1)
            b = np.append((1 - omega) * b, 0) + np.insert((omega * b), 0, 0)

        a[i, mu - p:mu + 1] = b
    return a


def algorithm_4_10(p, tau, t, c):
    """
    Computes the spline coefficients representing a coarse spline in a finer spline space.
    :param p: The spline degree
    :param tau: The coarse knot vector
    :param t: The fine knot vector
    :param c: The set of coarse spline coefficients
    :return: The set of fine spline coefficients
    """

    m = len(t) - (p + 1)
    n = len(tau) - (p + 1)
    c = np.array(c, dtype=np.float64)
    t = np.array(t, dtype=np.float64)
    tau = np.array(tau, dtype=np.float64)
    b = np.zeros(m)

    for i in range(m):
        mu = index(t[i], tau)
        if p == 0:
            b[i] = c[mu]
        else:
            C = c[mu - p:mu + 1]
            for j in range(0, p):
                k = p - j
                tau1 = tau[mu - k + 1:mu + 1]
                tau2 = tau[mu + 1:mu + k + 1]
                omega = np.divide(
                    (t[i + k] - tau1), (tau2 - tau1),
                    out=np.zeros_like(tau1),
                    where=((tau2 - tau1) != 0))
                C = (1 - omega) * C[:-1] + omega * C[1:]
            b[i] = C
    return b
