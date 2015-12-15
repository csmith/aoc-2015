#!/usr/bin/python

import operator
import functools
from collections import defaultdict

PART_TWO = True

ingredients = []

with open('15.txt', 'r') as file:
    for line in file.readlines():
        _, details = line.split(': ')
        ingredients.append({p: int(v) for p, v in (x.split(' ') for x in details.split(', '))})


def sums(n, target):
    if n == 1:
        yield [target]
    else:
        for i in xrange(target + 1):
            for j in sums(n - 1, target - i):
                yield [i] + j


def score(amounts):
    properties = defaultdict(int)

    for i, amount in enumerate(amounts):
        for k, v in ingredients[i].iteritems():
            properties[k] += v * amount

    if properties.pop('calories') != 500 and PART_TWO:
        return -1

    return functools.reduce(operator.mul, (max(0, v) for v in properties.values()))


print(max(map(score, sums(len(ingredients), 100))))
