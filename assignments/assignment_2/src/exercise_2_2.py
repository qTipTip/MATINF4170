import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style
matplotlib.style.use('fivethirtyeight')

@np.vectorize
def f1(x):
    if 0 <= x < 1:
        return (1 - x)**3
    else:
        return 0.0

@np.vectorize
def f2(x):
    if 0 <= x < 1:
        return x**3
    else:
        return 0.0

@np.vectorize
def f3(x):
    if 0 <= x < 1:
        return x**3
    elif 1 <= x < 2:
        return (2 - x)**3
    else:
        return 0.0

x_values = np.linspace(-1, 3, 10000)
y_f1 = f1(x_values)
y_f2 = f2(x_values)
y_f3 = f3(x_values)

fig = plt.figure()
plt.plot(x_values, y_f1, label="$B[0, 0, 0, 0, 1](x)$")
plt.plot(x_values, y_f2, label="$B[0, 1, 1, 1, 1](x)$")
plt.plot(x_values, y_f3, label="$B[0, 1, 1, 1, 2](x)$")
plt.legend()
plt.show()
