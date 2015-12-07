#!/usr/bin/python

import re

wires = {}
functions = {
    'AND': lambda left, right: lambda: left() & right(),
    'OR': lambda left, right: lambda: left() | right(),
    'LSHIFT': lambda left, right: lambda: left() << right(),
    'RSHIFT': lambda left, right: lambda: left() >> right(),
    'NOT': lambda value: lambda: ~ value()
}

def get_wire(name):
    if (name.isdigit()):
        return int(name)

    if hasattr(wires[name], '__call__'):
        wires[name] = wires[name]()

    return wires[name]

def handle_input(text):
    binary_match = re.match('^(.*?) (AND|OR|LSHIFT|RSHIFT) (.*?)$', text)
    if binary_match:
        (left, operator, right) = binary_match.group(1, 2, 3)
        return functions[operator](lambda: get_wire(left), lambda: get_wire(right))

    unary_match = re.match('^(NOT) (.*?)$', text)
    if unary_match:
        (operator, value) = unary_match.group(1, 2)
        return functions[operator](lambda: get_wire(value))

    return lambda: get_wire(text)

def initialise():
    with open('7.txt', 'r') as file:
        input = file.read()

    for line in input.splitlines():
        (input, output) = line.split(' -> ')
        wires[output] = handle_input(input)

initialise()
part_1 = wires['a']()
print('Part 1: %s' % part_1)

initialise()
wires['b'] = part_1
print('Part 2: %s' % wires['a']())
