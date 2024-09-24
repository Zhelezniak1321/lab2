import math


def S(x):
    result = 0
    for k in range(2, 100):
        term = ((-1)**k * math.cos(k * x)) / (k**2 - 1)
        result += term
        if abs(term) < 0.001:  
            break
    return result


x = -1
while x <= -0.9:
    print(x, S(x))  
    x += 0.01 