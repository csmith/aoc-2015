from itertools import combinations

with open('17.txt', 'r') as file:
    lines = map(int, file.readlines())
    count = [[sum(c) for c in combinations(lines, n + 1)].count(150) for n in range(len(lines))]
    print("Total: %s   Minimum: %s" % (sum(count), next(x for x in count if x)))
