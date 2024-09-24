import math


def f(x):
    if x < 2:
        return 1 / math.sin(math.exp(x))
    elif 2 <= x < 3:
        return 1 / math.cos(math.log(x))
    else:
        return math.sin(math.log(x))


x = 1.5
while x < 3.5:
    print(round(x, 1), f(x))
    x += 0.2