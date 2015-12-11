#!/usr/bin/python

from string import ascii_lowercase
from itertools import takewhile
import re

input = 'cqjxjnds'

run_regex = '|'.join(ascii_lowercase[i:i+3] for i in range(24))
next_letter = dict((l, chr(ord(l) + 1)) for l in ascii_lowercase)
next_letter['h'] = 'j'
next_letter['n'] = 'p'
next_letter['k'] = 'm'
next_letter['z'] = 'a'


def increment(str):
    tail = sum(1 for _ in takewhile(lambda x: x == 'z', str[::-1]))
    next = list(str)
    if tail < len(next):
        next[-tail - 1] = next_letter[next[-tail - 1]]
    if tail > 0:
        next[-tail:] = 'a' * tail
    return ''.join(next)


def matches(str):
    has_run = re.search(run_regex, str)
    has_bad_letters = re.search('[iol]', str)
    has_pairs = re.search(r'(.)(\1).*?(?!\1)(.)(\3)', str)
    return has_run and has_pairs and not has_bad_letters


for _ in range(2):
    input = increment(input)
    while not matches(input):
        input = increment(input)
    print(input)
