from math import sqrt
import matplotlib.pyplot as plt

iter = 5
x0 = [[0.0, 1.0, 0.5, 0]]
y0 = [[0.0, 0.0, (sqrt(3) / 2), 0]]
plt.plot(x0[0], y0[0])


def t(a, b, c, d, e, f):
    x = []
    y = []
    for p in range(len(x0)):
        xn = []
        yn = []
        for i in range(len(x0[p])):
            xn.append(x0[p][i] * a + y0[p][i] * b + c)
            yn.append((x0[p][i] * d + y0[p][i] * e + f))
        x.append(xn)
        y.append(yn)
        plt.plot(xn, yn)
    return [x, y]

for i in range(iter):
    t1 = t(0.5, 0.0, 0.0, 0.0, 0.5, 0.0)
    t2 = t(0.5, 0.0, 0.5, 0.0, 0.5, 0.0)
    t3 = t(0.5, 0, 0.25, 0, 0.5, sqrt(3) / 4)
    x0.clear()
    x0 = t1[0]
    x0.extend(t2[0])
    x0.extend(t3[0])
    y0.clear()
    y0 = t1[1]
    y0.extend(t2[1])
    y0.extend(t3[1])

plt.show()