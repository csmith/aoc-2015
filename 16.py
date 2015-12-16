#!/usr/bin/python

import re

target = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

low, high = ['cats', 'trees'], ['goldfish', 'pomeranians']

with open('16.txt', 'r') as file:
    for i, line in enumerate(file.readlines()):
        for k, v in re.findall('([a-z]+): ([0-9]+)', line):
            vs = '|'.join(str(x) for x in (range(int(v)) if k in low else
                                           range(int(v) + 1, 11) if k in high else [v]))
            if not re.search('%s: (%s)$' % (k, vs), target, re.M):
                break
        else:
            print('SUE %d' % (i + 1))
