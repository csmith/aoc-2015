#!/usr/bin/python3

SIZE = 100
PART_TWO = True

to_bool = lambda char: char == '#'
get_range = lambda x: range(-1 if x > 0 else 0, 2 if x < SIZE - 1 else 1)


def step_one(lights, x, y, state):
    n = sum(lights[y + i][x + j] for i in get_range(y) for j in get_range(x) if i != 0 or j != 0)
    return n == 3 or (n == 2 and state)


def with_broken_lights(lights):
    if PART_TWO:
        for y, x in zip([0, 0, SIZE-1, SIZE-1], [0, SIZE-1] * 2):
            lights[y][x] = True
    return lights


def step(lights):
    return with_broken_lights([[step_one(lights, x, y, cell) for x, cell in enumerate(line)]
                              for y, line in enumerate(lights)])

with open('18.txt', 'r') as f:
    lights = with_broken_lights([list(map(to_bool, line)) for line in f.read().splitlines()])

for _ in range(100):
    lights = step(lights)

print(sum(sum(line) for line in lights))
