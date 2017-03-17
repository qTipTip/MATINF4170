import numpy as np
import matplotlib.style
matplotlib.style.use('fivethirtyeight')
import matplotlib.pyplot as plt
from algorithms import algorithm_2_20 as evaluate, algorithm_4_10 as insert_knots


def insert_midpoints(x, p):
    """
    Routine for inserting n - 1 midpoints in a p+1 extended knot vector, using numpy
    vector operations.
    """
    midpoints = (x[p:-p - 1] + x[p + 1:-p]) / 2
    new_array = np.zeros(len(x) + len(midpoints), dtype=np.float64)

    new_array[:p + 1] = x[:p + 1]
    new_array[-p - 1:] = x[-p - 1]
    new_array[p + 1:p + 2 * len(midpoints):2] = midpoints
    new_array[p + 2:p + 2 * len(midpoints) - 1:2] = x[p + 1:-p - 1]

    return new_array


def get_control_points(t, p, c):
    """
    Given a p+1 extended knot vector t and a set of coefficients c, returns the
    control polygon [(t*, cj)] where t* is a knot average.
    """
    control_points = []
    n = len(c)
    for j in range(0, n):
        t_average = sum(t[j + 1:j + p + 1]) / float(p)
        control_points.append((t_average, c[j]))
    return control_points


def example_1():

    p = 3
    t = np.array([0, 0, 0, 0, 1, 2, 3, 4, 4, 4, 4])
    c = [-1, 1, -1, 1, -1, 1, -1]

    # exact
    x_values = np.linspace(t[0], t[-1] - 1.0e-14, 100)
    y_values = [evaluate(p, t, c, x) for x in x_values]
    control_poly = get_control_points(t, p, c)
    
    f, axes = plt.subplots(4, 1, sharex='col', sharey='row')

    axes[0].plot(x_values, y_values, lw=1)
    axes[0].plot(*zip(*control_poly), color='grey', label='subdivisions: 0', lw=1)
    axes[0].scatter(*zip(*control_poly), color='grey', s=20)

    # knot insertions
    n = 3
    for i in range(n):
        refined_t = insert_midpoints(t, p)
        refined_c = insert_knots(p, t, refined_t, c)
        control_poly = get_control_points(refined_t, p, refined_c)

        t = refined_t
        c = refined_c
        axes[i+1].plot(x_values, y_values, lw=1)
        axes[i+1].plot(*zip(*control_poly), color='grey', label='subdivisions: {n}'.format(n=i+1), lw=1)
        axes[i+1].scatter(*zip(*control_poly), color='grey', s=20)

    for ax in axes:
        ax.set_xticks([])
        ax.set_yticks([])

    plt.tight_layout()
    plt.savefig('example_1.pdf')

def example_2():

    p = 2
    t = np.array([0,0, 0,1, 2, 3, 3, 3])
    c = [-3, -6, 5, -0.5, 6]

    # exact
    x_values = np.linspace(t[0], t[-1] - 1.0e-14, 100)
    y_values = [evaluate(p, t, c, x) for x in x_values]
    control_poly = get_control_points(t, p, c)
    
    f, axes = plt.subplots(4, 1, sharex='col', sharey='row')

    axes[0].plot(x_values, y_values, lw=1)
    axes[0].plot(*zip(*control_poly), color='grey', label='subdivisions: 0', lw=1)
    axes[0].scatter(*zip(*control_poly), color='grey', s=20)

    # knot insertions
    n = 3
    for i in range(n):
        refined_t = insert_midpoints(t, p)
        refined_c = insert_knots(p, t, refined_t, c)
        control_poly = get_control_points(refined_t, p, refined_c)

        t = refined_t
        c = refined_c
        axes[i+1].plot(x_values, y_values, lw=1)
        axes[i+1].plot(*zip(*control_poly), color='grey', label='subdivisions: {n}'.format(n=i+1), lw=1)
        axes[i+1].scatter(*zip(*control_poly), color='grey', s=20)

    for ax in axes:
        ax.set_xticks([])
        ax.set_yticks([])

    plt.tight_layout()
    plt.savefig('example_2.pdf')

if __name__ == "__main__":
    example_1()
    example_2()
