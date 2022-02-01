from math import pi, cos, sin
import matplotlib.pyplot as plt

axiom = "FX"
axel = pi/2
Xrule = "X+YF+"
Yrule = "-FX-Y"
iter = 10


x = [0.0]
y = [0.0]
length = 1
alpha = 0
stack = []


for i in range(iter):
    string = ''
    for s in axiom:
        if s == 'X':
            string += Xrule
        elif s == 'Y':
            string += Yrule
        else:
            string += s
        axiom = string



print(axiom)
for counter, symbol in enumerate(axiom, start=0):
    if symbol == 'F':
        x.append(x[-1] + length * cos(alpha))
        y.append(y[-1] + length * sin(alpha))
    elif symbol == '+':
        alpha += axel
    elif symbol == '-':
        alpha -= axel


print(x, y, sep="\n")
plt.plot(x, y)
plt.show()