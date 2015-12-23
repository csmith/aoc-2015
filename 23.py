import re


def set_register(r, v):
    global registers
    registers[r] = v

registers = {'a': 1, 'b': 0, 'pc': 0}
program = [re.split(',? ', line) for line in open('23.txt', 'r').read().splitlines()]
instructions = {
    'hlf': lambda args: set_register(args[0], registers[args[0]] / 2),
    'tpl': lambda args: set_register(args[0], registers[args[0]] * 3),
    'inc': lambda args: set_register(args[0], registers[args[0]] + 1),
    'jmp': lambda args: set_register('pc', registers['pc'] + (int(args[0]) - 1)),
    'jie': lambda args: set_register('pc', registers['pc'] + (int(args[1]) - 1 if registers[args[0]] % 2 == 0 else 0)),
    'jio': lambda args: set_register('pc', registers['pc'] + (int(args[1]) - 1 if registers[args[0]] == 1 else 0))
}

try:
    while True:
        line = program[registers['pc']]
        instructions[line[0]](line[1:])
        registers['pc'] += 1
except LookupError:
    print(registers['b'])
