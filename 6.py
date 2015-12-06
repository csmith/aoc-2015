#!/usr/bin/python

PART_TWO = True


def turn_on(old):
    return old + 1 if PART_TWO else True


def turn_off(old):
    return max(0, old - 1) if PART_TWO else False


def toggle(old):
    return old + 2 if PART_TWO else not old


with open('6.txt', 'r') as file:
    input = file.read()

state = [[0 if PART_TWO else False for x in range(1000)] for y in range(1000)]

for line in input.splitlines():
    if line.startswith('turn on'):
        action = turn_on
        line = line[8:]
    elif line.startswith('turn off'):
        action = turn_off
        line = line[9:]
    else:
        action = toggle
        line = line[7:]

    ((x1, y1), (x2, y2)) = [coord.split(',') for coord in line.split(' through ')]

    for x in range(int(x1), int(x2) + 1):
        for y in range(int(y1), int(y2) + 1):
            state[x][y] = action(state[x][y])

count = sum([sum(col) for col in state])
print(count)
