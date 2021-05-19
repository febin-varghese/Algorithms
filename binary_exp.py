"""
Calculate a^n using binary exponentiation.
Reference: https://cp-algorithms.com/algebra/binary-exp.html
"""


def binary_exp(a, n):
    result = 1
    while n > 0:
        if n & 1:
            result = result * a
        a = a * a
        n >>= 1
    return result


if __name__ == "__main__":
    number = int(input("Enter the number: "))
    power = int(input("Enter the power: "))
    print(f"{number}^{power} = {binary_exp(number, power)}")
