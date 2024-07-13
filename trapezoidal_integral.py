from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math
def f(x):
    return sin(x)

a = 0
b = math.pi / 2
n = 100

h = (b - a) / n

sum = 0.5 * (f(a) + f(b))
for i in range(1, n):
    sum += f(a + i * h)
sum *= h

print("答えは"+str(sum))