#!/bin/python

# 2024-12 Matt Perry mjperry82@gmail.com
# adventofcode 2024 day3

import re

from pathlib import Path

input_file = "input"
directory = Path.cwd()

in_file = directory / input_file

mul_reg = r'mul[(]\d+,\d+[)]'
do_reg = r'do\(\)'
dont_reg = r"don't\(\)"

def load_input():
    s = ''
    with open(in_file, 'r') as file:
        s = file.read()

    return s

def process_mul(mul_string):
    s = mul_string.replace('mul(', '')
    s = s.replace(')', '')
    s = s.split(',')

    return int(s[0]) * int(s[1])

def process_input(s):
    mul_sum = 0
    while True:
        mul_match = re.search(mul_reg, s)
        dont_match = re.search(dont_reg, s)
        do_match = re.search(do_reg, s)

        if dont_match:
            dont_end = dont_match.end()
        else:
            dont_end = len(s) - 1

        if do_match:
            do_end = do_match.end()
        else:
            do_end = len(s) - 1

        if mul_match and mul_match.end() <= dont_end:
            mul_string = s[mul_match.start():mul_match.end()]
            s = s[mul_match.end():]
            mul_sum += process_mul(mul_string)
        elif mul_match:
            do_match = re.search(do_reg, s)
            s = s[do_end:]
        else:
            return mul_sum

def main():
    s = load_input()
    mul_sum = process_input(s)

    print(mul_sum)

if __name__ == "__main__":
    main()
