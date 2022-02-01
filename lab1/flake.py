from math import pi, cos, sin
import matplotlib.pyplot as plt

axiom = "F++F++F"
axel = pi/3
rule = "F-F++F-F"
iter = 2

x = [0.0]
y = [0.0]
length = 1
alpha = 0

for i in range(iter):
    axiom = axiom.replace('F', rule)

for counter, symbol in enumerate(axiom, start=0):
    if symbol == 'F':
        x.append(x[-1] + length * cos(alpha))
        y.append(y[-1] + length * sin(alpha))
    elif symbol == '+':
        alpha += axel
    elif symbol == '-':
        alpha -= axel
    # else:
    #     #     Exception("Non such element")
plt.plot(x, y)
plt.show()
