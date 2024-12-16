#!/bin/python

# 2024-12 Matt Perry mjperry82@gmail.com
# adventofcode 2024 day3

import re

from pathlib import Path

input_file = "input"
directory = Path.cwd()

in_file = directory / input_file

regex = r'mul[(]\d+,\d+[)]'

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
        match = re.search(regex, s)

        if match:
            mul_string = s[match.start():match.end()]
            s = re.sub(regex, '', s, count=1)
            mul_sum += process_mul(mul_string)
        else:
            return mul_sum

def main():
    s = load_input()
    mul_sum = process_input(s)

    print(mul_sum)

if __name__ == "__main__":
    main()
