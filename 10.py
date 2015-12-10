#!/usr/bin/python

import re

input = '1113222113'

for _ in range(50):
    input = ''.join(str(1 + len(m[1])) + m[0] for m in re.findall('(.)(\\1*)', input))

print len(input)
