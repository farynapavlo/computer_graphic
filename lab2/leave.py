import matplotlib.pyplot as plt
import random

iter = 100000
x = [0]
y = [0]

for n in range(iter):
    r = random.random() * 100
    xn = x[-1]
    yn = y[-1]
    if r < 10:
        x.append(0.14 * xn + 0.01 * yn - 0.08)
        y.append(0.51 * yn - 1.31)
    elif r < 45:
        x.append(0.43 * xn + 0.52 * yn + 1.49)
        y.append(-0.45 * xn + 0.5 * yn - 0.75)
    elif r < 80:
        x.append(0.45 * xn - 0.49 * yn - 1.62)
        y.append(0.47 * xn + 0.47 * yn - 0.74)
    else:
        x.append(0.49 * xn + 0.02)
        y.append(0.51 * yn + 1.62)

plt.scatter(x, y)
plt.show()