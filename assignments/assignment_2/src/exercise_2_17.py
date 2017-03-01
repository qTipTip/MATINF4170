from algorithm_2_20 import SplineEvaluation

import numpy as np
import matplotlib.pyplot as plt

n = 10
p = 3
mu = 4
knots = range(n + p + 1)
coefficients = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]

for x in np.linspace(knots[0], knots[-1], 20):
    f_x = SplineEvaluation(x, p, knots, coefficients, mu=7)
    print(knots[7] <= x < knots[8], f_x)
