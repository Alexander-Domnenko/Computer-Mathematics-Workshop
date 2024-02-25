from math import factorial, pi
import matplotlib.pyplot as plt


def calculation_exp(x, n):
    return (x ** n) / factorial(n)


def calculation_cos(x, i, _a=0):
    return (-1) ** i * x ** (2 * i + _a) / factorial(2 * i + _a)


def calculation_sin(x, n):
    return ((x ** (2 * n + 1)) * (-1) ** n) / factorial(2 * n + 1)


def calculation_arcsin(x, n):
    return (factorial(2 * n) * (x ** (2 * n + 1))) / ((4 ** n) * factorial(n) * factorial(n) * (2 * n + 1))


def calculation_arccos(x, n):
    return calculation_arcsin(x, n)


def search_points(f, interval, n):
    X = []
    Y = []
    for i in range(-interval, interval+1):
        lst = []
        X.append(i/2)
        for j in range(n+1):
            lst.append(f(i/2, j))
        if f != calculation_arccos:
            Y.append(sum(lst))
        else:
            Y.append(pi/2-sum(lst))
    return X, Y