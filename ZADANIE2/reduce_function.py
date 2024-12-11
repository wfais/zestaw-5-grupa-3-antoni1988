from fractions import Fraction
from functools import reduce


def product(fracs):
    fraction = reduce(lambda x, y: x * y, fracs)
    return fraction.numerator, fraction.denominator

if __name__ == "__main__":
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
