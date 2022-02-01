import matplotlib.pyplot as plt
import random

file = open("affineTransformation3", "r")
arrayT = [[float(number) for number in line.split()] for line in file.readlines()]
arrayP = [] if len(arrayT[0]) < 7 else [i[6] for i in arrayT]
print(arrayP)
iteration = 10000
x0 = [0.0]
y0 = [0.0]

def t(coeficients):
    x = []
    y = []
    for i in range(len(x0)):
        x.append(x0[i] * coeficients[0] + y0[i] * coeficients[1] + coeficients[4])
        y.append(x0[i] * coeficients[2] + y0[i] * coeficients[3] + coeficients[5])
    return x, y

def tp(coeficients):
    x = x0[-1] * coeficients[0] + y0[-1] * coeficients[1] + coeficients[4]
    y = x0[-1] * coeficients[2] + y0[-1] * coeficients[3] + coeficients[5]
    return x, y


for i in range(iteration):
    x = []
    y = []
    if len(arrayP) > 0:
        r = random.random()
        res = next(index for index, val in enumerate(arrayP) if val > r)
        xn, yn = tp(arrayT[res])
        x0.append(xn)
        y0.append(yn)
    else:
        for j in arrayT:
            xn, yn = t(j)
            x.extend(xn)
            y.extend(yn)
        x0.clear()
        y0.clear()
        x0.extend(x)
        y0.extend(y)
        plt.scatter(x0, y0, c='b')
plt.scatter(x0, y0, s=0.2, c='b')
plt.show()
