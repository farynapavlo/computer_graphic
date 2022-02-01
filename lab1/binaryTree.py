from math import pi, cos, sin
import matplotlib.pyplot as plt

axiom = "F"
axel = pi/7
rule = "F[+F]F[-F]F"
iter = 8

x = [0.0]
y = [0.0]
length = 1
alpha = pi/2
stack = []

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
    elif symbol == '[':
        stack.append([x[-1], y[-1], alpha])
    elif symbol == ']':
        i = len(x) - 2
        while(stack[-1][0] != x[i] and stack[-1][1] != y[i]):
            x.append(x[i])
            y.append(y[i])
            i -= 1
        x.append(stack[-1][0])
        y.append(stack[-1][1])
        alpha = stack[-1][2]
        stack.pop()

# print(x, y, sep="\n")
plt.plot(x, y)
plt.show()