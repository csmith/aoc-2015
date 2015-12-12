#!/usr/bin/python

import json
import re

with open('12.txt', 'r') as file:
    input = file.read()

print("Part 1: %d" % sum(int(x) for x in re.findall('-?[0-9]+', input)))


def process(obj):
    if isinstance(obj, dict):
        if 'red' in obj.values():
            return 0
        else:
            return process(obj.values())

    if isinstance(obj, list):
        return sum(process(x) for x in obj)

    if isinstance(obj, int):
        return obj

    return 0


print("Part 2: %d" % process(json.loads(input)))
