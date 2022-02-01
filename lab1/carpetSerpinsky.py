import matplotlib.pyplot as plt
from math import pi, cos, sin

axiom = "FXF--FF--FF"
Frule = "FF"
Xrule = "--FXF++FXF++FXF--"
iter = 5
length = 1
axel = pi / 3

for i in range(iter):
    string = ''
    for s in axiom:
        if s == 'X':
            string += Xrule
        elif s == 'F':
            string += Frule
        else:
            string += s
        axiom = string
print(axiom)

x = [0.0]
y = [0.0]
length = 1
alpha = 0
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