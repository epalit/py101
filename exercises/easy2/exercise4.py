from math import isnan

def multiply(num1, num2):
    return num1 * num2

def power(num, exponent):
    if exponent == 0:
        return 1
    if num == 0 and exponent < 0:
        return float('nan')

    result = num
    positive_exp = abs(exponent)
    for _ in range(1, positive_exp):
        result = multiply(result, num)

    if exponent < 0:
        result = 1 / result
    return result

print(power(5, 2) == 25)   # True
print(power(-8, 2) == 64)  # True
print(power(3, 3) == 27)  # True
print(power(4, 0) == 1)  # True
print(power(2, -1) == 0.5)  # True
print(power(2, -3) == 0.125)  # True
print(isnan(power(0, -1))) # True
