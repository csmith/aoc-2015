#!/usr/bin/python

from collections import defaultdict
from itertools import permutations
import re

pattern = re.compile('^(.*) would (lose|gain) ([0-9]+) happiness .* next to (.*).')
happiness = defaultdict(int)
names = set()

with open('13.txt', 'r') as file:
    for line in file.readlines():
        first, type, value, second = pattern.match(line).groups()
        happiness[frozenset((first, second))] += (-1 if type == 'lose' else 1) * int(value)
        names.add(first)


def get_score(order):
    return sum(happiness[frozenset(pair)] for pair in zip(order, order[1:] + [order[0]]))


def find_best(people):
    remaining = people.copy()
    first = remaining.pop()
    return max(get_score([first] + list(order)) for order in permutations(remaining))


print(find_best(names))
print(find_best(names.union("me")))
