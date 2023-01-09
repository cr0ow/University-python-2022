import random as rand
from math import sqrt


def random(n):
    result = []
    for i in range(n):
        result.append(int(rand.random() * 1000))
    return result


def almost_sorted(n):
    result = []
    for i in range(n):
        result.append(i)
    for i in range(max(3, int(n / 100))):
        idx1 = int(rand.random() * n)
        idx2 = int(rand.random() * n)
        result[idx1], result[idx2] = result[idx2], result[idx1]
    return result


def almost_sorted_reverted(n):
    result = almost_sorted(n)
    result.reverse()
    return result


def random_gauss(n):
    result = []
    for i in range(n):
        result.append(rand.gauss(100, 50))
    return result


def random_from_set(n):
    k = int(sqrt(n))
    result = []
    for i in range(n):
        result.append(int(rand.random() * k))
    return result
