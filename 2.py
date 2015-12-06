#!/usr/bin/python

with open('2.txt', 'r') as file:
    input = file.read()

paper = 0
ribbon = 0

for line in input.split('\n'):
    (w, h, d) = [int(x) for x in line.split('x')]
    areas = [w*h, w*d, h*d]
    perims = [2 * x for x in [w+h, w+d, h+d]]
    paper += sum(areas) * 2 + min(areas)
    ribbon += min(perims) + w*h*d

print("Paper: %s" % paper)
print("Ribbon: %s" % ribbon)
