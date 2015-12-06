#!/usr/bin/python

import re


def is_nice_1(word):
    has_vowels = len(re.sub('[^aeiou]+', '', word)) >= 3
    has_doubles = re.search('(.)\\1', word) is not None
    has_bad_letters = re.search('ab|cd|pq|xy', word) is not None
    return has_vowels and has_doubles and not has_bad_letters


def is_nice_2(word):
    has_repeated_pair = re.search('(..).*?\\1', word) is not None
    has_repeated_letter = re.search('(.).\\1', word) is not None
    return has_repeated_pair and has_repeated_letter


with open('5.txt', 'r') as file:
    input = file.read()

nice_1 = 0
nice_2 = 0
for string in input.splitlines():
    if is_nice_1(string):
        nice_1 += 1
    if is_nice_2(string):
        nice_2 += 1

print(nice_1)
print(nice_2)
