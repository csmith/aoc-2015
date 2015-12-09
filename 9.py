#!/usr/bin/python

import re

with open('9.txt', 'r') as file:
    input = file.read()

FUNC = max  # min for part 1

distances = {}
places = {}

for line in input.splitlines():
    (source, dest, distance) = re.match('^(.*?) to (.*?) = ([0-9]+)$', line).group(1, 2, 3)
    distances[(source, dest)] = int(distance)
    distances[(dest, source)] = int(distance)
    places[dest] = True
    places[source] = True

places = places.keys()


def without(list, item):
    return [x for x in list if x != item]


def find_shortest(current, to_visit):
    if len(to_visit) == 0:
        return 0

    return FUNC([distances[(current, target)] +
                find_shortest(target, without(to_visit, target))
                for target in to_visit])

print(FUNC([find_shortest(place, without(places, place)) for place in places]))
