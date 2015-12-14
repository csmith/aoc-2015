#!/usr/bin/python

import re
from collections import defaultdict

at = 2503
pattern = re.compile('^(.*) can fly ([0-9]+) .*? for ([0-9]+) seconds, .* for ([0-9]+) seconds.')
reindeer = {}

with open('14.txt', 'r') as file:
    for line in file.readlines():
        name, speed, speed_period, rest_period = pattern.match(line).groups()
        reindeer[name] = (int(speed), int(speed_period), int(rest_period))


def distance_at(reindeer_spec, time):
    speed, speed_period, rest_period = reindeer_spec
    cycle_period = speed_period + rest_period
    return speed * (speed_period * (time // cycle_period) + min(speed_period, time % cycle_period))

print(max(distance_at(v, at) for v in reindeer.values()))

points = defaultdict(int)
for i in range(at):
    distances = {r[0]: distance_at(r[1], i + 1) for r in reindeer.iteritems()}
    for n in [n for n, d in distances.iteritems() if d == max(distances.values())]:
        points[n] += 1

print(max(points.values()))
