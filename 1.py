#!/usr/bin/python

with open('1.txt', 'r') as file:
    input = file.read()

floor = 0
position = 1

while True:
    floor += 1 if input[position - 1] == '(' else -1

    if floor < 0:
        print('Position %s' % position)
        break

    position += 1
