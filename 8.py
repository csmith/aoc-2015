#!/usr/bin/python

import re

with open('8.txt', 'r') as file:
    input = file.read()

difference = 0
for line in input.splitlines():
    (remaining, count) = re.subn('^"|"$', '', line)
    difference += count
    (remaining, count) = re.subn('\\\\\\\\', '', remaining)
    difference += count
    (remaining, count) = re.subn('\\\\"', '', remaining)
    difference += count
    (remaining, count) = re.subn('\\\\x[a-fA-F0-9]{2}', '', remaining)
    difference += count * 3

print(difference)

difference = 0
for line in input.splitlines():
    difference += 2
    (remaining, count) = re.subn('"', '', line)
    difference += count
    (remaining, count) = re.subn('\\\\', '', remaining)
    difference += count

print(difference)
