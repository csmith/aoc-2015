#!/usr/bin/python

from collections import defaultdict
import re

subs = defaultdict(list)

with open('19.txt', 'r') as f:
    lines = f.read().splitlines()
    gen = set()
    long = lines[-1]
    for search, replace in [line.split(' => ') for line in lines[0:-2]]:
        for start, end in [(i.start(), i.end()) for i in re.finditer(search, long)]:
            gen.add(long[0:start] + replace + long[end:])
    print(len(gen))

# --- This is ugly as sin, and I've no idea why it seems to work. ¯\_(ツ)_/¯

with open('19.txt', 'r') as f:
    lines = f.read().splitlines()
    long = lines[-1]
    for search, replace in [line.split(' => ') for line in lines[0:-2]]:
        subs[search].append(replace)
    results = set([long])
    previous = set([long])
    step = 0
    while True:
        step += 1
        new_results = set()
        for candidate in results:
            for search, replacements in subs.iteritems():
                for replacement in replacements:
                    for start, end in [(i.start(), i.end()) for i in re.finditer(replacement, candidate)]:
                        r = candidate[0:start] + search + candidate[end:]
                        if r not in previous:
                            new_results.add(r)
                            previous.add(r)
        shortest = min(len(x) for x in new_results)
        new_results = set(list({r for r in new_results if len(r) == shortest})[:1])
        print("%s (%s)" % (step, len(new_results)))
        if 'e' in new_results:
            print("*** %s" % step)
            break
        results = new_results
