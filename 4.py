#!/usr/bin/python

import hashlib

input = 'ckczppom'
count = -1
hash = '111111'

while hash[0:6] != '000000':
    count += 1
    hash = hashlib.md5("%s%s" % (input, count)).hexdigest()

print(count)
print(hash)
