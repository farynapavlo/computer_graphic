import matplotlib.pyplot as plt

axiom = "F"
Frule = "FbF"
brule = "bbb"
iter = 7
length = 3
l = length / 3 * (iter + 1)

for i in range(iter):
    axiom = axiom.replace("b", brule)
    axiom = axiom.replace("F", Frule)
print(axiom)

x = []
x0 = 0.0
countB = 0
for counter, symbol in enumerate(axiom, start=0):
    if symbol == 'F':
        x.append(x0)
        x.append(x0 + l)
        countB = 0
    if countB == 0 and symbol == 'b':
        x.append(float("NaN"))
        countB += 1
    x0 += l

plt.plot(x, [0] * len(x))
plt.show()