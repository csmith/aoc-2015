#!/usr/bin/python

with open('3.txt', 'r') as file:
    input = file.read()

locations = [[0, 0], [0, 0]]
visited = {'0,0': True}
i = 0

for dir in input:
    if dir == '^':
        locations[i][1] -= 1
    if dir == 'v':
        locations[i][1] += 1
    if dir == '>':
        locations[i][0] += 1
    if dir == '<':
        locations[i][0] -= 1

    visited['%s,%s' % (locations[i][0], locations[i][1])] = True
    i = 1 - i  # (Remove this line if only Santa is delivering)

print(len(visited))
